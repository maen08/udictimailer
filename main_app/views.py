from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponse
from django.contrib import messages
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate, login







# @csrf_exempt
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
def create_email_view(request):
    return render(request, template_name='create_email.html')




# works fine

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def sender_email_view(request):
    if request.method == 'POST':

        # parsing data
        subject = request.data.get('email-subject')
        body = request.data.get('email-body')
        receiver_email = request.POST.get('email-receiver')
        
        # in future, store these details in DB

        user = User.objects.filter(username=username).first()
        if user is None:
            raise AuthenticationFailed('User is not found, please register')

        # else:
        #     to_email = user.email

        #  continue with this

        to_email = user.email

        email = EmailMessage(
            subject,
            body,
            settings.EMAIL_HOST_USER,
            to_email,
            # receiver.split(),
        )
        email.fail_silently = False
        email.send()
        messages.success(request, 'Email sent Successfully')
        print('EMAIL GOT SENT')

    else:
        print('NOT SENT')
  
    return render(request, template_name='create_email.html')






# works fine

@csrf_exempt
@api_view(['POST'])
def register(request):
    email = request.data['email']
    username = request.data['username']
    password = request.data['password']


    if User.objects.filter(username=username).exists():
        raise AuthenticationFailed('Username has already taken, please choose another')

    user = User.objects.create_user(
        email=email,username=username,password=password
    )
    
    data = {
        'username': username,
        'message': 'success registered'
    }
    return JsonResponse(data, status=status.HTTP_201_CREATED)






# test for token auth

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def test_view(request):

    data = {
        'message': 'Official udictimailer'
    }

    return JsonResponse(data)





# up and running

@api_view(['POST'])
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        try:

            this_user = User.objects.filter(username=username).first()

            if not this_user.check_password(password):
                raise AuthenticationFailed('Wrong password, please try again')

            elif this_user is None:
                raise AuthenticationFailed('User is not found, please register')

            else:
                user = authenticate(username=username, password=password)
                if user in User.objects.all():
                    if not user.check_password(password):
                        raise AuthenticationFailed('Wrong password!')
                    
                    login(request, user)
                    user_token = str(Token.objects.create(user=user))

                    args = {
                        'message': 'Successful login',
                        'token':user_token
                    }
                    return JsonResponse(args, status=status.HTTP_201_CREATED)

        except AttributeError:
            raise AuthenticationFailed('User is not found, please register')

    else:
        args = {
            'message': 'You dont have an account, please register',
            
        }
        raise JsonResponse(args, status=status.HTTP_403_FORBIDDEN)




