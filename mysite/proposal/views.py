from django.shortcuts import render
from django.urls import reverse

from django.views.generic.edit import CreateView
from extra_views import ModelFormSetView
from .models import customer, proposal, proposal_item


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


class ProposalItem(ModelFormSetView):
    model = proposal_item
    template_name = 'proposal/proposal_item.html'
    fields = ('product', 'product_type', 'product_finish', 'quantity', 'product_color', 'location', 'louver', 'panels', 'int_ext', 'trim', 'trim_type', 'tilt_rod', 'hinges', 'hinge_color', 'width', 'height', 'height_center', 'height_left', 'height_right', 'approved') #product_model
    queryset = proposal.objects.none()
    factory_kwargs={'extra': 10}

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.customer_id = self.kwargs['pk']
        self.object.save()
        form.save_m2m()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('proposal-item', kwargs={'pk': self.object.pk})
