from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),
    
    # App URLs
    path('blog/', include('blog_engine.urls')),
    path('forum/', include('forum_board.urls')),
    path('gallery/', include('photo_gallery.urls')),
    path('video/', include('video_streamer.urls')),
    path('portfolio/', include('portfolio_showcase.urls')),
    path('elearning/', include('e_learning.urls')),
    path('jobs/', include('job_board.urls')),
    path('events/', include('event_planner.urls')),
    path('chat/', include('chat_room.urls')),
    path('marketplace/', include('marketplace.urls')),
    path('reviews/', include('review_system.urls')),
    path('newsletter/', include('newsletter_sub.urls')),
    path('wiki/', include('wiki_pages.urls')),
    path('polls/', include('poll_maker.urls')),
    path('music/', include('music_player.urls')),
    path('recipe/', include('recipe_book.urls')),
    path('weather/', include('weather_app.urls')),
    path('quiz/', include('quiz_master.urls')),
    path('feed/', include('news_feed.urls')),
    path('ads/', include('ad_manager.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
