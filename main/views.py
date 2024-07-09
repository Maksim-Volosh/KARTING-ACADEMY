from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from app_gallery.models import Gallery
from app_gallery.services import get_last_ten_photos
from app_news.models import News
from app_news.services import get_last_three_news
from main.models import Category, Event, Player, Statistics
from main.services import *
from services.services import *


def index(request):
    event = get_last_event(Event)
    
    if obj_count(Category) > 0:
        statistic = junior_stats(Statistics, event)
    else:
        statistic = all_stats(Statistics, event)
  
    news = get_last_three_news(News)
    next_event = get_next_event(Event)
    
    if next_event:
        next_event_time = timezone.localtime(next_event.date_of_start).strftime("%Y-%m-%d %H:%M:%S")
    else: next_event_time = 0   
    
    gallery = get_last_ten_photos(Gallery, 1080)  
    
    context = {
        'event': event,
        'statistic': statistic,
        'news': news,
        'next_event': next_event,
        'next_event_time': next_event_time,
        'gallery': gallery,
        'is_homepage': True
    }
    return render(request, 'main/index.html', context=context)


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    
    cat_name = request.GET.get('cat')
    
    if cat_name:
        statistics = category_event_detail_stats(Statistics, event, cat_name)
    else:
        statistics = event_detail_stats(Statistics, event)
        cat_name = "junior"
    
    player_stats = {}
    for stat in statistics:
        player = stat.player
        if player not in player_stats:
            player_stats[player] = []
        player_stats[player].append(stat)
    print(player_stats)
        
    player_gap = [0]
    prev_time = 0
    for player, stats in player_stats.items():
        for stat in stats:
            gap = float(stat.lap_time) - float(prev_time)
            prev_time = float(stat.lap_time)
            player_gap.append(gap)
        
    player_gap = [0]
    prev_time = 0
    for player, stats in player_stats.items():
        for stat in stats:
            gap = float(stat.lap_time) - float(prev_time)
            prev_time = float(stat.lap_time)
            player_gap.append(gap)
        
    best_lap_player_stats = get_best_lap_player_stats(Statistics, event, cat_name)
    if best_lap_player_stats:
        best_lap_player = str(best_lap_player_stats.player)
    else:
        best_lap_player = ''

    context = {
        'event': event,
        'player_stats': player_stats,
        'best_lap_player': best_lap_player,
        'gaps': player_gap,
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

def event_list(request):
    year = request.GET.get('y')
    
    if year:
        if year == 'all':
            events = get_events_list(Event)
        else:
            events = get_events_by_year(Event, year)
    else:
        events = get_events_list(Event)
        
    years = get_years_of_events(Event)

    context = {
        'events': events,
        'years': years,
        'selected_year': year
    }
    return render(request, 'main/event-list.html', context=context)
