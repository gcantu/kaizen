from django.shortcuts import render
from proposal.models import proposal


def Home(request):
    p = proposal.objects.filter(pending=0)

    return render(request, 'dashboard/home.html', {'proposals': p})
