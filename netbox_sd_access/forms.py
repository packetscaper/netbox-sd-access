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
    physical_site = DynamicModelChoiceField(queryset=Site.objects.all(),required=True)
    location = DynamicModelChoiceField(queryset=Location.objects.all(), required=False, query_params={'site_id': '$physical_site'} )
    ip_prefixes = DynamicModelMultipleChoiceField(queryset=Prefix.objects.all(), required=True, label='IP Prefixes')
    devices = DynamicModelMultipleChoiceField(queryset=Device.objects.all(), required=True, query_params={'site_id':'$physical_site', 'location_id':'$location'})
    
    class Meta:
        model = FabricSite
        fields = ('name', 'physical_site', 'location', 'ip_prefixes', 'devices')

class FabricSiteFilterForm(NetBoxModelFilterSetForm):
    model = FabricSite
    physical_site = forms.ModelMultipleChoiceField(
        queryset=Site.objects.all(),
        required=False
    )
    
class IPTransitForm(NetBoxModelForm):
    fabric_site = DynamicModelChoiceField(queryset=FabricSite.objects.all(), required=True)
    asn = forms.IntegerField(required=False)
    comments = CommentField()
    
    class Meta:
        model = IPTransit
        fields = ('name', 'fabric_site', 'asn', 'comments', 'tags')
        
class IPTransitFilterForm(NetBoxModelFilterSetForm):
    model = IPTransit
    fabric_site = forms.ModelMultipleChoiceField(
        queryset=FabricSite.objects.all(),
        required=False
    )
    
class SDATransitForm(NetBoxModelForm):
    #transit_type = ArrayField(queryset=SDATransitType.choices(),required=True)
    fabric_site = DynamicModelChoiceField(queryset=FabricSite.objects.all(), required=True)
    control_plane_node = DynamicModelChoiceField(queryset=Device.objects.all(), required=True)
    devices = DynamicModelMultipleChoiceField(queryset=Device.objects.all())
    comments = CommentField()
    
    class Meta:
        model = SDATransit
        fields = ('name', 'transit_type', 'fabric_site', 'control_plane_node', 'devices', 'comments', 'tags')
        
class SDATransitFilterForm(NetBoxModelFilterSetForm):
    model = IPTransit
    fabric_site = forms.ModelMultipleChoiceField(
        queryset=FabricSite.objects.all(),
        required=False
    )