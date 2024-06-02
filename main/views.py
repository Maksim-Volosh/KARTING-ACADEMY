from django.shortcuts import render
from .models import Event, Statistics

def index(request):
    event = Event.last_event(Event)
    
    statistic = Statistics.objects.filter(event=event).select_related('player').values(
        'player__name', 'player__nationality', 'lap_time', 'points'
    )
    
    context = {
        'event': event,
        'statistic': statistic
    }
    return render(request, 'main/index.html', context=context)
