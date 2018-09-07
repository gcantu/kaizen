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



from django.forms.models import inlineformset_factory

proposalLineItemFormSet = inlineformset_factory(
    proposal,
    line_item,
    fields=('product', 'shutter_type', 'finish', 'stain', 'color', 'location', 'mount', 'trim', 'trim_style', 'louver', 'hinges', 'hinge_color', 'panels', 't_post', 'tilt_rod', 'separate_parts', 'width', 'width_fraction', 'height', 'height_fraction', 'height_left', 'height_left_fraction', 'height_right', 'height_right_fraction', 'height_center',    'height_center_fraction', 'quantity', 'price', 'approved',),
    extra=0
)
