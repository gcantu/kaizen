from extra_views import InlineFormSet
from .models import proposal, proposal_item


class ProposalInline(InlineFormSet):
    model = proposal
    fields = "__all__"
    factory_kwargs={'extra': 1}


class ProposalItemInline(InlineFormSet):
    model = proposal_item
    fields = "__all__"
    factory_kwargs={'extra': 10}
