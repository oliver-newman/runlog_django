"""
Custom filters for activities
"""
from django import template

register = template.Library()

# For activity objects, returns whether title is empty
@register.filter
def hasTitle(activity):
    return activity.hasTitle()
