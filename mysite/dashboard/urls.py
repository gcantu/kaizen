from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('home', views.Home, name='home'),
]
