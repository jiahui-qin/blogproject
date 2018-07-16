from ..models import bact, crudeex
from django import template
register = template.Library()

@register.simple_tag
def get_all_bact():
    print(bact.objects.all().order_by('-storetime'))
    return bact.objects.all().order_by('-storetime')
@register.simple_tag
def get_all_cru():
    print(crudeex.objects.all().order_by('-entertime'))
    return crudeex.objects.all().order_by('-entertime')