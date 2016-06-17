from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils.crypto import get_random_string
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
    session_id = models.CharField(verbose_name=_("Session Id"), max_length=64)
    created_at = models.DateTimeField(verbose_name=_(u"Created At"), auto_now_add=True)

    def __unicode__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = unique_slugify(self, self.title.upper())
        return super(PasteItem, self).save()

    def get_expiry_day(self):
        now = datetime.datetime.now()
        if self.delete_period == self.ONE_DAY:
            return now.day - self.created_at.date().day + 1
        elif self.delete_period == self.ONE_WEEK:
            return now.day - self.created_at.date().day + 7
        elif self.delete_period == self.ONE_MONTH:
            return now.day - self.created_at.date().day + 30
        elif self.delete_period == self.ONE_YEAR:
            return now.day - self.created_at.date().day + 365
        return 0

    @staticmethod
    def create_unique_session_id():
        session_id = get_random_string(length=32, allowed_chars="abcdefghijklmnopqrstuvwxyz1234567890")
        item = PasteItem.objects.first()
        if item:
            session_id = unique_slugify(item, session_id, slug_field_name="session_id", slug_separator="")
        return session_id


class Syntax(models.Model):
    name = models.CharField(verbose_name=_(u"Name"), max_length=64, unique=True)
    is_active = models.BooleanField(verbose_name=_(u"Is Active?"), default=True)
    slug = models.SlugField(max_length=128, unique=True, editable=False)

    def __unicode__(self):
        return self.name
