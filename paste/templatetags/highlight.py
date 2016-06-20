from django import template

from paste.utils import highlighter_helper, highlighter_without_number_helper

register = template.Library()


@register.filter(is_safe=True)
def highlighter(content, name):
    return highlighter_helper(content, name)


@register.filter(is_safe=True)
def highlighter_without_number(content, name):
    return highlighter_without_number_helper(content, name)
