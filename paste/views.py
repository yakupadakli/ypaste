from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from paste.forms import PasteItemForm
from paste.models import PasteItem


class ItemCreateView(CreateView):
    model = PasteItem
    form_class = PasteItemForm
    template_name = "create_item.html"
    success_url = reverse_lazy("item-create")


class ItemDetailView(DetailView):
    model = PasteItem
    template_name = "detail_item.html"
