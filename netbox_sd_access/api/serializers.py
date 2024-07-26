from rest_framework import serializers

from dcim.api.serializers import SiteSerializer, LocationSerializer, DeviceSerializer
from ipam.models import IPAddress
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from netbox.api.fields import SerializedPKRelatedField, ChoiceField
from ipam.api.serializers import NestedVRFSerializer, IPAddressSerializer, PrefixSerializer
from ..models import FabricSite, IPPool, SDADevice, IPTransit, SDATransit, VirtualNetwork, SDADeviceRoleChoices

#import and use NestedPrefix, Nested Device Serializer
class NestedFabricSiteSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_sd_access-api:fabricsite-detail'
    )
    
    class Meta:
        model = FabricSite
        fields = ('id', 'url', 'display', 'name')
        
class NestedIPPoolSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_sd_access-api:ippool-detail'
    )
    prefix = PrefixSerializer(nested=True)
    
    class Meta:
        model = IPPool
        fields = ('id', 'url', 'display', 'name', 'prefix')

class FabricSiteSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_sd_access-api:fabricsite-detail'
    )
    physical_site = SiteSerializer(nested=True)
    device_count = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = FabricSite
        fields = ('id', 'url', 'display', 'name', 'physical_site', 'location', 'ip_prefixes', 'device_count', 'tags', 'custom_fields', 'created', 'last_updated')
        brief_fields = ('id', 'url', 'display', 'name', 'device_count')

class NestedIPTransitSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = 'plugins-api:netbox_sd_access-api:iptransit-detail'
    )
    
    class Meta:
        model = IPTransit
        fields = ('id','url','display','name')

class IPTransitSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = 'plugins-api:netbox_sd_access-api:iptransit-detail'
    )
    
    class Meta:  
        model = IPTransit
        fields= ('id', 'url', 'display', 'name', 'fabric_site', 'asn', 'comments', 'tags', 'custom_fields', 'created', 'last_updated')
    
    
class SDADeviceSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_sd_access-api:sdadevice-detail'
    )
    fabric_site = NestedFabricSiteSerializer()
    device = DeviceSerializer(nested=True)
    role = ChoiceField(choices=SDADeviceRoleChoices)
    
    class Meta:
        model = SDADevice
        fields = ('id', 'url', 'display', 'device', 'role', 'fabric_site', 'tags', 'custom_fields', 'created', 'last_updated')
        brief_fields = ('id', 'url', 'display', 'device', 'role', 'fabric_site')

class NestedSDATransitSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = 'plugins-api:netbox_sd_access-api:sdatransit-detail'
    )
    
    class Meta:
        model = SDATransit
        fields = ('id','url','display','name')
        
class SDATransitSerializer(NetBoxModelSerializer):
    url=serializers.HyperlinkedIdentityField(
        view_name = 'plugins-api:netbox_sd_access-api:sdatransit-detail'
    )
    
    class Meta:
        model = SDATransit
        fields = ('id', 'url', 'display', 'name', 'transit_type', 'fabric_site', 'control_plane_node', 'devices', 'comments', 'tags', 'custom_fields', 'created', 'last_updated')
        brief_fields = ('id', 'url', 'display', 'name', 'transit_type', 'fabric_site', 'control_plane_node')

class IPPoolSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_sd_access-api:ippool-detail'
    )
    prefix = PrefixSerializer(nested=True)
    gateway = IPAddressSerializer(nested=True)
    dhcp_server = IPAddressSerializer(nested=True)
    dns_servers = SerializedPKRelatedField(
        queryset=IPAddress.objects.all(),
        serializer=IPAddressSerializer,
        nested=True,
        required=False,
        allow_null=True,
        many=True
    )
    
    class Meta:
        model = IPPool
        fields = ('id', 'url', 'display', 'name', 'prefix', 'gateway', 'dhcp_server', 'dns_servers')
        brief_fields = ('id', 'url', 'display', 'prefix')

class NestedVirtualNetworkSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_sd_access-api:virtualnetwork-detail'
    )

    class Meta:
        model = VirtualNetwork
        fields = ('id', 'url', 'display', 'name')

class VirtualNetworkSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_sd_access-api:virtualnetwork-detail'
    )
    fabric_site = SerializedPKRelatedField(
        queryset=FabricSite.objects.all(),
        serializer=FabricSiteSerializer,
        nested=True,
        required=False,
        many=True
    )
    vrf = NestedVRFSerializer()

    class Meta:
        model = VirtualNetwork
        fields = ('id','url', 'name', 'fabric_site','vrf', 'tags', 'custom_fields', 'created', 'last_updated')
        brief_fields = ('id', 'url', 'name', 'fabric_site')
