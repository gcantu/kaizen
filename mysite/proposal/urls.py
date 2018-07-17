from django.urls import path
from .views import NewCustomer, CreateProposal, ProposalItem
from . import views

urlpatterns = [
    path('customer_type', views.CustomerType, name='customer-type'),
    path('new_customer', NewCustomer.as_view(), name='customer-new'),
    path('existing_customer', views.ExistingCustomer, name='customer-existing'),
    path('<int:pk>/new', CreateProposal.as_view(), name='proposal-new'),
    path('<int:pk>/item', views.ProposalItem, name='proposal-item'),
]
