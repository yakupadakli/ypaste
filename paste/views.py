from django.core.urlresolvers import reverse_lazy
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from paste.forms import PasteItemForm, PasteItemExpiryForm
from paste.mixins import SessionMixin, JSONResponseMixin
from paste.models import PasteItem, Syntax

from pygments import highlight, styles
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name, guess_lexer


class ItemCreateView(SessionMixin, CreateView):
    model = PasteItem
    form_class = PasteItemForm
    template_name = "create_item.html"
    success_url = reverse_lazy("item-create")

    def get_success_url(self):
        return reverse_lazy("item-detail", kwargs={"slug": self.object.slug})


class ItemDetailView(DetailView):
    model = PasteItem
    template_name = "detail_item.html"


class ItemRawDetailView(DetailView):
    model = PasteItem
    template_name = ""

    def get(self, request, *args, **kwargs):
        item = self.get_object()
        return HttpResponse(item.content, content_type='text/plain')


class ItemDuplicateView(SessionMixin, UpdateView):
    model = PasteItem
    form_class = PasteItemForm
    template_name = "create_item.html"

    def get_success_url(self):
        return reverse_lazy("item-detail", kwargs={"slug": self.object.slug})


class ItemDeleteView(DeleteView):
    model = PasteItem
    template_name = "delete_item.html"
    success_url = reverse_lazy("item-create")


class ItemListView(ListView):
    model = PasteItem
    template_name = "list_item.html"

    def get_queryset(self):
        queryset = super(ItemListView, self).get_queryset()
        session_id = self.request.COOKIES.get("sessionid")
        if session_id:
            queryset = queryset.filter(session_id=session_id)
        else:
            queryset = []
        return queryset


class ItemChangeExpiryView(UpdateView):
    model = PasteItem
    form_class = PasteItemExpiryForm
    template_name = "change_item_expiry.html"
    success_url = reverse_lazy("item-create")

    def get_success_url(self):
        return reverse_lazy("item-detail", kwargs={"slug": self.object.slug})


class HighlightContentView(JSONResponseMixin, TemplateView):

    def get_data(self, context):
        syntax = "text"
        data = self.request.GET.get("data")
        syntax_id = self.request.GET.get("syntax_id")
        if syntax_id:
            syntax = Syntax.objects.get(pk=syntax_id)
            syntax = syntax.name
        lexer = get_lexer_by_name(syntax, stripall=True)
        formatter = HtmlFormatter(cssclass="source", style=styles.get_style_by_name("friendly"), linenos=False)
        result = highlight(data, lexer, formatter)
        context = {"data": result, "syntax": syntax}
        return context
