import select
from django.utils import timezone

from services.services import obj_all, select_related_decorator
from .models import Statistics
  
def get_last_event(model):
    return obj_all(
                model=model,
                filter={'date_of_start__lte': timezone.now()},
                order_by=("-date_of_start",),
                only=('date_of_start', 'title'),
                first=True,
            )

def get_next_event(event):
   return obj_all(
                model=event,
                filter={'date_of_start__gt': timezone.now()},
                order_by=("date_of_start",),
                only=('title', 'date_of_start', 'logo'),
                first=True,
            )

def all_stats(statistics, event):
    return obj_all(
                model=statistics,
                filter={'event': event},
                select_related=('player',),
                values=('player__name', 'player__nationality', 'lap_time', 'points'),
            )[:3]
    
def junior_stats(statistics, event):
    return obj_all(
                model=statistics,
                filter={'event': event, 'category': 2},
                select_related=('player',),
                values=('player__name', 'player__nationality', 'lap_time', 'points'),
            )[:3]

def event_detail_stats(statistics, event):
    return obj_all(
                model=statistics,
                filter={'event': event, 'category': 2},
                select_related=('player', 'category'),
                order_by=('-points',),
            )
    
def category_event_detail_stats(statistics, event, cat_name):
    return obj_all(
                model=statistics,
                filter={'event': event, 'category__name__iexact': cat_name},
                select_related=('player', 'category'),
                order_by=('-points',),
            )

def player_events_all(player):
    return player.events.all()

def get_years_of_events(event):
    events = obj_all(event)
    return list(set([event.date_of_start.year for event in events]))

def get_events_list(model):
    return obj_all(
        model=model,
        order_by=('-date_of_start',),
    )

def get_events_by_year(model, year):
    return obj_all(
        model=model,
        filter={'date_of_start__year': year},
        order_by=('-date_of_start',),
    )