from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.Login, name='login-page'),
    path('home', views.Home, name='home'),
]
