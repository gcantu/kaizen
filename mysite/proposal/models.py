from django.db import models
from datetime import date
from django.urls import reverse


class customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=5, blank=True)
    home_phone = models.CharField(max_length=25, blank=True)
    mobile_phone = models.CharField(max_length=25, blank=True)
    email = models.EmailField(max_length=254, blank=True)

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()
        self.city = self.city.capitalize()
        return super(customer, self).save(*args, **kwargs)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('customer-detail', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'customer'


class agent(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('agent-detail', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'agent'


class product(models.Model):
    product_name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'product'


class product_style(models.Model):
    style = models.CharField(max_length=100, unique=True)
    product = models.ForeignKey(product, models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.style

    def get_absolute_url(self):
        return reverse('style-detail', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'product_style'


class product_type(models.Model):
    product_type = models.CharField(max_length=100, unique=True)
    product = models.ForeignKey(product, models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.product_type

    def get_absolute_url(self):
        return reverse('type-detail', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'product_type'


class proposal(models.Model):
    created_date = models.DateField(default=date.today)
    customer = models.ForeignKey(customer, models.SET_NULL, blank=True, null=True)
    agents = models.ManyToManyField(agent)
    measured_by = models.ManyToManyField(agent, related_name='proposal_measured_by')
    notes = models.TextField(blank=True)

    # def __str__(self):
    #     return f'Proposal ID: {self.id}.'

    def get_absolute_url(self):
        return reverse('proposal-detail', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'proposal'


class line_item(models.Model):
    TEXTURE_CHOICES = [('Smooth', 'Eco Wood (Smooth)'), ('Textured', 'Facade (Textured)')]
    FINISH_CHOICES = [('Paint', 'Paint'), ('Stain', 'Stain')]
    STAIN_CHOICES = [('Ash', 'Ash'), ('Basswood', 'Basswood'), ('Knotty Alder', 'Knotty Alder'), ('Maple', 'Maple'), ('Pine', 'Pine')]
    MOUNT_CHOICES = [('Int', 'Interior'), ('Ext', 'Exterior')]
    TRIM_CHOICES = [(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')]
    TRIM_STYLE_CHOICES = [('Deco', 'Decorative'), ('Square', 'Square (Smooth)'), ('Round', 'Round (Smooth)'), ('Z', 'Z (Primed)'), ('Other', 'Other')]
    LOUVER_CHOICES = [(2.5, '2 1/2'), (3.5, '3 1/2'), (4.5, '4 1/2')]
    HINGE_CHOICES = [('LR', 'Left/Right'), ('L', 'Left'), ('R', 'Right')]
    HINGE_COLOR_CHOICES = [('Bronze', 'Bronze'), ('Nickel', 'Nickel'), ('White', 'White'), ('Bright White', 'Bright-White'), ('Off White', 'Off-White'), ('No Hinges', 'No Hinges'), ('Other', 'Other')]
    TILT_ROD_CHOICES = [('Normal', 'Normal'), ('Side and Back', 'Side and Back'), ('Aluminum', 'Aluminum')]

    proposal = models.ForeignKey(proposal, models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(product, models.SET_NULL, blank=True, null=True)
    style = models.ForeignKey(product_style, models.SET_NULL, blank=True, null=True)
    product_type = models.ForeignKey(product_type, models.SET_NULL, blank=True, null=True)
    texture = models.CharField(max_length=10, choices=TEXTURE_CHOICES, blank=True, null=True)
    finish = models.CharField(max_length=5, choices=FINISH_CHOICES, blank=True, null=True)
    stain = models.CharField(max_length=15, choices=STAIN_CHOICES, blank=True, null=True)
    color = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    mount = models.CharField(max_length=3, choices=MOUNT_CHOICES, blank=True)
    trim = models.IntegerField(choices=TRIM_CHOICES, blank=True, null=True)
    trim_style = models.CharField(max_length=10, choices=TRIM_STYLE_CHOICES, blank=True)
    louver = models.FloatField(choices=LOUVER_CHOICES, blank=True, null=True)
    hinges = models.CharField(max_length=2, choices=HINGE_CHOICES, blank=True)
    hinge_color = models.CharField(max_length=15, choices=HINGE_COLOR_CHOICES, blank=True)
    panels = models.IntegerField(blank=True, null=True)
    t_post = models.IntegerField(blank=True, null=True)
    tilt_rod = models.CharField(max_length=15, choices=TILT_ROD_CHOICES, blank=True)
    separate_parts = models.NullBooleanField()
    width = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    height_left = models.FloatField(blank=True, null=True)
    height_right = models.FloatField(blank=True, null=True)
    height_center = models.FloatField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    approved = models.BooleanField(default=False)

    # def __str__(self):
    #     return f'Line item ID: {self.id}.'

    def get_absolute_url(self):
        return reverse('line-item-detail', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'line_item'
