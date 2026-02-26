from django.shortcuts import render, get_object_or_404
from .models import AdCampaign

def index(request):
    campaigns = AdCampaign.objects.filter(is_active=True).order_by('-start_date')
    total_impressions = sum(c.impressions for c in campaigns)
    total_clicks = sum(c.clicks for c in campaigns)
    return render(request, 'ad_manager/index.html', {
        'campaigns': campaigns,
        'total_impressions': total_impressions,
        'total_clicks': total_clicks,
    })
