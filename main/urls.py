from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', index, name='index'),
    # path('event/<int:pk>/', event_detail, name='event_detail'),
    path('send-email/', send_email, name='send_email'),
]
