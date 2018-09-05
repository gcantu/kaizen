from django.forms import ModelForm
from .models import customer, proposal, line_item


# Customer form
class customerForm(ModelForm):
    class Meta:
        model = customer
        fields = '__all__'

# Proposal form
class proposalForm(ModelForm):
    class Meta:
        model = proposal
        fields = '__all__'

# Line Item form
class lineItemForm(ModelForm):
    class Meta:
        model = line_item
        fields = '__all__'
