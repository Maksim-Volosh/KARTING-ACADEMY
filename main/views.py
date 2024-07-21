from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from app_gallery.models import Gallery
from app_gallery.services import get_last_ten_photos
from app_news.models import News
from app_news.services import get_last_three_news
from main.models import Category, Event, Player, PlayerStatistic, Statistics
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
        
    player_gap = [0]
    best_lap_time = 0
    prev_time = 0
    for player, stats in player_stats.items():
        for stat in stats:
            if best_lap_time == 0:
                best_lap_time = float(stat.lap_time)
            if float(stat.lap_time) < best_lap_time:
                best_lap_time = float(stat.lap_time)
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

    context = {
        'event': event,
        'player_stats': player_stats,
        'best_lap_time': best_lap_time,
        'gaps': player_gap,
    }
    
    return render(request, 'event/event-detail.html', context=context)

def player_detail(request, pk):
    event_id = request.GET.get('ev')
    
    player = get_object_or_404(Player, pk=pk)
         
    statistics = all_stats_for_player_with_event(Statistics, player)
        
    # Создаем словарь, чтобы сгруппировать статистики по событиям
    events_with_categories = {}
    for stat in statistics:
        if stat.event not in events_with_categories:
            events_with_categories[stat.event] = []
        events_with_categories[stat.event].append(stat.category)
        
    context = {
        'player': player,
        'events_with_categories': events_with_categories
    }
    
    if event_id:
        player_event_stats = PlayerStatistic.objects.filter(player__pk=pk, event__pk=event_id).select_related('event', 'player').values(
            'event__id', 'event__image_of_track', 'event__title', 'player__id', 'player__name', 'player__surname', 'player__nationality', 'lap_number', 'lap_time', 'sector1_time', 'sector2_time', 'sector3_time', 'sector4_time')
        
        if player_event_stats:
            image_of_track = player_event_stats[0]['event__image_of_track']
            event_name = player_event_stats[0]['event__title']

            context.update({
                'player_event_stats': player_event_stats,
                'image_of_track': image_of_track,
                'event_name': event_name,
                'status': True
            })
        
    return render(request, 'player/player-detail.html', context=context)


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
    
    paginator = Paginator(events, 15)
    page = request.GET.get('page')
    
    try:
        events_paginated = paginator.page(page)
    except PageNotAnInteger:
        events_paginated = paginator.page(1)
    except EmptyPage:
        events_paginated = paginator.page(paginator.num_pages)

    context = {
        'events': events_paginated,
        'years': years,
        'selected_year': year,
        'now': timezone.now()
    }
    return render(request, 'event/event-list.html', context=context)

def about_us(request):
    return render(request, 'info/about-us.html')

def karting_rules(request):
    return render(request, 'info/karting-rules.html')
