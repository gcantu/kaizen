from django.urls import path
from .views import ProposalCreate

urlpatterns = [
    path('new', ProposalCreate.as_view(), name='proposal-new'),
]
