from django.shortcuts import render
from proposal.models import proposal


def Home(request):
    p_all = proposal.objects.all().count()
    p_pending = proposal.objects.filter(status="Pending").count()
    p_approved = proposal.objects.filter(status="Approved").count()

    t = 'home'

    return render(request, 'dashboard/home.html', {'p_all': p_all, 'p_pending': p_pending, 'p_approved': p_approved, 'type': t})

def pList(request, status, type):
    p_all = proposal.objects.all().count()
    p_pending = proposal.objects.filter(status="Pending").count()
    p_approved = proposal.objects.filter(status="Approved").count()

    if (status=="All"):
        p = proposal.objects.all()
    elif (status=="Approved"):
        p = proposal.objects.filter(status="Approved")
    elif (status=="Pending"):
        p = proposal.objects.filter(status="Pending")

    return render(request, 'dashboard/list_index.html', {'proposals': p, 'p_all': p_all, 'p_pending': p_pending, 'p_approved': p_approved, 'type': type})


def mReport(request):
    p = proposal.objects.all()

    p_all = proposal.objects.all().count()
    p_pending = proposal.objects.filter(status="Pending").count()
    p_approved = proposal.objects.filter(status="Approved").count()

    t = 'report'

    return render(request, 'dashboard/home.html', {'p_all': p_all, 'p_pending': p_pending, 'p_approved': p_approved, 'type': t})
