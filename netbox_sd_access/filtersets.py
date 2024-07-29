import django_filters
from django.db.models import Q
from netbox.filtersets import NetBoxModelFilterSet
from .models import *
from dcim.models import Site

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
        fields = ('id', 'name', 'physical_site', 'location', 'ip_prefixes', 'comments')
    
    def search(self, queryset, name, value):
        return queryset.filter(Q(name__icontains=value) | Q(comments__icontains=value))

class SDADeviceFilterSet(NetBoxModelFilterSet):
    role = django_filters.CharFilter(field_name='role', lookup_expr='exact')
    
    class Meta:
        model = SDADevice
        fields = ('role','fabric_site')
    
    def search(self, queryset, name, value):
        # return queryset.filter(comments__icontains=value)
        return queryset.filter(Q(comments__icontains=value) | Q(device__name__icontains=value))
    

class IPTransitFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = IPTransit
        fields = ('id', 'name', 'fabric_site', 'asn', 'comments')
        
    def search(self, queryset, name, value):
        return queryset.filter(name__icontains=value)

class SDATransitFilterSet(NetBoxModelFilterSet):
    transit_type = django_filters.CharFilter(field_name='transit_type', lookup_expr='exact')
    
    class Meta:
        model = SDATransit
        fields = ('id', 'name', 'transit_type', 'fabric_site', 'control_plane_node', 'devices', 'comments')
        
    def search(self, queryset, name, value):
        return queryset.filter(name__icontains=value)

class IPPoolFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = IPPool
        fields = ('id', 'name', 'gateway', 'dhcp_server', 'dns_servers', 'comments')
    
    def search(self, queryset, name, value):
        return queryset.filter(Q(name__icontains=value) | Q(comments__icontains=value))
    
class VirtualNetworkFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = VirtualNetwork
        fields = ('name', 'fabric_site', 'vrf')

    def search(self, queryset, name, value):
        return queryset.filter(name_icontains=value)
