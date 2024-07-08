from django import forms
from ipam.models import Prefix
from dcim.models import Site, Location, Device
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField, DynamicModelMultipleChoiceField

from .models import *


class SDAccessForm(NetBoxModelForm):
    class Meta:
        model = SDAccess
        fields = ("name", "tags")

class FabricSiteForm(NetBoxModelForm):
    physical_site = DynamicModelChoiceField(queryset=Site.objects.all(), required=True)
    location = DynamicModelChoiceField(queryset=Location.objects.all(), required=False)
    ip_prefixes = DynamicModelMultipleChoiceField(queryset=Prefix.objects.all(), required=True)
    devices = DynamicModelMultipleChoiceField(queryset=Device.objects.all(), required=True)
    
    class Meta:
        model = FabricSite
        fields = ('name', 'physical_site', 'location', 'ip_prefixes', 'devices')

class FabricSiteFilterForm(NetBoxModelFilterSetForm):
    model = FabricSite
    physical_site = forms.ModelMultipleChoiceField(
        queryset=Device.objects.all(),
        required=False
    )