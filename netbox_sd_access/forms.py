from django import forms
from ipam.models import Prefix, IPAddress, ASN, VRF
from dcim.models import Site, Location, Device
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm, NetBoxModelImportForm, NetBoxModelBulkEditForm
from utilities.forms.fields import (
    CommentField,
    DynamicModelChoiceField,
    DynamicModelMultipleChoiceField,
    CSVChoiceField,
    CSVModelChoiceField,
    CSVModelMultipleChoiceField,
)

from .models import *

class FabricSiteForm(NetBoxModelForm):
    """
    GUI form for creating or editing a Fabric Site.
    Requires a name, physical site, and location.
    """
    physical_site = DynamicModelChoiceField(queryset=Site.objects.all(),required=True)
    location = DynamicModelChoiceField(queryset=Location.objects.all(), required=False, query_params={'site_id': '$physical_site'} )
    ip_prefixes = DynamicModelMultipleChoiceField(queryset=IPPool.objects.all(), required=False, label='IP Pools')
    comments = CommentField()
    
    class Meta:
        model = FabricSite
        fields = ('name', 'physical_site', 'location', 'ip_prefixes', 'comments', 'tags')

class FabricSiteFilterForm(NetBoxModelFilterSetForm):
    """
    GUI form for filtering and searching Fabric Sites.
    """
    model = FabricSite
    physical_site = forms.ModelMultipleChoiceField(
        queryset=Site.objects.all(),
        required=False
    )

class FabricSiteImportForm(NetBoxModelImportForm):
    """
    GUI form for bulk importing Fabric Sites using CSV format.
    """
    physical_site = CSVModelChoiceField(
        queryset=Site.objects.all(),
        to_field_name="name",
    )
    location = CSVModelChoiceField(
        queryset=Location.objects.all(),
        to_field_name="name",
    )
    ip_prefixes = CSVModelMultipleChoiceField(
        queryset=IPPool.objects.all(),
        to_field_name = "name",
    )
    
    class Meta:
        model = FabricSite
        fields = ('name', 'physical_site', 'location', 'ip_prefixes', 'tags')
    
class IPTransitForm(NetBoxModelForm):
    """
    GUI form for creating and editing IP Transits.
    Requires a name, fabric site, and ASN.
    """
    fabric_site = DynamicModelChoiceField(queryset=FabricSite.objects.all(), required=True)
    asn = DynamicModelChoiceField(queryset=ASN.objects.all())
    comments = CommentField()
    
    class Meta:
        model = IPTransit
        fields = ('name', 'fabric_site', 'asn', 'comments', 'tags')
        
class IPTransitFilterForm(NetBoxModelFilterSetForm):
    """
    GUI form for filtering and searching IP Transits.
    """
    model = IPTransit
    fabric_site = forms.ModelMultipleChoiceField(
        queryset=FabricSite.objects.all(),
        required=False
    )

class IPTransitImportForm(NetBoxModelImportForm):
    """
    GUI form for bulk importing IP Transits using CSV format.
    """
    fabric_site = CSVModelChoiceField(
        queryset=FabricSite.objects.all(),
        to_field_name="name",
        help_text='Fabric site'
    )
    asn = CSVModelChoiceField(
        queryset=ASN.objects.all(),
        to_field_name="name",
        help_text='ASN',
    )

    class Meta:
        model = IPTransit
        fields = ('fabric_site', 'asn', 'comments', 'tags')
    
class SDATransitForm(NetBoxModelForm):
    """
    GUI form for creating and editing SDA Transits.
    Requires name, fabric site, control plane node, and list of devices.
    """
    fabric_site = DynamicModelChoiceField(queryset=FabricSite.objects.all(), required=True)
    control_plane_node = DynamicModelChoiceField(queryset=SDADevice.objects.all(), required=True)
    devices = DynamicModelMultipleChoiceField(queryset=SDADevice.objects.all())
    comments = CommentField()
    
    class Meta:
        model = SDATransit
        fields = ('name', 'transit_type', 'fabric_site', 'control_plane_node', 'devices', 'comments', 'tags')
        
class SDATransitFilterForm(NetBoxModelFilterSetForm):
    """
    GUI form for filtering and searching SDA Transits.
    """
    model = SDATransit
    fabric_site = forms.ModelMultipleChoiceField(
        queryset=FabricSite.objects.all(),
        required=False
    )
    transit_type = forms.MultipleChoiceField(choices=SDATransitTypeChoices, required=False, initial=None)
    
class SDATransitImportForm(NetBoxModelImportForm):
    """
    GUI form for bulk importing SDA Transits using CSV format.
    """
    transit_type = CSVChoiceField(
        choices=SDATransitTypeChoices, help_text='SDA trasit type'
    )
    fabric_site = CSVModelChoiceField(
        queryset=FabricSite.objects.all(),
        to_field_name="name",
        help_text='Fabric site'
    )
    control_plane_node = CSVModelChoiceField(
        queryset=SDADevice.objects.all(),
        to_field_name="name",
        help_text='Control plane node, an SDA device',
    )
    devices = CSVModelMultipleChoiceField(
        queryset=SDADevice.objects.all(),
        to_field_name="name",
        help_text='SDA devices within the transit',
    )

    class Meta:
        model = SDATransit
        fields = ('transit_type', 'fabric_site', 'control_plane_node', 'devices', 'comments', 'tags')

