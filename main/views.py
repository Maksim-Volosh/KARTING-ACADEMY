from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.contrib import messages

from KARTING_ACADEMY import settings
from main.models import Category, Event, Statistics

def index(request):
    event = Event.last_event(Event)
    if Category.objects.count() > 0:
        statistic = Statistics.objects.filter(event=event, category=1).select_related('player').values(
            'player__name', 'player__nationality', 'lap_time', 'points'
        )
    else:
        statistic = Statistics.objects.filter(event=event).select_related('player').values(
            'player__name', 'player__nationality', 'lap_time', 'points'
        )
    context = {
        'event': event,
        'statistic': statistic
    }
    return render(request, 'main/index.html', context=context)

def send_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        
        send_mail(
            'CARTING ACADEMY',  # Тема письма
            f"Вам пришло сообщение - {message} \n\nВот его контактная информация - {email}",  # Тело письма
            email,
            [settings.DEFAULT_FROM_EMAIL], 
            fail_silently=False,
        )
        messages.success(request, "Message sent successfully!")
        return redirect('index')
    return redirect('index')


# def event_detail(request, pk):
#     event = get_object_or_404(Event, pk=pk)
    
#     cat_name = request.GET.get('cat')
    
#     if cat_name:
#         category = get_object_or_404(Category, name__iexact=cat_name)
#         statistics = Statistics.objects.filter(event=event, category=category).select_related('player') 
#     else:
#         statistics = Statistics.objects.filter(event=event).select_related('player') 
    
#     player_stats = {}
#     for stat in statistics:
#         player = stat.player
#         if player not in player_stats:
#             player_stats[player] = []
#         player_stats[player].append(stat)

#     context = {
#         'event': event,
#         'player_stats': player_stats,
#     }
    
#     return render(request, 'main/event_detail.html', context=context)

    
