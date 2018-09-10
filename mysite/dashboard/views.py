from django.shortcuts import render
from proposal.models import proposal


def Home(request):
    p_all = proposal.objects.all().count()
    p_pending = proposal.objects.filter(status="Pending").count()
    p_approved = proposal.objects.filter(status="Approved").count()

    return render(request, 'dashboard/home.html', {'p_all': p_all, 'p_pending': p_pending, 'p_approved': p_approved})

def pList(request, status):
    p_all = proposal.objects.all().count()
    p_pending = proposal.objects.filter(status="Pending").count()
    p_approved = proposal.objects.filter(status="Approved").count()

    if (status=="All"):
        p = proposal.objects.all()
    elif (status=="Approved"):
        p = proposal.objects.filter(status="Approved")
    elif (status=="Pending"):
        p = proposal.objects.filter(status="Pending")

    return render(request, 'dashboard/list_index.html', {'proposals': p, 'p_all': p_all, 'p_pending': p_pending, 'p_approved': p_approved})


def mReport(request):
    p = proposal.objects.all()

    return render(request, 'dashboard/home.html', {'proposals': p, 'pending': False})
