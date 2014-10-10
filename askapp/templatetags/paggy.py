from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()

@register.filter 
def paggy(n, steps):
    n=int(n)
    return range(n-steps, n+steps+1)
