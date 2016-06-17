from django.core.urlresolvers import reverse_lazy
from django.http.response import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from paste.forms import PasteItemForm
from paste.models import PasteItem


class ItemCreateView(CreateView):
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


class ItemDuplicateDetailView(UpdateView):
    model = PasteItem
    form_class = PasteItemForm
    template_name = "create_item.html"

    def get_success_url(self):
        return reverse_lazy("item-detail", kwargs={"slug": self.object.slug})
