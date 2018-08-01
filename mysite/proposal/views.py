from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import customer, proposal, product_style
from .forms import ProposalFormSet, LineItemFormSet


# Customer form
class CreateCustomer(CreateView):
    model = customer
    fields = '__all__'
    template_name = 'proposal/create_customer.html'

    def get_success_url(self):
        return reverse('proposal:create-proposal', kwargs={'pk': self.object.pk})


# Proposal form
def CreateProposal(request, pk):
    cust = customer.objects.get(pk=pk)

    if request.method == "POST":
        formset = ProposalFormSet(request.POST, instance=cust)

        if formset.is_valid():
            formset.save()
            return redirect(reverse('proposal:create-line-item', kwargs={'pk': pk}))

    else:
        formset = ProposalFormSet(instance=cust)

    return render(request, 'proposal/create_proposal.html', {'formset': formset, 'customer': cust})


# Proposal line items form
def LineItem(request, pk):
    p = proposal.objects.get(customer_id=pk)
    cust = customer.objects.get(pk=pk)
    p_agents = p.agents.all()
    p_measuredby = p.measured_by.all()

    if request.method == 'POST':
        formset = LineItemFormSet(request.POST, instance=p)

        if formset.is_valid():
            formset.save()
            return redirect(reverse('manufacturing:report', kwargs={'pk': pk})) # manufacturing is the namespace

    else:
        formset = LineItemFormSet(instance=p)

    return render(request, 'proposal/create_line_item.html', {'formset': formset, 'customer': cust, 'proposal': p, 'agents': p_agents, 'measuredby': p_measuredby})


# return a list of product styles based on selected product
def load_styles(request):
    product_id = request.GET.get('product')
    styles = product_style.objects.filter(product_id=product_id).order_by('style')

    return render(request, 'proposal/product_styles_dropdown.html', {'styles': styles})
