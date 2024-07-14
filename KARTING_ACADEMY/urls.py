from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from django.views.i18n import set_language

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path('admin/', admin.site.urls),
    path('set_language/', set_language, name='set_language'),
]

urlpatterns += i18n_patterns(
    path('', include('main.urls')),
    path('tracks/', include('app_track.urls')),
    path('gallery/', include('app_gallery.urls')),
    path('news/', include('app_news.urls')),
)
