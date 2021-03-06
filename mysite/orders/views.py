from django.urls import reverse
from django.shortcuts import render, redirect
from .models import customer, proposal, agent, line_item
from .forms import customerForm, proposalForm, lineItemForm
from django.views.generic.edit import DeleteView


# CREATE FORMS ----------------------------------------------------------------
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


def addLineItem(request, pk):
    f = lineItemForm(initial={'proposal': pk})
    lineitem = line_item.objects.filter(proposal_id=pk)

    if request.method == 'POST':
        form = lineItemForm(request.POST)

        if form.is_valid():
            li = form.save(commit=False)

            if li.shutter_type_id == 4:
                li.panels = 1
                li.louver = 2.5

            if li.finish == 'Paint':
                li.stain = 'None'

            li.save()

            return redirect(reverse('orders:add-line-item', kwargs={'pk': pk}))

    return render(request, 'orders/content.html', {'form': f, 'lineitem': lineitem, 'proposal_id': pk, 'form_name': 'line_item', 'id': pk})


def addProposal(request, pk):
    p = proposal.objects.get(pk=pk)
    form = proposalForm(request.POST or None, instance=p)
    lineitem = line_item.objects.filter(proposal_id=pk)

    # calculate proposal total with/without tax
    subtotal = round(sum(i.totalPrice() for i in lineitem), 2)

    if form.is_valid():
        new_proposal = form.save(commit=False)
        new_proposal.order_subtotal = subtotal
        new_proposal.order_total = subtotal
        new_proposal.order_balance = subtotal
        new_proposal.save()
        form.save_m2m()
        return redirect(reverse('orders:order-summary', kwargs={'pk': pk}))

    return render(request, 'orders/content.html', {'form': form, 'lineitem': lineitem, 'proposal_id': pk, 'form_name': 'proposal'})


# EDIT FORMS ------------------------------------------------------------------
def editCustomer(request, pk):
    p = proposal.objects.get(customer_id=pk)
    data = customer.objects.get(pk=pk)
    form = customerForm(request.POST or None, instance=data)

    if form.is_valid():
        form.save()
        return redirect(reverse('orders:order-summary', kwargs={'pk': p.id}))

    return render(request, 'orders/content.html', {'form': form, 'form_name': 'customer', 'edit': True, 'id': pk})


def editProposal(request, pk):
    data = proposal.objects.get(pk=pk)
    form = proposalForm(request.POST or None, instance=data)

    if form.is_valid():
        form.save()
        return redirect(reverse('orders:order-summary', kwargs={'pk': pk}))

    return render(request, 'orders/content.html', {'form': form, 'form_name': 'proposal', 'edit': True, 'id': pk})


def editLineItem(request, pk):
    data = line_item.objects.get(pk=pk)
    form = lineItemForm(request.POST or None, instance=data)

    if form.is_valid():
        li = form.save(commit=False)

        if li.shutter_type_id == 4:
            li.panels = 1
            li.louver = 2.5

        if li.finish == 'Paint':
            li.stain = None

        li.save()

        return redirect(reverse('orders:order-summary', kwargs={'pk': data.proposal_id}))

    return render(request, 'orders/content.html', {'form': form, 'form_name': 'line_item', 'edit': True, 'id': data.proposal_id})


def editPrice(request, pk):
    p = proposal.objects.get(pk=pk)
    form = proposalForm(request.POST or None, instance=p)
    lineitem = line_item.objects.filter(proposal_id=pk)

    if form.is_valid():
        new_price = form.save(commit=False)
        if (new_price.add_tax):
            new_price.order_tax = round(new_price.order_subtotal*.0825, 2)
        else:
            new_price.order_tax = 0
        new_price.order_total = round(new_price.order_subtotal + new_price.order_tax,2)
        new_price.order_balance = round(new_price.order_total - new_price.order_down_payment,2)
        new_price.save()
        form.save_m2m()
        return redirect(reverse('orders:order-summary', kwargs={'pk': pk}))

    return render(request, 'orders/content.html', {'proposal': p, 'form': form, 'form_name': 'price', 'edit': True, 'id': pk})

# DELETE FORMS ------------------------------------------------------

# Line Item
class lineItemDelete(DeleteView):
    model = line_item
    template_name = 'orders/confirm_delete.html'

    def get_success_url(self):
        p_id = self.get_object().proposal_id
        return reverse('orders:order-summary', kwargs={'pk': p_id})

# Proposal
def confirm_status(request, pk, status):
    p = proposal.objects.get(pk=pk)

    return render(request, 'orders/confirm_status_update.html', {'p': p, 'status': status})


def update_status(request, pk, status):
    p = proposal.objects.get(pk=pk)

    p.status = status
    p.save()

    return redirect(reverse('dashboard:home'))



# ORDER SUMMARY --------------------------------------------------------------
def orderSummary(request, pk):
    p = proposal.objects.get(pk=pk)
    p_agents = p.agents.all()
    p_measuredby = p.measured_by.all()
    cust_id = p.customer_id
    cust = customer.objects.get(pk=cust_id)
    lineitem = line_item.objects.filter(proposal_id=pk)

    return render(request, 'orders/order_summary.html', {'customer': cust, 'proposal': p, 'agents': p_agents, 'measuredby': p_measuredby, 'lineitem': lineitem, 'report_name': 'order_summary'})
