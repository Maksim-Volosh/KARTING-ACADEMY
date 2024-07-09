from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('tracks/', include('app_track.urls')),
    path('gallery/', include('app_gallery.urls')),
    path('news/', include('app_news.urls')),
]
