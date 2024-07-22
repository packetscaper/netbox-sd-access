from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ipam.api.serializers import NestedVRFSerializer
from ..models import FabricSite, VirtualNetwork

#import and use NestedPrefix, Nested Device Serializer
class NestedFabricSiteSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_sd_access-api:fabricsite-detail'
    )
    
    class Meta:
        model = FabricSite
        fields = ('id', 'url', 'display', 'name')

class FabricSiteSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_sd_access-api:fabricsite-detail'
    )
    device_count = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = FabricSite
        fields = ('id', 'url', 'display', 'name', 'physical_site', 'location', 'ip_prefixes', 'device_count', 'devices', 
                  'tags', 'custom_fields', 'created', 'last_updated')
        
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
    vrf = NestedVRFSerializer()

    class Meta:
        model = VirtualNetwork
        fields = ('id','url', 'name', 'fabric_site','vrf', 'tags', 'custom_fields', 'created', 'last_updated')