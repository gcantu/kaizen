from django.urls import path
from .views import CreateProposalView

urlpatterns = [
    path('new', CreateProposalView.as_view(), name='proposal-new'),
]
