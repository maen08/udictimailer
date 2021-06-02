from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponse
from django.contrib import messages
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate, login
from django.conf.urls import url
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.template.loader import get_template




# SEND EMAIL ENDPOINT

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def sender_email_view(request):

    subject = request.data.get('email-subject')
    body = request.data.get('email-body')
    receiver_email = request.data.get('email-receiver') 
             


    template = get_template('email.html')
    content = template.render({'body':body})

    email = EmailMessage(
            subject,
            body=content,
            from_email='',
            to= receiver_email.split(','),  
            # settings.EMAIL_HOST_USER,
              # separate by comma
        )
    email.fail_silently = False
    email.content_subtype='html'
    email.send()

    
       
    data = {
        'message': 'Email sent!',
        'status': status.HTTP_200_OK,

    }
    return JsonResponse(data, status=status.HTTP_200_OK)
   






# REGISTER ENDPOINT
@csrf_exempt
@api_view(['POST'])
def register(request):
    email = request.POST.get('email')
    username = request.POST.get('username')
    password = request.POST.get('password')

    if User.objects.filter(username=username).exists():
        raise AuthenticationFailed(
            'Username has already taken, please choose another')

    user = User.objects.create_user(
        email=email, username=username, password=password
    )

    data = {
        'username': username,
        'message': 'Success registered, login to get the API Token',
        'status': status.HTTP_201_CREATED,
    }
    return JsonResponse(data, status=status.HTTP_201_CREATED)






# GET TEST ENDPOINT
@csrf_exempt
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_view(request):

    data = {
        'message': 'Official udictimailer'
    }

    return JsonResponse(data)






# LOGIN ENDPOINT

@api_view(['POST'])
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:

            this_user = User.objects.filter(username=username).first()

            if not this_user.check_password(password):
                raise AuthenticationFailed('Wrong password, please try again')

            elif this_user is None:
                raise AuthenticationFailed(
                    'User is not found, please register')

            else:
                user = authenticate(username=username, password=password)
                if user in User.objects.all():
                    if not user.check_password(password):
                        raise AuthenticationFailed('Wrong password!')

                login(request, user)
                user_token = str(Token.objects.create(user=user))


                args = {
                    'message': 'Successful login!',
                    'token': user_token,
                    'status':status.HTTP_200_OK,
                   
                }
                return JsonResponse(args, status=status.HTTP_200_OK)

        except AttributeError:
            raise AuthenticationFailed('User is not found, please register')

    else:
        args = {
            'message': 'You dont have an account, please register',
            'status':status.HTTP_403_FORBIDDEN,

        }
        raise JsonResponse(args, status=status.HTTP_403_FORBIDDEN)


