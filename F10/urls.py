from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Core
    path('', views.product_list, name='product_list'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart_view, name='cart_view'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment/', views.payment, name='payment'),
    path('orders/', views.order_history, name='order_history'),
    # Extra pages
    path('wishlist/', views.wishlist, name='wishlist'),
    path('about/', views.about, name='about'),
    path('deals/', views.deals, name='deals'),
    path('sell/', views.become_seller, name='become_seller'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.user_profile, name='user_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    # Auth
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    # Style Zone (Fashion Hub)
    path('style-zone/', views.style_zone, name='style_zone'),
    path('style-zone/<str:gender>/', views.style_gender, name='style_gender'),
    # Category Landing Pages
    path('category/<slug:slug>/', views.category_landing, name='category_landing'),
]
