from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.Login, name='login-page'),
    path('home', views.Home, name='home'),
    path('ajax/load-letterhead/', views.load_letterhead, name='ajax_load_letterhead'),
]
