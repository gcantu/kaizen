from django.urls import path
from .views import CreateCustomer
from . import views

app_name = 'proposal'

urlpatterns = [
    path('customer', CreateCustomer.as_view(), name='create-customer'),
    path('<int:pk>/new', views.CreateProposal, name='create-proposal'),
    path('<int:pk>/line_items', views.LineItem, name='create-line-item'),
    path('ajax/load-line-item', views.load_line_item, name='load-line-item'),
]
