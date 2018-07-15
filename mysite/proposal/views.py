from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView

from .models import customer, proposal, proposal_item
from .forms import ProposalItemFormSet


def CustomerType(request):
    return render(request, 'proposal/customer_type.html')


def ExistingCustomer(request):
    return render(request, 'proposal/existing_customer.html')


class NewCustomer(CreateView):
    model = customer
    fields = '__all__'
    template_name = 'proposal/new_customer_form.html'

    def get_success_url(self):
        return reverse('proposal-new', kwargs={'pk': self.object.pk})


class CreateProposal(CreateView):
    model = proposal
    template_name = 'proposal/proposal_form.html'
    fields = ('created_date', 'notes', 'agents', 'measured_by')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.customer_id = self.kwargs['pk']
        self.object.save()
        form.save_m2m()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('proposal-item', kwargs={'pk': self.object.pk})


def ProposalItem(request, pk):
    if request.method == 'POST':
        formset = ProposalItemFormSet(
            request.POST,
            queryset=proposal_item.objects.none(),
        )

        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.proposal_id = pk
                instance.save()
            formset.save_m2m()
            return redirect(reverse('manufacturing:report', kwargs={'pk': pk})) # manufacturing is the namespace
    else:
        formset = ProposalItemFormSet(queryset=proposal_item.objects.none())

    return render(request, 'proposal/proposal_item.html', {'formset': formset})
