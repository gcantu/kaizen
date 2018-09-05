from django.shortcuts import render
from proposal.models import line_item, proposal


class Shutter:
    def __init__(self, **kwargs):
        if 'width' in kwargs: self._width = kwargs['width']
        if 'height' in kwargs: self._height = kwargs['height']
        if 'panels' in kwargs: self._panels = kwargs['panels']
        if 'trim' in kwargs: self._trim = kwargs['trim']

    def width(self):
        return self._width
		# if w: self._width = w
		# try: return self._width
		# except AttributeError: return None

    def height(self):
        return self._height

    def panels(self):
        return self._panels

    def trim(self):
        return self._trim

    def LframeWidth(self):
        width = self.width()
        Lwidth = width - 0.375 # -3/8
        return round(Lwidth, 3)

    def LframeHeight(self):
        height = self.height()
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
    proposalInfo = proposal.objects.get(customer_id=pk)
    p_id = proposalInfo.id
    line_items = line_item.objects.filter(proposal_id=p_id)

    results = []
    for item in line_items:
        w = item.width
        h = item.height
        p = item.panels
        t = item.trim

        shutter_instance = Shutter(width=w, height=h, panels=p, trim=t)
        results.append(shutter_instance)

    return render(request, 'manufacturing/report.html', {'results': results})


# def ManufacturingReport(request, pk):
    # return render(request, 'manufacturing/report.html')
