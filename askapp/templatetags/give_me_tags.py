from django import template
from askapp.models import User, Question, Tag
from django.db.models import Count
register = template.Library()

@register.inclusion_tag("show_tags.html")
def show_tags():

    tags = Tag.objects.annotate(count=Count('questions')).order_by('-count')[:10]
    return {'tags': tags}
