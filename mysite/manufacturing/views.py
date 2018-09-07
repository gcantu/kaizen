from django.shortcuts import render
from proposal.models import line_item, proposal, customer


class Shutter:
    def __init__(self, **kwargs):
        if 'width' in kwargs: self._width = kwargs['width']
        if 'height' in kwargs: self._height = kwargs['height']
        if 'width_fraction' in kwargs: self._width_fraction = kwargs['width_fraction']
        if 'height_fraction' in kwargs: self._height_fraction = kwargs['height_fraction']
        if 'panels' in kwargs: self._panels = kwargs['panels']
        if 'trim' in kwargs: self._trim = kwargs['trim']
        if 'prod_type' in kwargs: self._prod_type = kwargs['prod_type']
        if 'location' in kwargs: self._location = kwargs['location']

    def width(self):
        return self._width
		# if w: self._width = w
		# try: return self._width
		# except AttributeError: return None

    def height(self):
        return self._height

    def width_fraction(self):
        return self._width_fraction

    def height_fraction(self):
        return self._height_fraction

    def panels(self):
        return self._panels

    def trim(self):
        return self._trim

    def prod_type(self):
        return self._prod_type

    def location(self):
        return self._location

    def totalWidth(self):
        width = self.width()
        width_f = self.width_fraction()
        total = width + width_f
        return(total)

    def totalHeight(self):
        height = self.height()
        height_f = self.height_fraction()
        total = height + height_f
        return(total)

    def LframeWidth(self):
        width = self.totalWidth()
        Lwidth = width - 0.375 # -3/8
        return round(Lwidth, 3)

    def LframeHeight(self):
        height = self.totalHeight()
        Lheight = height - 0.25 # -1/4
        return round(Lheight, 3)

    def rail(self):
        panels = self.panels()
        Lwidth = self.LframeWidth()

        if panels == 1:
            rail = Lwidth - 5.6875 # 5 11/16
        elif panels == 2:
            rail = ((Lwidth - 1.25) - 8.625) / 2
        else: # 4 panels
            rail = (((Lwidth / 2) - 1.75) - 8.625) / 2 # 1 1/4, 8 5/8
        return round(rail, 3)

    def louver(self):
        rail = self.rail()
        louver = rail - 0.0625 # 1/16
        return round(louver, 3)

    def stile(self):
        Lheight = self.LframeHeight()
        stile = Lheight - 1.75 # 1 3/4
        return round(stile, 3)

    def tiltRod(self):
        stile = self.stile()
        Trod = stile - 9.875 # 9 7/8
        return round(Trod, 3)

    def hinges(self):
        Lheight = self.LframeHeight()
        panels = self.panels()

        if Lheight < 60:
            hinges = panels * 2
        elif Lheight < 85:
            hinges = panels * 3
        else: # < 100
            hinges = panels * 4
        return hinges

    def magnets(self):
        panels = self.panels()
        magnets = panels
        return magnets

    def screws(self):
        hinges = self.hinges()
        screws = hinges * 6
        return screws

    def louverQty(self):
        panels = self.panels()
        stile = self.stile()

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
        panels = self.panels()
        railQty = panels * 2
        return railQty

    def stileQty(self):
        panels = self.panels()
        stileQty = panels * 2
        return stileQty

    def LframeMaterial(self):
        Lwidth = self.LframeWidth()
        Lheight = self.LframeHeight()
        material = ((Lwidth + Lheight) / 12) * 2
        return round(material, 3)

    def louverMaterial(self):
        louver = self.louver()
        louverQty = self.louverQty()
        material = (louver / 12) * louverQty
        return round(material, 3)

    def railMaterial(self):
        rail = self.rail()
        railQty = self.railQty()
        material = (rail / 12) * railQty
        return round(material, 3)

    def stileMaterial(self):
        stile = self.stile()
        stileQty = self.stileQty()
        material = (stile / 12) * stileQty
        return round(material, 3)

    def tiltRodMaterial(self):
        Lwidth = self.LframeWidth()
        Lheight = self.LframeHeight()
        material = (Lwidth / 12) * (Lheight / 12)
        return round(material, 3)

    def panelMaterial(self):
        panels = self.panels()
        Lheight = self.LframeHeight()
        material = (Lheight / 12) * panels
        return round(material, 3)

    # def __str__(self):
    #     return f'shutter width: {self.width()} shutter height: {self.height()} total panels {self.panels()}.'



def ManufacturingReport(request, pk):
    p = proposal.objects.get(id=pk)
    p_agents = p.agents.all()
    p_measuredby = p.measured_by.all()
    cust_id = p.customer_id
    cust = customer.objects.get(pk=cust_id)
    line_items = line_item.objects.filter(proposal_id=pk)

    results = []
    for item in line_items:
        w = item.width
        h = item.height
        w_f = item.width_fraction
        h_f = item.height_fraction
        p = item.panels
        t = item.trim
        pt = item.shutter_type
        l = item.location

        shutter_instance = Shutter(width=w, height=h, width_fraction=w_f, height_fraction=h_f, panels=p, trim=t, prod_type=pt, location=l)
        results.append(shutter_instance)

    return render(request, 'manufacturing/report.html', {'results': results, 'customer': cust, 'agents': p_agents, 'measuredby': p_measuredby, 'lineitem': line_items})
