from django.urls import path
from . import views

app_name = 'proposal'

urlpatterns = [
    path('add_customer', views.addCustomer, name='add-customer'),
    path('add_proposal/<int:pk>', views.addProposal, name='add-proposal'),
    path('add_line_item/<int:pk>', views.addLineItem, name='add-line-item'),
    path('add_extra_line_item/<int:pk>', views.addExtraLineItem, name='add-extra-line-item'),
    path('final-proposal/<int:pk>', views.finalProposal, name='final-proposal'),
]
