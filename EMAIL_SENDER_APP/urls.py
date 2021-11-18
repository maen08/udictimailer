
from django.contrib import admin
from django.urls import path, include
from main_app import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token
from des import urls as des_urls
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', include('rest_framework.urls')),
    path('send/', views.sender_email_view, name='send-email'),
    path('login/', views.login_view, name='login-view'),
    path('register/', views.register, name='register-view'),
    path('', views.test_view),

    url(r'^django-des/', include(des_urls)),

    # path('create/', views.create_email_view, name='create-view'),
   
   



    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
      
]



# path('auth/', obtain_auth_token),  