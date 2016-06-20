from django import forms
from django.utils.translation import ugettext as _

from paste.models import PasteItem


class PasteItemForm(forms.ModelForm):
    is_sent_email = forms.BooleanField(label=_(u"Sent Email To Me"), initial=False, required=False)

    class Meta:
        model = PasteItem
        fields = ["content", "syntax", "title", "username", "email", "is_sent_email", "delete_period", "session_id"]

    def __init__(self, *args, **kwargs):
        self.session = kwargs.pop("session", "")
        super(PasteItemForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.iteritems():
            if name != "is_sent_email":
                field.widget.attrs["title"] = field.label
                field.widget.attrs["class"] = "form-control"
        session_id = self.fields['session_id']
        session_id.widget = forms.HiddenInput()
        session_id.required = False
        session_id.initial = self.session

        syntax = self.fields['syntax']
        syntax.queryset = syntax.queryset.filter(is_active=True).order_by("name")

    def save(self, commit=True):
        item = super(PasteItemForm, self).save()
        if item.email:
            pass

        if not item.session_id:
            item.session_id = PasteItem.create_unique_session_id()
            item.save()
        return item

    def clean(self):
        is_sent_email = self.cleaned_data.get("is_sent_email")
        email = self.cleaned_data.get("email")
        if is_sent_email and not email:
            self.errors['email'] = [_(u"This field is required.")]
        return self.cleaned_data


class PasteItemExpiryForm(forms.ModelForm):

    class Meta:
        model = PasteItem
        fields = ("delete_period",)

    def __init__(self, *args, **kwargs):
        self.session = kwargs.pop("session", "")
        super(PasteItemExpiryForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.iteritems():
            field.widget.attrs["title"] = field.label
            field.widget.attrs["class"] = "form-control"
        delete_period = self.fields['delete_period']
        delete_period.empty_label = None
