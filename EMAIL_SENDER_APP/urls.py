
from django.contrib import admin
from django.urls import path
from main_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.sender_view),
    path('create/', views.create_email_view, name='create')
]
