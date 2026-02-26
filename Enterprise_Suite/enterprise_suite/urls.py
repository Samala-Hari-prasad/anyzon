from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),
    
    # App URLs
    path('auth/', include('auth_system.urls')),
    path('profiles/', include('user_profiles.urls')),
    path('inventory/', include('inventory_manager.urls')),
    path('tasks/', include('task_scheduler.urls')),
    path('expenses/', include('expense_tracker.urls')),
    path('notifications/', include('notification_hub.urls')),
    path('documents/', include('document_vault.urls')),
    path('feedback/', include('feedback_collector.urls')),
    path('analytics/', include('analytics_dashboard.urls')),
    path('helpdesk/', include('help_desk.urls')),
    path('settings/', include('settings_panel.urls')),
    path('audit/', include('audit_log.urls')),
    path('mail/', include('mail_client.urls')),
    path('calendar/', include('calendar_sync.urls')),
    path('search/', include('search_engine.urls')),
    path('api/', include('api_gateway.urls')),
    path('billing/', include('billing_module.urls')),
    path('roles/', include('role_manager.urls')),
    path('backup/', include('backup_service.urls')),
    path('assets/', include('asset_library.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
