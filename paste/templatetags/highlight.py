from django import template

from pygments import highlight, styles
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name, guess_lexer


register = template.Library()


@register.filter(is_safe=True)
def highlighter(content, name, linenos=True):
    lexer = get_lexer_by_name(name, stripall=True)
    formatter = HtmlFormatter(cssclass="source", style=styles.get_style_by_name("friendly"), linenos=linenos)
    result = highlight(content, lexer, formatter)
    return result


@register.filter(is_safe=True)
def highlighter_without_number(content, name):
    return highlight(content, name, linenos=False)
