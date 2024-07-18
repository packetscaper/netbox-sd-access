from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ipam.api.serializers import NestedPrefixSerializer, NestedIPAddressSerializer
from ..models import FabricSite, IPPool

#import and use NestedPrefix, Nested Device Serializer
class NestedFabricSiteSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_sd_access-api:fabricsite-detail'
    )
    
    class Meta:
        model = FabricSite
        fields = ('id', 'url', 'display', 'name')
        
class NextedIPPoolSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_sd_access-api:ippool-detail'
    )
    prefix = NestedPrefixSerializer()
    
    class Meta:
        model = IPPool
        fields = ('id', 'url', 'display', 'name', 'prefix')

class FabricSiteSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_sd_access-api:fabricsite-detail'
    )
    device_count = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = FabricSite
        fields = ('id', 'url', 'display', 'name', 'physical_site', 'location', 'ip_prefixes', 'device_count', 'devices', 
                  'tags', 'custom_fields', 'created', 'last_updated')

class IPPoolSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_sd_access-api:ippool-detail'
    )
    prefix = NestedPrefixSerializer()
    gateway = NestedIPAddressSerializer()
    dhcp_server = NestedIPAddressSerializer()
    dns_servers = NestedIPAddressSerializer(many=True)
    
    class Meta:
        model = IPPool
        fields = ('id', 'url', 'display', 'name', 'prefix', 'gateway', 'dhcp_server', 'dns_servers')