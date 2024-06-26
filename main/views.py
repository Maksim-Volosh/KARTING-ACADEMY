from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from app_gallery.models import Gallery
from app_gallery.services import get_last_ten_photos
from app_news.models import News
from app_news.services import get_last_three_news
from app_partners.models import Partner
from app_partners.services import get_partners
from main.models import Category, Event, Player, Statistics
from main.services import *
from services.services import *


def index(request):
    event = get_last_event(Event)
    
    if obj_count(Category) > 0:
        statistic = junior_stats(Statistics, event)
    else:
        statistic = all_stats(Statistics, event)
    
    partners = get_partners(Partner)   
    news = get_last_three_news(News)
    next_event = get_next_event(Event)
    
    if next_event:
        next_event_time = timezone.localtime(next_event.date_of_start).strftime("%Y-%m-%d %H:%M:%S")
    else: next_event_time = 0   
    
    gallery = get_last_ten_photos(Gallery, 1080)  
    
    context = {
        'event': event,
        'statistic': statistic,
        'partners': partners,
        'news': news,
        'next_event': next_event,
        'next_event_time': next_event_time,
        'gallery': gallery,
    }
    return render(request, 'main/index.html', context=context)


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    
    cat_name = request.GET.get('cat')
    
    if cat_name:
        statistics = category_event_detail_stats(Statistics, event, cat_name)
    else:
        statistics = event_detail_stats(Statistics, event)
    
    player_stats = {}
    for stat in statistics:
        player = stat.player
        if player not in player_stats:
            player_stats[player] = []
        player_stats[player].append(stat)

    context = {
        'event': event,
        'player_stats': player_stats,
    }
    
    return render(request, 'main/event-detail.html', context=context)

def player_detail(request, pk):
    player = get_object_or_404(Player, pk=pk)
    events = player_events_all(player)
    context = {
        'player': player,
        'events': events
    }
    return render(request, 'main/player-detail.html', context=context)
