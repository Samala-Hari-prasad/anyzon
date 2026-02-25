from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Category, CartItem, Order, OrderItem, Profile
from .forms import UserUpdateForm, ProfileUpdateForm
import json

# ---------------------------------------------------------------------------
# HELPER
# ---------------------------------------------------------------------------
def _get_base_context(request):
    categories = Category.objects.all()
    cart_count = 0
    if request.user.is_authenticated:
        cart_count = CartItem.objects.filter(user=request.user).count()
    elif request.session.session_key:
        cart_count = CartItem.objects.filter(session_key=request.session.session_key).count()
    return categories, cart_count

# ---------------------------------------------------------------------------
# CORE PAGES
# ---------------------------------------------------------------------------
def product_list(request):
    query = request.GET.get('q')
    category_slug = request.GET.get('category')
    products = Product.objects.all()
    categories, cart_count = _get_base_context(request)
    if query:
        products = products.filter(name__icontains=query) | products.filter(description__icontains=query)
    if category_slug:
        products = products.filter(category__slug=category_slug)
    return render(request, 'anyzon/index.html', {
        'products': products, 'categories': categories,
        'cart_count': cart_count, 'search_query': query,
        'selected_category': category_slug,
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    categories, cart_count = _get_base_context(request)
    related_products = Product.objects.filter(category=product.category).exclude(slug=slug)[:6]
    return render(request, 'anyzon/product_detail.html', {
        'product': product, 'categories': categories,
        'cart_count': cart_count, 'related_products': related_products,
    })

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.user.is_authenticated:
        cart_item, created = CartItem.objects.get_or_create(
            product=product, user=request.user)
    else:
        if not request.session.session_key:
            request.session.create()
        cart_item, created = CartItem.objects.get_or_create(
            product=product, session_key=request.session.session_key)
            
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_view')

def cart_view(request):
    cart_items = []
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
    else:
        if not request.session.session_key:
            request.session.create()
        cart_items = CartItem.objects.filter(session_key=request.session.session_key)
        
    total = sum(item.total_price() for item in cart_items)
    categories, cart_count = _get_base_context(request)
    return render(request, 'anyzon/cart.html', {
        'cart_items': cart_items, 'total': total,
        'categories': categories, 'cart_count': cart_count,
    })

def checkout(request):
    cart_items = []
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
    elif request.session.session_key:
        cart_items = CartItem.objects.filter(session_key=request.session.session_key)
    else:
        return redirect('product_list')
        
    total = sum(item.total_price() for item in cart_items)
    categories, cart_count = _get_base_context(request)
    return render(request, 'anyzon/checkout.html', {
        'cart_items': cart_items, 'total': total,
        'categories': categories, 'cart_count': cart_count,
    })

def payment(request):
    if request.method == 'POST':
        if not request.session.session_key and not request.user.is_authenticated:
            return redirect('product_list')
        
        cart_items = []
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user)
        else:
            cart_items = CartItem.objects.filter(session_key=request.session.session_key)
            
        total = sum(item.total_price() for item in cart_items)
        payment_method = request.POST.get('payment_method', 'Card')
        
        order_data = {
            'full_name': request.user.get_full_name() or request.user.username if request.user.is_authenticated else "Guest User",
            'address': "H-45, Sector 62, Noida, Uttar Pradesh, 201301", # Still hardcoded but better
            'total_paid': total,
            'payment_method': payment_method,
        }
        
        if request.user.is_authenticated:
            order_data['user'] = request.user
        else:
            order_data['session_key'] = request.session.session_key
            
        order = Order.objects.create(**order_data)
        
        for item in cart_items:
            OrderItem.objects.create(
                order=order, product=item.product,
                price=item.product.price, quantity=item.quantity,
            )
        cart_items.delete()
        return render(request, 'anyzon/payment_success.html', {'order_id': order.id})
    return render(request, 'anyzon/payment.html')

def order_history(request):
    orders = []
    if request.user.is_authenticated:
        orders = Order.objects.filter(user=request.user).order_by('-created_at')
    elif request.session.session_key:
        orders = Order.objects.filter(session_key=request.session.session_key).order_by('-created_at')
    categories, cart_count = _get_base_context(request)
    return render(request, 'anyzon/order_history.html', {
        'orders': orders, 'categories': categories, 'cart_count': cart_count,
    })

def remove_from_cart(request, item_id):
    if request.user.is_authenticated:
        item = get_object_or_404(CartItem, id=item_id, user=request.user)
    else:
        item = get_object_or_404(CartItem, id=item_id, session_key=request.session.session_key)
    item.delete()
    return redirect('cart_view')

# ---------------------------------------------------------------------------
# EXTRA PAGES (About, Deals, Wishlist, Seller, Contact)
# ---------------------------------------------------------------------------
def wishlist(request):
    categories, cart_count = _get_base_context(request)
    wishlist_products = Product.objects.filter(category__slug='electronics')[:8]
    return render(request, 'anyzon/wishlist.html', {
        'categories': categories, 'cart_count': cart_count,
        'wishlist_products': wishlist_products,
    })

def about(request):
    categories, cart_count = _get_base_context(request)
    return render(request, 'anyzon/about.html', {
        'categories': categories, 'cart_count': cart_count,
    })

def deals(request):
    categories, cart_count = _get_base_context(request)
    deal_products = Product.objects.order_by('price')[:20]
    return render(request, 'anyzon/deals.html', {
        'categories': categories, 'cart_count': cart_count,
        'deal_products': deal_products,
    })

def become_seller(request):
    categories, cart_count = _get_base_context(request)
    return render(request, 'anyzon/become_seller.html', {
        'categories': categories, 'cart_count': cart_count,
    })

def contact(request):
    categories, cart_count = _get_base_context(request)
    submitted = False
    if request.method == 'POST':
        submitted = True
    return render(request, 'anyzon/contact.html', {
        'categories': categories, 'cart_count': cart_count, 'submitted': submitted,
    })

@login_required(login_url='login')
def user_profile(request):
    categories, cart_count = _get_base_context(request)
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    total_spent = sum(o.total_paid for o in orders)
    wishlist_count = Product.objects.filter(category__slug='electronics').count()
    return render(request, 'anyzon/profile.html', {
        'categories': categories,
        'cart_count': cart_count,
        'orders': orders,
        'total_spent': total_spent,
        'wishlist_count': wishlist_count,
    })

# ---------------------------------------------------------------------------
# AUTHENTICATION
# ---------------------------------------------------------------------------
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Transfer guest cart to user
                if request.session.session_key:
                    CartItem.objects.filter(session_key=request.session.session_key).update(user=user, session_key=None)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('product_list')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    
    categories, cart_count = _get_base_context(request)
    return render(request, 'anyzon/login.html', {
        'form': form, 'categories': categories, 'cart_count': cart_count, 'hide_nav': True
    })

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('product_list')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = UserCreationForm()
    
    categories, cart_count = _get_base_context(request)
    return render(request, 'anyzon/register.html', {
        'form': form, 'categories': categories, 'cart_count': cart_count, 'hide_nav': True
    })

@login_required(login_url='login')
def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('user_profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
 
    categories, cart_count = _get_base_context(request)
    return render(request, 'anyzon/edit_profile.html', {
        'u_form': u_form,
        'p_form': p_form,
        'categories': categories,
        'cart_count': cart_count
    })

def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('product_list')

# ---------------------------------------------------------------------------
# STYLE ZONE (Fashion Hub)
# ---------------------------------------------------------------------------
def style_zone(request):
    categories, cart_count = _get_base_context(request)
    men_products    = Product.objects.filter(category__slug='mens-fashion')[:6]
    women_products  = Product.objects.filter(category__slug='womens-fashion')[:6]
    kids_products   = Product.objects.filter(category__slug='kids-fashion')[:6]
    return render(request, 'anyzon/style_zone.html', {
        'categories': categories, 'cart_count': cart_count,
        'men_products': men_products,
        'women_products': women_products,
        'kids_products': kids_products,
    })

def style_gender(request, gender):
    """Gender-specific fashion page: men / women / kids."""
    categories, cart_count = _get_base_context(request)
    slug_map = {'men': 'mens-fashion', 'women': 'womens-fashion', 'kids': 'kids-fashion'}
    label_map = {'men': "Men's Style", 'women': "Women's Style", 'kids': "Kids' Style"}
    hero_map = {
        'men':   ('https://images.unsplash.com/photo-1617137968427-85924c800a22?w=1200&q=80&auto=format&fit=crop', '#1a1a2e', '#e8b4b8'),
        'women': ('https://images.unsplash.com/photo-1483985988355-763728e1935b?w=1200&q=80&auto=format&fit=crop', '#2d1b69', '#f8bbd9'),
        'kids':  ('https://images.unsplash.com/photo-1503454537195-1dcabb73ffb9?w=1200&q=80&auto=format&fit=crop', '#1b5e20', '#c8e6c9'),
    }
    gender = gender.lower()
    if gender not in slug_map:
        return redirect('style_zone')
    cat_slug  = slug_map[gender]
    title     = label_map[gender]
    hero_img, hero_dark, hero_accent = hero_map[gender]
    products  = Product.objects.filter(category__slug=cat_slug)
    return render(request, 'anyzon/style_gender.html', {
        'categories': categories, 'cart_count': cart_count,
        'products': products, 'gender': gender,
        'title': title, 'hero_img': hero_img,
        'hero_dark': hero_dark, 'hero_accent': hero_accent,
    })

# ---------------------------------------------------------------------------
# CATEGORY LANDING PAGES
# ---------------------------------------------------------------------------

# Config: slug -> (display name, emoji, hero_gradient, hero_image, sub_labels)
CATEGORY_CONFIG = {
    'mobiles': {
        'name': 'Mobiles',
        'emoji': '📱',
        'gradient': 'linear-gradient(135deg,#0f2027,#203a43,#2c5364)',
        'hero_img': 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=1200&q=80&auto=format&fit=crop',
        'subs': ['Smartphones', '5G Phones', 'Budget Phones', 'Premium Phones'],
    },
    'electronics': {
        'name': 'Electronics',
        'emoji': '💻',
        'gradient': 'linear-gradient(135deg,#141e30,#243b55)',
        'hero_img': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200&q=80&auto=format&fit=crop',
        'subs': ['Laptops', 'Cameras', 'Headphones', 'Smart TV', 'Tablets'],
    },
    'fashion': {
        'name': 'Fashion',
        'emoji': '👗',
        'gradient': 'linear-gradient(135deg,#ad1457,#880e4f)',
        'hero_img': 'https://images.unsplash.com/photo-1483985988355-763728e1935b?w=1200&q=80&auto=format&fit=crop',
        'subs': ["Men's Wear", "Women's Wear", "Kids' Wear", 'Footwear', 'Accessories'],
    },
    'home-kitchen': {
        'name': 'Home & Kitchen',
        'emoji': '🏠',
        'gradient': 'linear-gradient(135deg,#1b5e20,#2e7d32)',
        'hero_img': 'https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=1200&q=80&auto=format&fit=crop',
        'subs': ['Cookware', 'Bedding', 'Furniture', 'Decor', 'Kitchenware'],
    },
    'appliances': {
        'name': 'Appliances',
        'emoji': '🔌',
        'gradient': 'linear-gradient(135deg,#0d47a1,#1565c0)',
        'hero_img': 'https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?w=1200&q=80&auto=format&fit=crop',
        'subs': ['Air Conditioners', 'Refrigerators', 'Washing Machines', 'Microwaves', 'Air Fryers'],
    },
    'books': {
        'name': 'Books',
        'emoji': '📚',
        'gradient': 'linear-gradient(135deg,#4a148c,#6a1b9a)',
        'hero_img': 'https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=1200&q=80&auto=format&fit=crop',
        'subs': ['Bestsellers', 'Self-Help', 'Fiction', 'Academic', 'Biographies'],
    },
    'sports-fitness': {
        'name': 'Sports & Fitness',
        'emoji': '⚽',
        'gradient': 'linear-gradient(135deg,#bf360c,#e64a19)',
        'hero_img': 'https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b?w=1200&q=80&auto=format&fit=crop',
        'subs': ['Cricket', 'Football', 'Gym Equipment', 'Yoga', 'Running Gear'],
    },
}

def category_landing(request, slug):
    categories, cart_count = _get_base_context(request)
    config = CATEGORY_CONFIG.get(slug, {
        'name': slug.replace('-', ' ').title(),
        'emoji': '🏷️',
        'gradient': 'linear-gradient(135deg,#131921,#232f3e)',
        'hero_img': '',
        'subs': [],
    })
    products = Product.objects.filter(category__slug=slug)
    return render(request, 'anyzon/category_landing.html', {
        'categories': categories, 'cart_count': cart_count,
        'products': products, 'config': config, 'slug': slug,
    })
