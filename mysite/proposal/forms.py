from extra_views import InlineFormSet
from .models import proposal


class ProposalInline(InlineFormSet):
    model = proposal
    fields = "__all__"
    factory_kwargs={'extra': 1}
