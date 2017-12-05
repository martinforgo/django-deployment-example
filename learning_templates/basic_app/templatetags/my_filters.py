from django import template

register = template.Library()

@register.filter(name='cutting')
def cutter(value, arg):
    return value.replace(arg, '')