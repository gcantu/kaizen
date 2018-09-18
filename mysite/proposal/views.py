from django.urls import reverse
from django.shortcuts import render, redirect
from .models import customer, proposal, agent, line_item
from .forms import customerForm, proposalForm, lineItemForm
from django.views.generic.edit import UpdateView
from django.db.models import Sum
from .forms import proposalLineItemFormSet


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
            return redirect(reverse('proposal:add-line-item', kwargs={'pk': p.id}))

    return render(request, 'proposal/form_customer.html', {'form': f})


# LINE ITEM
def addLineItem(request, pk):
    f = lineItemForm(initial={'proposal': pk})

    if request.method == 'POST':
        form = lineItemForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)

            t_w = item.width + item.width_fraction
            t_h = item.height + item.height_fraction
            sq_in = t_w * t_h
            sq_ft = sq_in/144

            total_price = item.price_per_sq_ft * sq_ft

            item.total_price = round(total_price)
            item.save()

            return redirect(reverse('proposal:line-item-options', kwargs={'pk': pk}))

    return render(request, 'proposal/form_line_item.html', {'form': f})


# PROPOSAL
def addProposal(request, pk):
    p = proposal.objects.get(pk=pk)
    form = proposalForm(request.POST or None, instance=p)

    if form.is_valid():
        form.save()
        return redirect(reverse('proposal:final-proposal', kwargs={'pk': pk}))

    return render(request, 'proposal/form_proposal.html', {'form': form})


# OPTION FOR CREATING ANOTHER LINE ITEM
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

    return render(request, 'proposal/final_proposal.html', {'customer': cust, 'proposal': p, 'agents': p_agents, 'measuredby': p_measuredby, 'lineitem': lineitem, 'subtotal': subtotal, 'tax': tax, 'total': total})



# APPROVE PROPOSAL
def approveProposal(request,pk):
    p = proposal.objects.get(pk=pk)
    p.status = 'Approved'
    p.save()

    return redirect(reverse('dashboard:home'))
