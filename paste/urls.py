from django.conf.urls import url
from paste.views import (ItemCreateView, ItemDetailView, ItemRawDetailView, ItemDuplicateView, ItemDeleteView,
                         ItemListView, ItemChangeExpiryView, HighlightContentView)

urlpatterns = [
    url(r'^$', ItemCreateView.as_view(), name="item-create"),
    url(r'^yours/$', ItemListView.as_view(), name="item-list"),
    url(r'^get/highlight/data/$', HighlightContentView.as_view(), name="get-highlight-data"),
    url(r'^(?P<slug>[-A-Za-z0-9_]+)/$', ItemDetailView.as_view(), name="item-detail"),
    url(r'^(?P<slug>[-A-Za-z0-9_]+).txt/$', ItemRawDetailView.as_view(), name="item-raw-detail"),
    url(r'^(?P<slug>[-A-Za-z0-9_]+)/duplicate/$', ItemDuplicateView.as_view(), name="item-duplicate"),
    url(r'^(?P<slug>[-A-Za-z0-9_]+)/delete/$', ItemDeleteView.as_view(), name="item-delete"),
    url(r'^(?P<slug>[-A-Za-z0-9_]+)/expiry/$', ItemChangeExpiryView.as_view(), name="item-expiry"),
]
