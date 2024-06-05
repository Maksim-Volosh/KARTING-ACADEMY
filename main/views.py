from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse

from KARTING_ACADEMY import settings
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
