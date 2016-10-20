from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def home_title(context):
    if 'title' in context:
        return context['title']
    return 'Johanderson\'s Portfolio'
