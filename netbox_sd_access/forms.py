from django import forms
from ipam.models import Prefix
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField

from .models import SDAccess


class SDAccessForm(NetBoxModelForm):
    class Meta:
        model = SDAccess
        fields = ("name", "tags")
