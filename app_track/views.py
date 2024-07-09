from django.shortcuts import render

from app_track.models import Track
from services.services import obj_all

def tracks(request):
    context = {
        'tracks': obj_all(Track),
    }
    return render(request, 'tracks/tracks.html', context=context)
