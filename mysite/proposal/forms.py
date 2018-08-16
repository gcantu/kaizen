
from django.forms import inlineformset_factory
from .models import proposal, customer, line_item


ProposalFormSet = inlineformset_factory(
    customer,
    proposal,
    fields=('created_date', 'agents', 'measured_by',),
    extra=1
    )

LineItemFormSet = inlineformset_factory(
    proposal,
    line_item,
    fields = ('product', 'style', 'product_type', 'texture', 'finish', 'stain', 'color', 'location', 'mount', 'trim', 'trim_style', 'louver', 'hinges', 'hinge_color', 'panels', 't_post', 'tilt_rod', 'separate_parts', 'width', 'height', 'height_left', 'height_right', 'height_center', 'quantity', 'approved'),
    extra=1
    )
