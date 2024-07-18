from netbox.filtersets import NetBoxModelFilterSet
from .models import *


# class SDAccessFilterSet(NetBoxModelFilterSet):
#
#     class Meta:
#         model = SDAccess
#         fields = ['name', ]
#
#     def search(self, queryset, name, value):
#         return queryset.filter(description__icontains=value)

class FabricSiteFilterSet(NetBoxModelFilterSet):
    
    class Meta:
        model = FabricSite
        fields = ('id', 'name', 'physical_site', 'location', 'ip_prefixes', 'devices')
    
    def search(self, queryset, name, value):
        return queryset.filter(name__icontains=value)
    
    
class IPTransitFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = IPTransit
        fields = ('id', 'name', 'fabric_site', 'asn', 'comments')
        
    def search(self, queryset, name, value):
        return queryset.filter(name__icontains=value)

class SDATransitFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = SDATransit
        fields = ('id', 'name', 'transit_type', 'fabric_site', 'control_plane_node', 'devices', 'comments')
        
    def search(self, queryset, name, value):
        return queryset.filter(name__icontains=value)