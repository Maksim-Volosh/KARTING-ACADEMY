from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect

from KARTING_ACADEMY import settings


def send_email(request):
    if request.method == 'POST' and settings.PASS:
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
    messages.success(request, 
                     "The message was not sent successfully because you have to add the PASS variable to the settings!")
    return redirect('index')