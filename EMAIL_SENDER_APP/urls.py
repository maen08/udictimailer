
from django.contrib import admin
from django.urls import path
from main_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send-email/', views.sender_view),
    path('', views.create_email_view, name='create')
]
