from django import forms
from paste.models import PasteItem


class PasteItemForm(forms.ModelForm):

    class Meta:
        model = PasteItem
        fields = ["content", "syntax", "title", "username", "email", "delete_period"]

    def __init__(self, *args, **kwargs):
        super(PasteItemForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.iteritems():
            field.widget.attrs["title"] = field.label
            field.widget.attrs["class"] = "form-control"
