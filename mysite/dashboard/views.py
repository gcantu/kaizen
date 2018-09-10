from django.shortcuts import render
from proposal.models import proposal


def Home(request):
    p = proposal.objects.all()

    return render(request, 'dashboard/home.html', {'proposals': p, 'pending': True})


def mReport(request):
    p = proposal.objects.all()

    return render(request, 'dashboard/home.html', {'proposals': p, 'pending': False})
