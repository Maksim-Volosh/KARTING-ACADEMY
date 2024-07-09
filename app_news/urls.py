from django.conf.urls.static import static
from django.urls import path

from KARTING_ACADEMY import settings

from .views import *

urlpatterns = [
    path('', news_list, name='news-list'),
    path('<int:nid>/', news_detail, name='news-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)