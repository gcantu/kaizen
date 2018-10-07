from django.shortcuts import render
from orders.models import line_item, proposal, customer



def proposalReport(request, pk):
    p = proposal.objects.get(pk=pk)
    p_agents = p.agents.all()
    p_measuredby = p.measured_by.all()
    cust_id = p.customer_id
    cust = customer.objects.get(pk=cust_id)
    lineitem = line_item.objects.filter(proposal_id=pk)

    # calculate proposal total with/without tax
    subtotal = round(sum(i.totalPrice() for i in lineitem), 2)
    tax = round(subtotal*.0825, 2)
    total = subtotal+tax

    return render(request, 'reports/content.html', {'customer': cust, 'proposal': p, 'agents': p_agents, 'measuredby': p_measuredby, 'lineitem': lineitem, 'subtotal': subtotal, 'tax': tax, 'total': total, 'report_name': 'proposal'})


def manufacturingReport(request, pk):
    prop = proposal.objects.get(id=pk)
    p_agents = prop.agents.all()
    p_measuredby = prop.measured_by.all()
    cust_id = prop.customer_id
    cust = customer.objects.get(pk=cust_id)
    lineitem = line_item.objects.filter(proposal_id=pk).order_by('shutter_type_id')

    materials = {
        'totalLframeMaterial': round(sum(i.LframeMaterial() for i in lineitem)),
        'totalLouverMaterial': round(sum(i.louverMaterial() for i in lineitem)),
        'totalRailMaterial': round(sum(i.railMaterial() for i in lineitem)),
        'totalStileMaterial': round(sum(i.stileMaterial() for i in lineitem)),
        'totalTiltRodMaterial': round(sum(i.tiltRodMaterial() for i in lineitem)),
        'totalPanelMaterial': round(sum(i.panelMaterial() for i in lineitem)),
        'totalHinges': round(sum(i.totalHinges() for i in lineitem)),
        'totalMagnets': round(sum(i.magnets() for i in lineitem)),
        'totalScrews': round(sum(i.screws() for i in lineitem))
    }

    return render(request, 'reports/content.html', {'proposal': prop, 'customer': cust, 'agents': p_agents, 'measuredby': p_measuredby, 'lineitem': lineitem, 'materials': materials, 'report_name': 'manufacturing'})



def invoiceReport(request, pk):
    p = proposal.objects.get(pk=pk)
    p_agents = p.agents.all()
    p_measuredby = p.measured_by.all()
    cust_id = p.customer_id
    cust = customer.objects.get(pk=cust_id)
    lineitem = line_item.objects.filter(proposal_id=pk)

    # calculate proposal total with/without tax
    subtotal = round(sum(i.totalPrice() for i in lineitem), 2)
    tax = round(subtotal*.0825, 2)
    total = subtotal+tax

    return render(request, 'reports/content.html', {'customer': cust, 'proposal': p, 'agents': p_agents, 'measuredby': p_measuredby, 'lineitem': lineitem, 'subtotal': subtotal, 'tax': tax, 'total': total, 'report_name': 'invoice'})
