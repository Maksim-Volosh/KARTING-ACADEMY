from django import template

register = template.Library()

@register.filter
def filename(value):
    return value.name.split('/')[-1]

@register.filter
def gap(value, value2):
    try:
        return float(value) - float(value2) if value2 else value
    except (TypeError, ValueError):
        return ''
    
@register.filter
def index(sequence, position):
    try:
        return sequence[position]
    except IndexError:
        return None