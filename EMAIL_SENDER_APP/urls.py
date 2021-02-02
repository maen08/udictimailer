
from django.contrib import admin
from django.urls import path, include
from main_app import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('', views.sender_view),
    path('get/', views.login_view),
    path('register/', views.register),
    path('test/', views.test_view),
    path('auth/', obtain_auth_token),    
    path('create/', views.create_email_view, name='create'),
]
