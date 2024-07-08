from rest_framework import serializers
from ipam.api.serializers import NestedPrefixSerializer, NestedSiteSerializer
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer

from ..models import SDAccess, FabricSite

class SDAccessSerializer(NetBoxModelSerializer):
    
    url = serializers.HyperlinkedIdentityField(
        view_name= 'plugins-api:netbox_sd_access-api:sd_access-detail'
    )
    class Meta:
        model = SDAccess
        fields = (
            'name', 'url',
        )

class FabricSiteSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name= 'plugins-api:netbox_sd_access-api:fabricsite-detail'
    )
    
    #what is the use of a nestedfabricsiteserializer or nestedsdaccessserializer
    physical_site = NestedSiteSerializer()
    ip_prefixes = NestedPrefixSerializer()
    

    class Meta:
        model = FabricSite
        fields = (
            'name', 'physical_site', 'location', 'ip prefixes', 'devices', 'url'
        )

class NestedFabricSiteSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = 'plugins-api:netbox_sd_access-api:fabricsite-detail'
    )

    class Meta:
        model = FabricSite
        fields = ('name', 'physical_site', 'location', 'ip prefixes', 'devices',)

class NestedSDAccessSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name = 'plugins-api:netbox_sd_access-api:sd_access-detail'
    )

    class Meta:
        model = SDAccess
        fields = ('name',)