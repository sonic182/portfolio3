from django import template
# from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext as _

register = template.Library()

@register.simple_tag(takes_context=True)
def home_title(context):
    if 'title' in context:
        return context['title']
    return 'Johanderson\'s Portfolio'

@register.simple_tag(takes_context=True)
def meta_description(context):
    if 'meta_description' in context:
        return context['meta_description']
    return _('meta description')
