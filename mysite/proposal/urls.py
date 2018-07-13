from django.urls import path
from .views import CustomerType, NewCustomer, ExistingCustomer, CreateProposal, ProposalItem 
from . import views

urlpatterns = [
    # path('new', CreateProposalView.as_view(), name='proposal-new'),
    path('customer_type', views.CustomerType, name='customer-type'),
    path('new_customer', NewCustomer.as_view(), name='customer-new'),
    path('existing_customer', views.ExistingCustomer, name='customer-existing'),
    path('<int:pk>/new', CreateProposal.as_view(), name='proposal-new'),
    path('<int:pk>/item', ProposalItem.as_view(), name='proposal-item'),
]
