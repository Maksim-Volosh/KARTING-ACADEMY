from django.urls import path
from django.conf.urls.static import static

from KARTING_ACADEMY import settings
from main.send_email import send_email

from .views import *

urlpatterns = [
    path('', index, name='index'),
    # path('event/<int:pk>/', event_detail, name='event_detail'),
    path('send-email/', send_email, name='send_email'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)