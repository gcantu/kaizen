from django.urls import path
from .views import manufacturingReport, proposalReport
from . import views

app_name = 'reports'

urlpatterns = [
    path('<int:pk>/manufacturing-report', views.manufacturingReport, name='manufacturing-report'),
    path('<int:pk>/proposal-report', views.proposalReport, name='proposal-report'),
    path('<int:pk>/invoice-report', views.invoiceReport, name='invoice-report'),
]
