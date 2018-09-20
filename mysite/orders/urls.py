from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('add_customer', views.addCustomer, name='add-customer'),
    path('add_proposal/<int:pk>', views.addProposal, name='add-proposal'),
    path('add_line_item/<int:pk>', views.addLineItem, name='add-line-item'),
    path('edit-customer/<int:pk>', views.editCustomer, name='edit-customer'),
    path('edit-proposal/<int:pk>', views.editProposal, name='edit-proposal'),
    path('edit-line-item/<int:pk>', views.editLineItem, name='edit-line-item'),
    path('order-summary/<int:pk>', views.orderSummary, name='order-summary'),
]