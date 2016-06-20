from django import forms

from paste.models import PasteItem


class PasteItemForm(forms.ModelForm):

    class Meta:
        model = PasteItem
        fields = ["content", "syntax", "title", "username", "email", "delete_period", "session_id"]

    def __init__(self, *args, **kwargs):
        self.session = kwargs.pop("session", "")
        super(PasteItemForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.iteritems():
            field.widget.attrs["title"] = field.label
            field.widget.attrs["class"] = "form-control"
        session_id = self.fields['session_id']
        session_id.widget = forms.HiddenInput()
        session_id.required = False
        session_id.initial = self.session

        syntax = self.fields['syntax']
        syntax.queryset = syntax.queryset.filter(is_active=True).order_by("name")

    def save(self, commit=True):
        obj = super(PasteItemForm, self).save()
        if not obj.session_id:
            obj.session_id = PasteItem.create_unique_session_id()
            obj.save()
        return obj


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
