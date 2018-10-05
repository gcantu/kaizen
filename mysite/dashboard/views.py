from django.urls import reverse
from django.shortcuts import render, redirect
from orders.models import proposal
import json


def Login(request):
    return redirect(reverse('login'))


def Home(request):
    p = proposal.objects.exclude(status="Deleted")

    return render(request, 'dashboard/home.html', {'proposals': p})


def load_letterhead(request):
    with open("assets/company.json", "r") as read_file:
        data = json.load(read_file)
        company = data['company']

    return render(request, 'dashboard/letterhead.html', {'company': company})
