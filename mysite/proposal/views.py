from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import proposal_item

class ProposalCreate(CreateView):
    model = proposal_item
    template_name = 'proposal/proposal_form.html'
    fields = '__all__'
    exclude = ['Proposal']
