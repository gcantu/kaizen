from django.urls import reverse
from django.shortcuts import render, redirect
from proposal.models import proposal


def Login(request):
    return redirect(reverse('login'))


def Home(request):
    p = proposal.objects.all()
    return render(request, 'dashboard/home.html', {'proposals': p})
