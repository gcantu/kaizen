from django.urls import reverse
from django.shortcuts import render, redirect
from .models import customer, proposal, agent, line_item
from .forms import customerForm, proposalForm, lineItemForm


def addCustomer(request):
    cust = customerForm()

    if request.method == 'POST':
        form = customerForm(request.POST)

        if form.is_valid():
            form.save()
            cust_id = form.instance.id
            return redirect(reverse('proposal:add-proposal', kwargs={'pk': cust_id}))

    return render(request, 'proposal/customer_form.html', {'form': cust})



def addProposal(request, pk):
    cust = customer.objects.get(pk=pk)
    p = proposalForm()

    if request.method == 'POST':
        form = proposalForm(request.POST)

        if form.is_valid():
            new_p = form.save(commit=False)
            new_p.customer_id = pk
            new_p.save()
            form.save_m2m()
            p_id = form.instance.id
            return redirect(reverse('proposal:add-line-item', kwargs={'pk': p_id}))

    return render(request, 'proposal/proposal_form.html', {'form': p, 'customer': cust})



def addLineItem(request, pk):
    p = proposal.objects.get(pk=pk)
    p_agents = p.agents.all()
    p_measuredby = p.measured_by.all()
    cust_id = p.customer_id
    cust = customer.objects.get(pk=cust_id)
    li = lineItemForm()

    if request.method == 'POST':
        form = lineItemForm(request.POST)

        if form.is_valid():
            new_li = form.save(commit=False)
            new_li.proposal_id = pk
            new_li.save()
            # p_id = form.instance.id
            return redirect(reverse('proposal:add-extra-line-item', kwargs={'pk': pk}))

    return render(request, 'proposal/line_item_form.html', {'form': li, 'customer': cust, 'proposal': p, 'agents': p_agents, 'measuredby': p_measuredby})



def addExtraLineItem(request, pk):
    p = proposal.objects.get(pk=pk)
    p_agents = p.agents.all()
    p_measuredby = p.measured_by.all()
    cust_id = p.customer_id
    cust = customer.objects.get(pk=cust_id)
    lineitem = line_item.objects.filter(proposal_id=pk)
    li = lineItemForm()

    if request.method == 'POST':
        form = lineItemForm(request.POST)

        if form.is_valid():
            new_li = form.save(commit=False)
            new_li.proposal_id = pk
            new_li.save()
            # p_id = form.instance.id
            return redirect(reverse('proposal:add-extra-line-item', kwargs={'pk': pk}))

    return render(request, 'proposal/extra_line_item_form.html', {'form': li, 'customer': cust, 'proposal': p, 'agents': p_agents, 'measuredby': p_measuredby, 'lineitem': lineitem})



def finalProposal(request, pk):
    p = proposal.objects.get(pk=pk)
    p_agents = p.agents.all()
    p_measuredby = p.measured_by.all()
    cust_id = p.customer_id
    cust = customer.objects.get(pk=cust_id)
    lineitem = line_item.objects.filter(proposal_id=pk)

    return render(request, 'proposal/final_proposal.html', {'customer': cust, 'proposal': p, 'agents': p_agents, 'measuredby': p_measuredby, 'lineitem': lineitem})
