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







def sender_view(request):
    if request.method == 'POST':
        subject = request.POST.get('email-subject')
        body = request.POST.get('email-body')
        receiver = request.POST.get('email-receiver')
        
        # in future, store these details in DB

        email = EmailMessage(
            subject,
            body,
            settings.EMAIL_HOST_USER,
            receiver.split(),
        )
        email.fail_silently = False
        email.send()
        messages.success(request, 'Email sent Successfully')
        print('EMAIL GOT SENT')

    else:
        print('NOT SENT')
  
    return render(request, template_name='create_email.html')


def create_email_view(request):
    return render(request, template_name='create_email.html')






# works fine

@csrf_exempt
@api_view(['POST'])
def register(request):
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']


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






# works fine

# @csrf_exempt
# @api_view(['POST'])
# def signin(request):
#     username = request.POST['username']
#     password = request.POST['password']


#     if not User.objects.filter(username=username).exists():
#         raise AuthenticationFailed('Username does not exist, please register')
    
#     # try:
#     user = authenticate(request, username=username, password=password)
#     login(request, user)
#         # print('GOOD LOGGER')
#     token = str(Token.objects.get(user=user).key) 
#         # print(token)

#     # except Exception:
#     #     raise AuthenticationFailed('Authentication Failed!')        
 
#     data = {
#         'message': 'logged in',
#         'token': token,
#     }
#     return JsonResponse(data, status=status.HTTP_202_ACCEPTED)



# test for token auth

@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test_view(request):

    data = {
        'message': 'Official udictimailer'
    }

    return JsonResponse(data)



@api_view(['POST'])
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = authenticate(username=username, password=password)
            login(request, user)
            user_token = str(Token.objects.get().key)

            args = {
                'message': 'Successful login',
                'token':user_token
            }
            return JsonResponse(args, status=status.HTTP_201_CREATED)

        except AttributeError:
            raise AuthenticationFailed('You dont have an account, please register')

    else:
        args = {
            'message': 'You dont have an account, please register',
            
        }
        raise JsonResponse(args, status=status.HTTP_403_FORBIDDEN)


