from extra_views import CreateWithInlinesView

from .models import customer
from .forms import ProposalInline, ProposalItemInline


class CreateProposalView(CreateWithInlinesView):
    model = customer
    inlines = [ProposalInline, ProposalItemInline]
    fields = "__all__"
    template_name = 'proposal/proposal_form.html'

    def get_success_url(self):
        return self.object.get_absolute_url()

# ---------------------------------------------------
# from django.views.generic.edit import CreateView
# from .forms import CustomerForm # , ProposalFormSet
# from extra_views import InlineFormSet, CreateWithInlinesView
# from extra_views.generic import GenericInlineFormSetFactory


# from extra_views import InlineFormSetView
#
# class ProposalCreate(InlineFormSetView):
#     model = customer
#     inline_model = proposal
#     fields="__all__"


# SI FUNCIONA ----------------------------
# from extra_views import ModelFormSetView
# from .models import customer
# from django.forms import formset_factory
#
# class ProposalCreate(ModelFormSetView):
#     template_name = 'proposal/proposal_form.html'
#     model = customer
#     factory_kwargs={'extra': 2}
#     fields="__all__"
# SI FUNCIONA ----------------------------


# class ProposalCreate(InlineFormSetView):
#     model = customer
#     inline_model = proposal

# class ProposalInline(InlineFormSet):
#     model = proposal
#     fields = '__all__'


# class TagInline(GenericInlineFormSetFactory):
#     model = Tag
#     fields = '__all__'


# class ProposalCreate(CreateWithInlinesView):
#     model = customer
#     inlines = [ProposalInline]
#     fields = '__all__'
#     template_name = 'proposal/proposal_form.html'

# class ProposalCreate(CreateView):
#     model = customer
#     form_class = CustomerForm
#     template_name = 'proposal/proposal_form.html'
#
#     def get(self, request, *args, **kwargs):
#         self.object = None
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         proposal_form = ProposalFormSet()
#         # proposal_item_form = ProposalItemFormSet()
#         return self.render_to_response(
#             self.get_context_data(form=form,
#                                   proposal_form=proposal_form))
#                                   # proposal_item_form=proposal_item_form))
#
#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         proposal_form = ProposalFormSet(self.request.POST)
#         # instruction_form = InstructionFormSet(self.request.POST)
#         if (form.is_valid() and proposal_form.is_valid()):
#             return self.form_valid(form, proposal_form) # , instruction_form)
#         else:
#             return self.form_invalid(form, proposal_form) # , instruction_form)
#
#     def form_valid(self, form, proposal_form): # , instruction_form):
#         self.object = form.save()
#         proposal_form.instance = self.object
#         proposal_form.save()
#         # instruction_form.instance = self.object
#         # instruction_form.save()
#         return HttpResponseRedirect(self.get_success_url())
#
#     def form_invalid(self, form, proposal_form): # , instruction_form):
#         return self.render_to_response(
#             self.get_context_data(form=form,
#                                   proposal_form=proposal_form))
#                                   # instruction_form=instruction_form))
