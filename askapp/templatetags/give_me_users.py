from django import template
from askapp.models import User
register = template.Library()

@register.inclusion_tag("show_users.html")
def show_users():
    users = User.objects.all().order_by("-date_joined")[:5]
    return {'users': users}
