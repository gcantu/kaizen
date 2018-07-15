from django.urls import path
from .views import ManufacturingReport
from . import views

app_name = 'manufacturing'
urlpatterns = [
    # path('<int:pk>/report', ManufacturingReport.as_view(), name='manufacturing-report'),
    path('<int:pk>/report', views.ManufacturingReport, name='report'),
]
