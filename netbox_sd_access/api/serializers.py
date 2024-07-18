from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import *

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

class NestedIPTransitSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = 'plugins-api:netbox_sd_access-api:iptransit-detail'
    )
    
    class Meta:
        model=IPTransit
        fields=('id','url','display','name')

class IPTransitSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_sd_access-api:iptransit-detail'
    )
    
    class Meta:
        model = IPTransit
        fields= ('id', 'url', 'display', 'name', 'fabric_site', 'asn', 'comments', 'tags', 'custom_fields', 'created', 'last_updated')


class NestedSDATransitSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = 'plugins-api:netbox_sd_access-api:sdatransit-detail'
    )
    
    class Meta:
        model=SDATransit
        fields=('id','url','display','name')
        
class SDATransitSerializer(NetBoxModelSerializer):
    url=serializers.HyperlinkedIdentityField(
        view_name = 'plugins-api:netbox_sd_access-api:sdatransit-detail'
    )
    
    class Meta:
        model=SDATransit
        fields=('id', 'url', 'display', 'name', 'transit_type', 'fabric_site', 'control_plane_node', 'devices', 'comments', 'tags', 'custom_fields', 'created', 'last_updated')