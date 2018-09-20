from django.urls import reverse
from django.shortcuts import render, redirect
from .models import customer, proposal, agent, line_item
from .forms import customerForm, proposalForm, lineItemForm
from django.views.generic.edit import UpdateView
from django.db.models import Sum


# CREATE FORMS ----------------------------------------------------------------
# CUSTOMER
def addCustomer(request):
    f = customerForm()

    if request.method == 'POST':
        form = customerForm(request.POST)

        if form.is_valid():
            form.save()
            p = proposal.objects.create(customer_id=form.instance.id)
            p.save()
            return redirect(reverse('orders:add-line-item', kwargs={'pk': p.id}))

    return render(request, 'orders/content.html', {'form': f, 'form_name': 'customer'})


# LINE ITEM
def addLineItem(request, pk):
    f = lineItemForm(initial={'proposal': pk})
    lineitem = line_item.objects.filter(proposal_id=pk)

    if request.method == 'POST':
        form = lineItemForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('orders:add-line-item', kwargs={'pk': pk}))

    return render(request, 'orders/content.html', {'form': f, 'lineitem': lineitem, 'proposal_id': pk, 'form_name': 'line_item'})


# PROPOSAL
def addProposal(request, pk):
    p = proposal.objects.get(pk=pk)
    form = proposalForm(request.POST or None, instance=p)
    lineitem = line_item.objects.filter(proposal_id=pk)

    if form.is_valid():
        form.save()
        return redirect(reverse('orders:order-summary', kwargs={'pk': pk}))

    return render(request, 'orders/content.html', {'form': form, 'lineitem': lineitem, 'proposal_id': pk, 'form_name': 'proposal'})


# ORDER SUMMARY
def orderSummary(request, pk):
    p = proposal.objects.get(pk=pk)
    p_agents = p.agents.all()
    p_measuredby = p.measured_by.all()
    cust_id = p.customer_id
    cust = customer.objects.get(pk=cust_id)
    lineitem = line_item.objects.filter(proposal_id=pk)

    li_sum = lineitem.aggregate(Sum('price_per_sq_ft'))
    subtotal = li_sum['price_per_sq_ft__sum']
    tax = round(subtotal*.0825, 2)
    total = subtotal+tax

    return render(request, 'orders/order_summary.html', {'customer': cust, 'proposal': p, 'agents': p_agents, 'measuredby': p_measuredby, 'lineitem': lineitem, 'subtotal': subtotal, 'tax': tax, 'total': total})


# EDIT FORMS ------------------------------------------------------------------
def editCustomer(request, pk):
    p = proposal.objects.get(customer_id=pk)
    data = customer.objects.get(pk=pk)
    form = customerForm(request.POST or None, instance=data)

    if form.is_valid():
        form.save()
        return redirect(reverse('orders:order-summary', kwargs={'pk': p.id}))

    return render(request, 'orders/content.html', {'form': form, 'form_name': 'customer'})


def editProposal(request, pk):
    data = proposal.objects.get(pk=pk)
    form = proposalForm(request.POST or None, instance=data)
    lineitem = line_item.objects.filter(proposal_id=pk)

    if form.is_valid():
        form.save()
        return redirect(reverse('orders:order-summary', kwargs={'pk': pk}))

    return render(request, 'orders/content.html', {'form': form, 'lineitem': lineitem, 'form_name': 'proposal'})



def editLineItem(request, pk):
    data = line_item.objects.get(pk=pk)
    form = lineItemForm(request.POST or None, instance=data)

    if form.is_valid():
        form.save()
        return redirect(reverse('orders:order-summary', kwargs={'pk': data.proposal_id}))

    return render(request, 'orders/content.html', {'form': form, 'form_name': 'line_item_edit'})


# FINAL PROPOSAL --------------------------------------------------------------
def finalProposal(request, pk):
    p = proposal.objects.get(pk=pk)
    p_agents = p.agents.all()
    p_measuredby = p.measured_by.all()
    cust_id = p.customer_id
    cust = customer.objects.get(pk=cust_id)
    lineitem = line_item.objects.filter(proposal_id=pk)

    li_sum = lineitem.aggregate(Sum('total_price'))
    subtotal = li_sum['total_price__sum']
    tax = round(subtotal*.0825, 2)
    total = subtotal+tax

    return render(request, 'orders/final_proposal.html', {'customer': cust, 'proposal': p, 'agents': p_agents, 'measuredby': p_measuredby, 'lineitem': lineitem, 'subtotal': subtotal, 'tax': tax, 'total': total})



# APPROVE PROPOSAL
def approveProposal(request,pk):
    p = proposal.objects.get(pk=pk)
    p.status = 'Approved'
    p.save()

    return redirect(reverse('dashboard:home'))
