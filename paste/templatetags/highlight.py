from django import template

from pygments import highlight, styles
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name, guess_lexer


register = template.Library()


@register.filter(is_safe=True)
def highlighter(content, name):
    lexer = get_lexer_by_name(name, stripall=True)
    formatter = HtmlFormatter(cssclass="source", style=styles.get_style_by_name("friendly"), linenos=True)
    result = highlight(content, lexer, formatter)
    return result
