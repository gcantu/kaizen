from django.db import models
from datetime import datetime
from django.urls import reverse


# FUNCTIONS
# -----------------------------------------------------------
def as_fraction(n):
    number = int(n)
    dec = round(n % 1, 4)

    if (dec == 0):
        return number
    else:
        ratio = dec.as_integer_ratio()
        frac = '{}/{}'.format(ratio[0], ratio[1])
        final = '{} {}'.format(number, frac)

        return final

def none_sum(*args):
    args = [a for a in args if not a is None]
    return sum(args) if args else 0

# TABLES
# -----------------------------------------------------------
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


class shutter_type(models.Model):
    shutter_type_name = models.CharField(max_length=100, unique=True)
    product = models.ForeignKey(product, models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.shutter_type_name

    def get_absolute_url(self):
        return reverse('shutter-type-detail', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'shutter_type'


class proposal(models.Model):
    FINISH_CHOICES = [('Paint', 'Paint'), ('Stain', 'Stain')]
    STAIN_CHOICES = [('Ash', 'Ash'), ('Basswood', 'Basswood'), ('Knotty Alder', 'Knotty Alder'), ('Maple', 'Maple'), ('Pine', 'Pine')]
    LOUVER_CHOICES = [(2.5, '2 1/2'), (3.5, '3 1/2'), (4.5, '4 1/2')]
    HINGE_COLOR_CHOICES = [('Bronze', 'Bronze'), ('Nickel', 'Nickel'), ('White', 'White'), ('Bright White', 'Bright-White'), ('Off White', 'Off-White'), ('No Hinges', 'No Hinges'), ('Other', 'Other')]
    TILT_ROD_CHOICES = [('Normal', 'Normal'), ('Side and Back', 'Side and Back'), ('Aluminum', 'Aluminum')]
    STATUS_CHOICES = [('Pending', 'Pending'), ('Approved', 'Approved')]
    created_date = models.DateTimeField(default=datetime.today)
    customer = models.ForeignKey(customer, models.SET_NULL, blank=True, null=True)
    agents = models.ManyToManyField(agent)
    measured_by = models.ManyToManyField(agent, related_name='proposal_measured_by')
    finish = models.CharField(max_length=5, choices=FINISH_CHOICES, blank=True, null=True)
    stain = models.CharField(max_length=15, choices=STAIN_CHOICES, blank=True, null=True)
    color = models.CharField(max_length=100, blank=True)
    louver = models.FloatField(choices=LOUVER_CHOICES, blank=True, null=True)
    hinge_color = models.CharField(max_length=15, choices=HINGE_COLOR_CHOICES, blank=True)
    tilt_rod = models.CharField(max_length=15, choices=TILT_ROD_CHOICES, blank=True)
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def get_absolute_url(self):
        return reverse('proposal-detail', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'proposal'


class line_item(models.Model):
    MOUNT_CHOICES = [('Int', 'Interior'), ('Ext', 'Exterior')]
    TRIM_CHOICES = [(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')]
    TRIM_STYLE_CHOICES = [('Deco', 'Decorative'), ('Square', 'Square (Smooth)'), ('Round', 'Round (Smooth)'), ('Z', 'Z (Primed)'), ('Other', 'Other')]
    FRACTION_CHOICES = [(0, ''), (.125, '1/8'), (.25, '1/4'), (.375, '3/8'), (.5, '1/2'), (.625, '5/8'), (.75, '3/4'), (.875, '7/8')]
    HINGE_CHOICES = [('LR', 'Left/Right'), ('L', 'Left'), ('R', 'Right')]

    proposal = models.ForeignKey(proposal, models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(product, models.SET_NULL, blank=True, null=True)
    shutter_type = models.ForeignKey(shutter_type, models.SET_NULL, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)
    mount = models.CharField(max_length=3, choices=MOUNT_CHOICES, blank=True)
    trim = models.IntegerField(choices=TRIM_CHOICES, blank=True, null=True)
    trim_style = models.CharField(max_length=10, choices=TRIM_STYLE_CHOICES, blank=True)
    panels = models.IntegerField(blank=True, null=True)
    hinges = models.CharField(max_length=2, choices=HINGE_CHOICES, blank=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    height_left = models.IntegerField(blank=True, null=True)
    height_right = models.IntegerField(blank=True, null=True)
    height_center = models.IntegerField(blank=True, null=True)
    width_fraction = models.FloatField(choices=FRACTION_CHOICES, default=0)
    height_fraction = models.FloatField(choices=FRACTION_CHOICES, default=0)
    height_left_fraction = models.FloatField(choices=FRACTION_CHOICES, default=0)
    height_right_fraction = models.FloatField(choices=FRACTION_CHOICES, default=0)
    height_center_fraction = models.FloatField(choices=FRACTION_CHOICES, default=0)
    height_door_knob = models.IntegerField(blank=True, null=True)
    height_door_knob_fraction = models.FloatField(choices=FRACTION_CHOICES, default=0)
    height_divider = models.IntegerField(blank=True, null=True)
    height_divider_fraction = models.FloatField(choices=FRACTION_CHOICES, default=0)
    price_per_sq_ft = models.FloatField(blank=True, null=True)


    def modHeight(self): # calculate height for shutter model #7: round (square+arch)
        if self.shutter_type_id == 3:
            h = self.height_center - (self.width / 2)
            return (h)
        else:
            h = self.height
            return (h)

    # L frame width and height
    # ------------------------------------------------------
    def LframeW(self): # L frame width
        width = self.width + self.width_fraction
        Lwidth = width - 0.375 # -3/8
        return round(Lwidth, 4)

    def LframeH(self): # L frame height
        height = none_sum(self.modHeight(), self.height_fraction)
        Lheight = (height - 0.25) if height > 0 else 0 # -1/4
        return round(Lheight, 4)

    # L frame height center, left and right
    # ------------------------------------------------------
    def LframeHC(self): # L frame height center
        height = none_sum(self.height_center, self.height_center_fraction)
        Lheight = (height - 0.25) if height > 0 else 0 # -1/4
        return round(Lheight, 4)

    def LframeHL(self): # L frame height left
        height = none_sum(self.height_left, self.height_left_fraction)
        Lheight = (height - 0.25) if height > 0 else 0 # -1/4
        return round(Lheight, 4)

    def LframeHR(self): # L frame height right
        height = none_sum(self.height_right, self.height_right_fraction)
        Lheight = (height - 0.25) if height > 0 else 0 # -1/4
        return round(Lheight, 4)

    # rail, louver, stile, tilt rod
    # ------------------------------------------------------
    def r(self): # rail
        panels = self.panels
        Lwidth = self.LframeW()

        if panels == 1:
            rail = Lwidth - 5.6875 # 5 11/16
        elif panels == 2:
            rail = ((Lwidth - 1.25) - 8.625) / 2
        else: # 4 panels
            rail = (((Lwidth / 2) - 1.75) - 8.625) / 2 # 1 1/4, 8 5/8
        return round(rail, 4)

    def l(self): # louver
        rail = self.r()
        louver = rail - 0.0625 # 1/16
        return round(louver, 4)

    def s(self): # stile
        Lheight = max(self.LframeH(), self.LframeHC())
        stile = Lheight - 1.75 # 1 3/4
        return round(stile, 4)

    def tr(self): # tilt rod
        stile = self.s()
        Trod = stile - 9.875 # 9 7/8
        return round(Trod, 4)

    def louverQty(self):
        panels = self.panels
        stile = self.s()

        if panels == 1:
            qty = (stile - 6) / 3
        elif panels == 2:
            qty = ((stile - 10) / 3) * 2
        else: # 4 panels
            qty = ((stile - 10) / 3) * 4

        num = qty % 2

        if num > 0: # if the number is not even, add 1
            louverQty = qty + 1
        else:
            louverQty = qty

        return round(louverQty)

    def railQty(self):
        panels = self.panels
        railQty = panels * 2
        return railQty

    def stileQty(self):
        panels = self.panels
        stileQty = panels * 2
        return stileQty

    # calculate material needed
    # ------------------------------------------------------
    def totalHinges(self):
        Lheight = self.LframeH()
        panels = self.panels

        if Lheight < 60:
            hinges = panels * 2
        elif Lheight < 85:
            hinges = panels * 3
        else: # < 100
            hinges = panels * 4
        return hinges

    def magnets(self):
        panels = self.panels
        magnets = panels
        return magnets

    def screws(self):
        hinges = self.totalHinges()
        screws = hinges * 6
        return screws

    def LframeMaterial(self):
        Lwidth = self.LframeW()
        Lheight = self.LframeH()
        material = ((Lwidth + Lheight) / 12) * 2
        return round(material, 4)

    def louverMaterial(self):
        louver = self.l()
        louverQty = self.louverQty()
        material = (louver / 12) * louverQty
        return round(material, 4)

    def railMaterial(self):
        rail = self.r()
        railQty = self.railQty()
        material = (rail / 12) * railQty
        return round(material, 4)

    def stileMaterial(self):
        stile = self.s()
        stileQty = self.stileQty()
        material = (stile / 12) * stileQty
        return round(material, 4)

    def tiltRodMaterial(self):
        Lwidth = self.LframeW()
        Lheight = self.LframeH()
        material = (Lwidth / 12) * (Lheight / 12)
        return round(material, 4)

    def panelMaterial(self):
        panels = self.panels
        Lheight = self.LframeH()
        material = (Lheight / 12) * panels
        return round(material, 4)

    # formatted fractions for display
    # ------------------------------------------------------
    def LframeWidth(self):
        prev = self.LframeW()
        new = as_fraction(prev)
        return new

    def LframeHeight(self):
        prev = self.LframeH()
        new = as_fraction(prev)
        return new if prev > 0 else None

    def LframeHeightCenter(self):
        prev = self.LframeHC()
        new = as_fraction(prev)
        return new if prev > 0 else None

    def LframeHeightLeft(self):
        prev = self.LframeHL()
        new = as_fraction(prev)
        return new if prev > 0 else None

    def LframeHeightRight(self):
        prev = self.LframeHR()
        new = as_fraction(prev)
        return new if prev > 0 else None

    def rail(self):
        prev = self.r()
        new = as_fraction(prev)
        return new

    def louver(self):
        prev = self.l()
        new = as_fraction(prev)
        return new

    def stile(self):
        prev = self.s()
        new = as_fraction(prev)
        return new

    def tiltRod(self):
        prev = self.tr()
        new = as_fraction(prev)
        return new

    # calculate total price
    # ------------------------------------------------------
    def totalPrice(self):
        t_w = self.width + self.width_fraction
        t_h = none_sum(self.height, self.height_fraction)
        t_h_c = none_sum(self.height_center, self.height_center_fraction)

        max_h = max(t_h, t_h_c)

        sq_in = t_w * max_h
        sq_ft = sq_in/144

        total_price = self.price_per_sq_ft * sq_ft
        return round(total_price)

    def get_absolute_url(self):
        return reverse('line-item-detail', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'line_item'
