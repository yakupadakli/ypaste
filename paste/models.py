from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _
from ypaste.utils import unique_slugify


class PasteItem(models.Model):
    ONE_DAY = 1
    ONE_WEEK = 2
    ONE_MONTH = 3
    ONE_YEAR = 4

    DELETE_PERIOD = (
        (ONE_DAY, _(u"One Day")),
        (ONE_WEEK, _(u"One Week")),
        (ONE_MONTH, _(u"One Month")),
        (ONE_YEAR, _(u"One Year")),
    )

    slug = models.SlugField(max_length=128, unique=True, editable=False)
    content = models.TextField(verbose_name=_(u"Content"))
    syntax = models.ForeignKey("Syntax", verbose_name=_(u"Syntax"))
    title = models.CharField(_(u"Title"), max_length=64)
    username = models.CharField(_(u"Your Name or Nick"), max_length=32)
    email = models.EmailField(_(u"Email"), null=True, blank=True)
    delete_period = models.PositiveIntegerField(_(u"Delete In"), choices=DELETE_PERIOD)

    def __unicode__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = unique_slugify(self, self.title.upper())
        return super(PasteItem, self).save()


class Syntax(models.Model):
    name = models.CharField(verbose_name=_(u"Name"), max_length=64, unique=True)
    is_active = models.BooleanField(verbose_name=_(u"Is Active?"), default=True)
    slug = models.SlugField(max_length=128, unique=True, editable=False)

    def __unicode__(self):
        return self.name
