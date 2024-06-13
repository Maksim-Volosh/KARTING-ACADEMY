from django.urls import path
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('', index, name='index'),
    # path('event/<int:pk>/', event_detail, name='event_detail'),
    path('send-email/', send_email, name='send_email'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)