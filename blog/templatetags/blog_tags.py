from ..models import bact
from django import template
register = template.Library()

@register.simple_tag
def get_all_bact():
    print(bact.objects.all().order_by('-storetime'))
    return bact.objects.all().order_by('-storetime')