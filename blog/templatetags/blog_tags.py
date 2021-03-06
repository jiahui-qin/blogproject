from ..models import bact, crudeex,cpd
from django import template
from django.db.models.aggregates import Count
register = template.Library()

@register.simple_tag
def get_all_bact():
    return bact.objects.all().order_by('-storetime')
@register.simple_tag
def get_all_cru():
    return crudeex.objects.all().order_by('-entertime')
@register.simple_tag
def get_all_cpd():
    return cpd.objects.all().order_by('-time')
@register.simple_tag
def get_cru():
    return bact.objects.annotate(num_crudeex=Count('crudeex'))
