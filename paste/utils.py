from pygments import highlight, styles
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name, guess_lexer


def highlighter_helper(content, name, linenos=True, css_class="source"):
    lexer = get_lexer_by_name(name, stripall=True)
    formatter = HtmlFormatter(cssclass=css_class, style=styles.get_style_by_name("friendly"), linenos=linenos)
    result = highlight(content, lexer, formatter)
    return result


def highlighter_without_number_helper(content, name, css_class="source"):
    return highlighter_helper(content, name, linenos=False, css_class=css_class)