class SDADeviceForm(NetBoxModelForm):
    """
    GUI Form for creating and editing SDA Devices.
    Requires a physical device and a fabric site.
    """
    physical_site = DynamicModelChoiceField(queryset=Site.objects.all(), required=False)
    location = DynamicModelChoiceField(queryset=Location.objects.all(), required=False, query_params={'site_id': '$physical_site'})
    fabric_site = DynamicModelChoiceField(
        queryset=FabricSite.objects.all(), 
        required=True,
        query_params={'physical_site': '$physical_site', 'location': '$location'}
    )
    device = DynamicModelChoiceField(
        queryset=Device.objects.all(), 
        required=True, 
        query_params={'site_id': '$physical_site', 'location_id': '$location'}
    )
    comments = CommentField()
    
    class Meta:
        model = SDADevice
        fields = ('physical_site', 'location', 'fabric_site', 'device', 'role', 'comments', 'tags',)

class SDADeviceImportForm(NetBoxModelImportForm):
    """
    GUI Form for bulk importing SDA Devices using CSV format.
    """
    device = CSVModelChoiceField(
        queryset=Device.objects.all(),
        to_field_name="name",
        help_text='Physical device',
    )
    fabric_site = CSVModelChoiceField(
        queryset=FabricSite.objects.all(),
        to_field_name="name",
        help_text='Fabric site'
    )
    role = CSVChoiceField(
        choices=SDADeviceRoleChoices, help_text='SDA role'
    )
    
    class Meta:
        model = SDADevice
        fields = ('device', 'fabric_site', 'role', 'comments', 'tags')

class SDADeviceFilterForm(NetBoxModelFilterSetForm):
    """
    GUI form for filtering and searching SDA Devices.
    """
    model = SDADevice
    site = forms.ModelChoiceField(queryset=FabricSite.objects.all(), required=False)
    role = forms.MultipleChoiceField(choices=SDADeviceRoleChoices, required=False, initial=None)

class IPPoolForm(NetBoxModelForm):
    """
    GUI form for creating and editing IP Pools.
    Requires a name, prefix, gateway, and DHCP server.
    """
    prefix = DynamicModelChoiceField(queryset=Prefix.objects.all(), required=True)
    gateway = DynamicModelChoiceField(queryset=IPAddress.objects.all(), required=True)
    dhcp_server = DynamicModelChoiceField(queryset=IPAddress.objects.all(), required=True)
    dns_servers = DynamicModelMultipleChoiceField(queryset=IPAddress.objects.all(), required=False)
    comments = CommentField()
    
    class Meta:
        model = IPPool
        fields = ('name', 'prefix', 'gateway', 'dhcp_server', 'dns_servers', 'comments')

class IPPoolImportForm(NetBoxModelImportForm):
    """
    GUI form for bulk importing IP Pools using CSV format.
    """
    prefix = CSVModelChoiceField(
        queryset=Prefix.objects.all(),
        to_field_name='prefix'
    )
    gateway = CSVModelChoiceField(
        queryset=IPAddress.objects.all(),
        to_field_name='address'
    )
    dhcp_server = CSVModelChoiceField(
        queryset=IPAddress.objects.all(),
        to_field_name='address'
    )
    dns_servers = CSVModelMultipleChoiceField(
        queryset=IPAddress.objects.all(),
        to_field_name='address',
        required=False
    )
    
    class Meta:
        model = IPPool
        fields = ('name', 'prefix', 'gateway', 'dhcp_server', 'dns_servers')

class IPPoolFilterForm(NetBoxModelFilterSetForm):
    """
    GUI form for filtering and searching IP Pools.
    """
    model = IPPool
    prefix = DynamicModelChoiceField(queryset=Prefix.objects.all(), required=False)

class VirtualNetworkForm(NetBoxModelForm):
    """
    GUI form for creating and editing virtual networks.
    Requires a name, fabric sites, and a VRF.
    """
    fabric_site = DynamicModelMultipleChoiceField(queryset = FabricSite.objects.all(), required=True)
    vrf = DynamicModelChoiceField(queryset = VRF.objects.all(), required=True, label='VRF')

    class Meta:
        model = VirtualNetwork
        fields = ('name', 'fabric_site', 'vrf')

class VirtualNetworkImportForm(NetBoxModelImportForm):
    """
    GUI form for bulk importing virtual networks using CSV format.
    """
    fabric_site = CSVModelMultipleChoiceField(
        queryset=FabricSite.objects.all(),
        to_field_name='name'
    )
    vrf = CSVModelChoiceField(
        queryset=VRF.objects.all(),
        to_field_name='name',
        required=True
    )
    
    class Meta:
        model = VirtualNetwork
        fields = ('name', 'fabric_site', 'vrf')

class VirtualNetworkFilterForm(NetBoxModelFilterSetForm):
    """
    GUI form for filtering and searching virtual networks.
    """
    model = VirtualNetwork
    fabric_site = DynamicModelChoiceField(
        queryset = FabricSite.objects.all(),
        required=False
    )
