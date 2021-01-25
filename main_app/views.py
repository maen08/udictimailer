from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponse
from django.contrib import messages



def sender_view(request):
    try:
        email = EmailMessage(
            'Sent from Django App',
            'Nadhan imekubali',
            settings.EMAIL_HOST_USER,
            ['2001stany@gmail.com', 'fredy.masika@gmail.com'],
        )
        email.fail_silently = False
        email.send()
        messages.success(request, 'Email sent Successfully')
        print('EMAIL GOT SENT')

    except:
        print('NOT SENT')
  
    return render(request, template_name='create_email.html')


def create_email_view(request):
    return render(request, template_name='create_email.html')