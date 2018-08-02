
from django.forms import inlineformset_factory
from django.forms import ModelForm
from .models import proposal, customer, line_item, product_style


ProposalFormSet = inlineformset_factory(
    customer,
    proposal,
    fields=('created_date', 'agents', 'measured_by',),
    extra=1
    )


class CustomModelForm(ModelForm):
    class Meta:
        model = line_item
        fields = ('product', 'style', 'product_type', 'texture', 'finish', 'stain', 'color', 'location', 'mount', 'trim', 'trim_style', 'louver', 'hinges', 'hinge_color', 'panels', 't_post', 'tilt_rod', 'separate_parts', 'width', 'height', 'height_left', 'height_right', 'height_center', 'quantity', 'approved')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['style'].queryset = product_style.objects.none()

        if 'line_item_set-0-product' in self.data:
            try:
                product_id = int(self.data.get('line_item_set-0-product'))
                self.fields['style'].queryset = product_style.objects.filter(product_id=product_id).order_by('style')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty style queryset

        elif self.instance.pk:
            self.fields['style'].queryset = self.instance.product.style_set.order_by('style')


LineItemFormSet = inlineformset_factory(
    proposal,
    line_item,
    form=CustomModelForm,
    extra=1
    )
