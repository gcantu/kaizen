from django.urls import reverse
from django.shortcuts import render, redirect
from .models import customer, proposal, agent, line_item
from .forms import customerForm, proposalForm, lineItemForm
from django.views.generic.edit import UpdateView
from django.db.models import Sum
from .forms import proposalLineItemFormSet


def addCustomer(request):
    f = customerForm()

    if request.method == 'POST':
        form = customerForm(request.POST)

        if form.is_valid():
            form.save()
            cust_id = form.instance.id
            return redirect(reverse('proposal:add-proposal', kwargs={'pk': cust_id}))

    return render(request, 'proposal/form_customer.html', {'form': f})



def addProposal(request, pk):
    f = proposalForm()

    if request.method == 'POST':
        form = proposalForm(request.POST)

        if form.is_valid():
            new_p = form.save(commit=False)
            new_p.customer_id = pk
            new_p.save()
            form.save_m2m()
            p_id = form.instance.id
            return redirect(reverse('proposal:add-line-item', kwargs={'pk': p_id}))

    return render(request, 'proposal/form_proposal.html', {'form': f})



def addLineItem(request, pk):
    p = proposal.objects.get(pk=pk)
    f = lineItemForm()

    if request.method == 'POST':
        form = lineItemForm(request.POST)

        if form.is_valid():
            new_li = form.save(commit=False)
            new_li.proposal_id = pk
            new_li.save()
            return redirect(reverse('proposal:line-item-options', kwargs={'pk': pk}))

    return render(request, 'proposal/form_line_item.html', {'form': f, 'proposal': p})



def lineItemOptions(request, pk):
    return render(request, 'proposal/line_item_options.html', {'p_id': pk})


# EDIT FORMS ------------------------------------------------------------------
def editCustomer(request, pk):
    p = proposal.objects.get(customer_id=pk)
    data = customer.objects.get(pk=pk)
    form = customerForm(request.POST or None, instance=data)

    if form.is_valid():
        form.save()
        return redirect(reverse('proposal:final-proposal', kwargs={'pk': p.id}))

    return render(request, 'proposal/form_customer.html', {'form': form})


def editProposal(request, pk):
    data = proposal.objects.get(pk=pk)
    form = proposalForm(request.POST or None, instance=data)

    if form.is_valid():
        form.save()
        return redirect(reverse('proposal:final-proposal', kwargs={'pk': pk}))

    return render(request, 'proposal/form_proposal.html', {'form': form})


def editLineItem(request, pk):
    data = proposal.objects.get(pk=pk)
    form = proposalLineItemFormSet(request.POST or None, instance=data)

    if form.is_valid():
        form.save()
        return redirect(reverse('proposal:final-proposal', kwargs={'pk': pk}))

    return render(request, 'proposal/form_line_item_edit.html', {'form': form})



def finalProposal(request, pk):
    p = proposal.objects.get(pk=pk)
    p_agents = p.agents.all()
    p_measuredby = p.measured_by.all()
    cust_id = p.customer_id
    cust = customer.objects.get(pk=cust_id)
    lineitem = line_item.objects.filter(proposal_id=pk)

    li_sum = lineitem.aggregate(Sum('price_per_sq_ft'))
    total = li_sum['price_per_sq_ft__sum']

    return render(request, 'proposal/final_proposal.html', {'customer': cust, 'proposal': p, 'agents': p_agents, 'measuredby': p_measuredby, 'lineitem': lineitem, 'total': total})






def approveProposal(request,pk):
    p = proposal.objects.get(pk=pk)
    p.status = 'Approved'
    p.save()

    return redirect(reverse('dashboard:home'))
