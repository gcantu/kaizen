from django.urls import reverse
from django.shortcuts import render, redirect
from orders.models import proposal
import json


def Login(request):
    return redirect(reverse('login'))


def Home(request):
    p = proposal.objects.filter(status="Pending")

    return render(request, 'dashboard/home.html', {'proposals': p, 'status': 'Pending'})


def updateList(request, status):
    p = proposal.objects.filter(status=status)

    return render(request, 'dashboard/home.html', {'proposals': p, 'status': status})
