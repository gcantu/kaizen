from django.db import models
from datetime import date


class customer(models.Model):
    COUNTRY_CHOICES = [('MX', 'MX'), ('US', 'US')]
    name = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=2, choices=COUNTRY_CHOICES)
    zip_code = models.CharField(max_length=5, blank=True)
    home_phone = models.CharField(max_length=25, blank=True)
    mobile_phone = models.CharField(max_length=25, blank=True)
    email = models.EmailField(max_length=254, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'customer'


class agent(models.Model):
    name = models.CharField(max_length=255, unique=True)
    home_phone = models.CharField(max_length=25, blank=True)
    mobile_phone = models.CharField(max_length=25, blank=True)
    email = models.EmailField(max_length=254, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'agent'


class product(models.Model):
    product_name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = 'product'


class product_type(models.Model):
    product_type = models.CharField(max_length=100, unique=True)
    product = models.ForeignKey(product, models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.product_type

    class Meta:
        db_table = 'product_type'


class product_finish(models.Model):
    finish_type = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.finish_type

    class Meta:
        db_table = 'product_finish'


class product_model(models.Model):
    model_name = models.CharField(max_length=3, unique=True)
    model_description = models.TextField()
    product = models.ForeignKey(product, models.SET_NULL, blank=True, null=True)
    product_finish = models.ManyToManyField(product_finish, through='product_price')

    def __str__(self):
        return self.model_name

    class Meta:
        db_table = 'product_model'


class product_price(models.Model):
    product_model = models.ForeignKey(product_model, models.SET_NULL, blank=True, null=True)
    product_finish = models.ForeignKey(product_finish, models.SET_NULL, blank=True, null=True)
    price_per_sqft = models.IntegerField()

    def __str__(self):
        return self.product_price_id

    class Meta:
        db_table = 'product_price'


class proposal(models.Model):
    created_date = models.DateField(default=date.today)
    customer = models.ForeignKey(customer, models.SET_NULL, blank=True, null=True)
    agents = models.ManyToManyField(agent)
    measured_by = models.ManyToManyField(agent, related_name='proposal_measured_by')
    notes = models.TextField()

    def __str__(self):
        return self.proposal_id

    class Meta:
        db_table = 'proposal'


class proposal_item(models.Model):
    INT_EXT_CHOICES = [('Int', 'Interior'), ('Ext', 'Exterior')]
    TRIM_CHOICES = [(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')]
    TRIM_TYPE_CHOICES = [('Colonial', 'Colonial'), ('Flat', 'Flat'), ('Modern', 'Modern')]
    HINGE_CHOICES = [('LR', 'Left/Right'), ('L', 'Left'), ('R', 'Right')]
    LOUVER_CHOICES = [(2.5, '2 1/2'), (3.5, '3 1/2'), (4.5, '4 1/2')]
    TILT_ROD_CHOICES = [('Aluminum', 'Aluminum'), ('Front', 'Front'), ('Side and Back', 'Side and Back')]
    proposal = models.ForeignKey(proposal, models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(product, models.SET_NULL, blank=True, null=True)
    product_model = models.ForeignKey(product_model, models.SET_NULL, blank=True, null=True)
    product_type = models.ForeignKey(product_type, models.SET_NULL, blank=True, null=True)
    product_finish = models.ForeignKey(product_finish, models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(null=True)
    product_color = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    louver = models.IntegerField(choices=LOUVER_CHOICES, null=True)
    panels = models.IntegerField(null=True)
    int_ext = models.CharField(max_length=3, choices=INT_EXT_CHOICES, blank=True)
    trim = models.IntegerField(choices=TRIM_CHOICES, blank=True)
    trim_type = models.CharField(max_length=25, choices=TRIM_TYPE_CHOICES, blank=True)
    tilt_rod = models.CharField(max_length=25, choices=TILT_ROD_CHOICES, blank=True)
    hinges = models.CharField(max_length=2, choices=HINGE_CHOICES, blank=True)
    hinge_color = models.CharField(max_length=100, blank=True)
    width = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    height_center = models.IntegerField(null=True)
    height_left = models.IntegerField(null=True)
    height_right = models.IntegerField(null=True)
    approved = models.NullBooleanField()

    def __str__(self):
        return self.proposal_item_id

    def get_absolute_url(self):
        return reverse('proposal-detail', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'proposal_item'
