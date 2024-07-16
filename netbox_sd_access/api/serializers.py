from rest_framework import serializers

from dcim.api.serializers import SiteSerializer
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
    physical_site = SiteSerializer(nested=True)
    device_count = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = FabricSite
        fields = ('id', 'url', 'display', 'name', 'physical_site', 'location', 'ip_prefixes', 'device_count', 
                  'tags', 'custom_fields', 'created', 'last_updated')

class SDADeviceSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_sd_access-api:sdadevice-detail'
    )
    fabric_site = NestedFabricSiteSerializer()
    
    class Meta:
        model = SDADevice
        fields = ('id', 'url', 'display', 'device', 'role', 'fabric_site', 'tags', 'custom_fields', 
                  'created', 'last_updated')