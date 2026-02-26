from django.shortcuts import render, get_object_or_404
from .models import ReviewItem, Review

def index(request):
    items = ReviewItem.objects.all()
    return render(request, 'review_system/index.html', {'items': items})

def item_detail(request, pk):
    item = get_object_or_404(ReviewItem, pk=pk)
    reviews = item.reviews.all().order_by('-created_at')
    if request.method == 'POST' and request.user.is_authenticated:
        Review.objects.create(
            item=item,
            user=request.user,
            rating=request.POST.get('rating', 5),
            title=request.POST.get('title', ''),
            body=request.POST.get('body', ''),
        )
        from django.shortcuts import redirect
        return redirect('review_system:item_detail', pk=pk)
    avg = sum(r.rating for r in reviews) / len(reviews) if reviews else 0
    return render(request, 'review_system/detail.html', {'item': item, 'reviews': reviews, 'avg': round(avg, 1)})
