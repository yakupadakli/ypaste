from django.conf.urls import url
from paste.views import ItemCreateView, ItemDetailView, ItemRawDetailView

urlpatterns = [
    url(r'^$', ItemCreateView.as_view(), name="item-create"),
    url(r'^(?P<slug>[-A-Za-z0-9_]+)/$', ItemDetailView.as_view(), name="item-detail"),
    url(r'^(?P<slug>[-A-Za-z0-9_]+).txt/$', ItemRawDetailView.as_view(), name="item-raw-detail"),
]
