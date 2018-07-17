
from django.forms import modelformset_factory
from .models import proposal_item

ProposalItemFormSet = modelformset_factory(
    proposal_item,
    fields=('product', 'product_type', 'product_finish', 'quantity', 'product_color', 'location', 'louver', 'panels', 'int_ext', 'trim', 'trim_type', 'tilt_rod', 'hinges', 'hinge_color', 'width', 'height', 'height_center', 'height_left', 'height_right', 'approved'), extra=2)
