from django.views.generic.edit import CreateView

from paste.forms import PasteItemForm
from paste.models import PasteItem


class ItemCreateView(CreateView):
    model = PasteItem
    form_class = PasteItemForm
    template_name = "create_item.html"
