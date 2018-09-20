from django.shortcuts import render
from orders.models import line_item, proposal, customer


def asFraction(n):
    number = int(n)
    dec = round(n % 1, 4)

    if (dec == 0):
        return number
    else:
        ratio = dec.as_integer_ratio()
        frac = '{}/{}'.format(ratio[0], ratio[1])
        final = '{} {}'.format(number, frac)

        return final


class Shutter:
    def __init__(self, **kwargs):
        if 'w' in kwargs: self._w = kwargs['w']
        if 'h' in kwargs: self._h = kwargs['h']
        if 'w_f' in kwargs: self._w_f = kwargs['w_f']
        if 'h_f' in kwargs: self._h_f= kwargs['h_f']
        if 'panels' in kwargs: self._panels = kwargs['panels']
        if 'trim' in kwargs: self._trim = kwargs['trim']
        if 'prod_type' in kwargs: self._prod_type = kwargs['prod_type']
        if 'location' in kwargs: self._location = kwargs['location']

    def w(self): # width whole number
        return self._w

    def h(self): # height whole number
        return self._h

    def w_f(self): # width fraction
        return self._w_f

    def h_f(self): # height fraction
        return self._h_f

    def panels(self):
        return self._panels

    def trim(self):
        return self._trim

    def prod_type(self):
        return self._prod_type

    def location(self):
        return self._location

    def totalWidth(self): # whole number + fraction width
        width = self.w()
        width_f = self.w_f()
        total = width + width_f
        return(total)

    def totalHeight(self): # whole number + fraction height
        height = self.h()
        height_f = self.h_f()
        total = height + height_f
        return(total)

    def LframeW(self): # L frame width
        width = self.totalWidth()
        Lwidth = width - 0.375 # -3/8
        return round(Lwidth, 4)

    def LframeH(self): # L frame height
        height = self.totalHeight()
        Lheight = height - 0.25 # -1/4
        return round(Lheight, 4)

    def r(self): # rail
        panels = self.panels()
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
        Lheight = self.LframeH()
        stile = Lheight - 1.75 # 1 3/4
        return round(stile, 4)

    def tr(self):
        stile = self.s()
        Trod = stile - 9.875 # 9 7/8
        return round(Trod, 4)

    def totalHinges(self):
        Lheight = self.LframeH()
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
        hinges = self.totalHinges()
        screws = hinges * 6
        return screws

    def louverQty(self):
        panels = self.panels()
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
        panels = self.panels()
        railQty = panels * 2
        return railQty

    def stileQty(self):
        panels = self.panels()
        stileQty = panels * 2
        return stileQty

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
        panels = self.panels()
        Lheight = self.LframeH()
        material = (Lheight / 12) * panels
        return round(material, 4)

    # formatted fractions for manufacturing report display
    def width(self):
        prev = self.totalWidth()
        new = asFraction(prev)
        return new

    def height(self):
        prev = self.totalHeight()
        new = asFraction(prev)
        return new

    def LframeWidth(self):
        prev = self.LframeW()
        new = asFraction(prev)
        return new

    def LframeHeight(self):
        prev = self.LframeH()
        new = asFraction(prev)
        return new

    def rail(self):
        prev = self.r()
        new = asFraction(prev)
        return new

    def louver(self):
        prev = self.l()
        new = asFraction(prev)
        return new

    def stile(self):
        prev = self.s()
        new = asFraction(prev)
        return new

    def tiltRod(self):
        prev = self.tr()
        new = asFraction(prev)
        return new



def ManufacturingReport(request, pk):
    prop = proposal.objects.get(id=pk)
    p_agents = prop.agents.all()
    p_measuredby = prop.measured_by.all()
    cust_id = prop.customer_id
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

        shutter_instance = Shutter(w=w, h=h, w_f=w_f, h_f=h_f, panels=p, trim=t, prod_type=pt, location=l)
        results.append(shutter_instance)


    lf_m = round(sum(i.LframeMaterial() for i in results))
    l_m = round(sum(i.louverMaterial() for i in results))
    r_m = round(sum(i.railMaterial() for i in results))
    s_m = round(sum(i.stileMaterial() for i in results))
    tr_m = round(sum(i.tiltRodMaterial() for i in results))
    p_m = round(sum(i.panelMaterial() for i in results))
    h_m = round(sum(i.totalHinges() for i in results))
    m_m = round(sum(i.magnets() for i in results))
    sc_m = round(sum(i.screws() for i in results))

    materials = {
        'totalLframeMaterial':lf_m,
        'totalLouverMaterial':l_m,
        'totalRailMaterial':r_m,
        'totalStileMaterial':s_m,
        'totalTiltRodMaterial':tr_m,
        'totalPanelMaterial':p_m,
        'totalHinges':h_m,
        'totalMagnets':m_m,
        'totalScrews':sc_m
    }

    return render(request, 'reports/report.html', {'proposal': prop, 'results': results, 'customer': cust, 'agents': p_agents, 'measuredby': p_measuredby, 'lineitem': line_items, 'materials': materials})
