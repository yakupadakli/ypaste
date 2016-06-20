from django import forms
from django import template

register = template.Library()


@register.filter
def is_checkbox(field):
    return isinstance(field.field.widget, forms.CheckboxInput)


@register.filter
def is_multiple_checkbox(field):
    return isinstance(field.field.widget, forms.CheckboxSelectMultiple)


@register.filter
def is_radio(field):
    return isinstance(field.field.widget, forms.RadioSelect)


@register.filter
def is_file(field):
    return isinstance(field.field.widget, forms.FileInput)


@register.filter
def is_date_time(field):
    return isinstance(field.field.widget, forms.DateTimeInput)


@register.filter
def add_class(field, value):
    existing_classes = field.field.widget.attrs.get("class")
    existing_classes += " %s" % value
    field.field.widget.attrs["class"] = existing_classes
    return field


@register.filter
def add_ng_model(field):
    field.field.widget.attrs["ng-model"] = field.name
    if field.value():
        field.field.widget.attrs["ng-init"] = "%s='%s'" % (field.name, field.value())
    return field
