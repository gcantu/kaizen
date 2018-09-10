from django.urls import path
from . import views

app_name = 'proposal'

urlpatterns = [
    path('add_customer', views.addCustomer, name='add-customer'),
    path('add_proposal/<int:pk>', views.addProposal, name='add-proposal'),
    path('add_line_item/<int:pk>', views.addLineItem, name='add-line-item'),
    path('options/<int:pk>', views.lineItemOptions, name='line-item-options'),
    path('final-proposal/<int:pk>/<int:var>', views.finalProposal, name='final-proposal'),
    path('edit/<int:pk>/<int:var>', views.editForm, name='edit-form'),
]
