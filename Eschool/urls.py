from django.contrib import admin
from django.urls import path, include
from . import settings
from core.views import error_404
from django.conf import settings
from django.conf.urls.static import  static

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('class/', include('class.urls')),
    path('forum/', include('forum.urls')),
    path('notification/', include('notification.urls')),
    path(r'tests/', include('quiz.urls')),
]

# handler404 = error_404
# handler500 = error_404
urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
if settings.DEBUG == False:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT) 
    urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATICFILES_DIRS)
