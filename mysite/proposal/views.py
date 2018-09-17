from django.urls import reverse
from django.shortcuts import render, redirect
from .models import customer, proposal, agent, line_item
from .forms import customerForm, proposalForm, lineItemForm
from django.views.generic.edit import UpdateView
from django.db.models import Sum
from .forms import proposalLineItemFormSet


def addCustomer(request):
    f = customerForm()
    c = 'Customer'

    if request.method == 'POST':
        form = customerForm(request.POST)

        if form.is_valid():
            form.save()
            cust_id = form.instance.id
            return redirect(reverse('proposal:add-proposal', kwargs={'pk': cust_id}))

    return render(request, 'proposal/create.html', {'form': f, 'current': c})



def addProposal(request, pk):
    f = proposalForm()
    c = 'Proposal'

    if request.method == 'POST':
        form = proposalForm(request.POST)

        if form.is_valid():
            new_p = form.save(commit=False)
            new_p.customer_id = pk
            new_p.save()
            form.save_m2m()
            p_id = form.instance.id
            return redirect(reverse('proposal:add-line-item', kwargs={'pk': p_id}))

    return render(request, 'proposal/create.html', {'form': f, 'current': c})



def addLineItem(request, pk):
    p = proposal.objects.get(pk=pk)
    f = lineItemForm()
    c = 'Line Item'

    if request.method == 'POST':
        form = lineItemForm(request.POST)

        if form.is_valid():
            new_li = form.save(commit=False)
            new_li.proposal_id = pk
            new_li.save()
            return redirect(reverse('proposal:line-item-options', kwargs={'pk': pk}))

    return render(request, 'proposal/create.html', {'form': f, 'current': c, 'proposal': p})



def lineItemOptions(request, pk):
    return render(request, 'proposal/line_item_options.html', {'p_id': pk})



def finalProposal(request, pk, var):
    p = proposal.objects.get(pk=pk)
    p_agents = p.agents.all()
    p_measuredby = p.measured_by.all()
    cust_id = p.customer_id
    cust = customer.objects.get(pk=cust_id)
    lineitem = line_item.objects.filter(proposal_id=pk)

    li_sum = lineitem.aggregate(Sum('price_per_sq_ft'))
    total = li_sum['price_per_sq_ft__sum']

    form = proposalForm(request.POST or None, instance=p)

    if form.is_valid():
        form.save()

    if (var == 1):
        return render(request, 'proposal/final_proposal.html', {'customer': cust, 'proposal': p, 'agents': p_agents, 'measuredby': p_measuredby, 'lineitem': lineitem, 'total': total, 'form': form, 'var': var})

    else:
        return render(request, 'proposal/final_proposal.html', {'customer': cust, 'proposal': p, 'agents': p_agents, 'measuredby': p_measuredby, 'lineitem': lineitem, 'total': total, 'var': var})



def editForm(request, pk, var):
    p = proposal.objects.get(pk=pk)
    cust_id = p.customer_id

    if (var == 1):
        data = customer.objects.get(pk=cust_id)
        form = customerForm(request.POST or None, instance=data)
        c = 'Customer'
    elif (var == 2):
        data = proposal.objects.get(pk=pk)
        form = proposalForm(request.POST or None, instance=data)
        c = 'Proposal'
    elif (var == 3):
          data = proposal.objects.get(pk=pk)
          form = proposalLineItemFormSet(request.POST or None, instance=data)
          c = 'Line Item Edit'

    if form.is_valid():
        form.save()
        return redirect(reverse('proposal:final-proposal', kwargs={'pk': pk, 'var': 2}))

    return render(request, 'proposal/create.html', {'form': form, 'current': c})


def approveProposal(request,pk):
    p = proposal.objects.get(pk=pk)
    p.status = 'Approved'
    p.save()

    return redirect(reverse('dashboard:home'))
