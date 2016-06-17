from django.conf.urls import url
from paste.views import ItemCreateView

urlpatterns = [
    url(r'^$', ItemCreateView.as_view(), name="item-create"),
]
