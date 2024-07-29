import django_filters
from django.db.models import Q
from netbox.filtersets import NetBoxModelFilterSet
from .models import *
from dcim.models import Site


"""Filtersets are used in query parameters and API calls. Visibly used in filter tabs. """

class FabricSiteFilterSet(NetBoxModelFilterSet):
    """
    Filter set for Fabric Sites.
    Allows filtering by ID, name, physical site, location, and IP Pool, as well as searching by name or comments.
    """
    class Meta:
        model = FabricSite
        fields = ('id', 'name', 'physical_site', 'location', 'ip_prefixes', 'comments')
    
    def search(self, queryset, name, value):
        return queryset.filter(Q(name__icontains=value) | Q(comments__icontains=value))

class SDADeviceFilterSet(NetBoxModelFilterSet):
    """
    Filter set for SDA Devices.
    Allows filtering by ID, role, and fabric site, as well as searching by comments or device name.
    """
    role = django_filters.CharFilter(field_name='role', lookup_expr='exact')

    class Meta:
        model = SDADevice
        fields = ('id', 'role','fabric_site')
    
    def search(self, queryset, name, value):
        return queryset.filter(Q(comments__icontains=value) | Q(device__name__icontains=value))
    

class IPTransitFilterSet(NetBoxModelFilterSet):
    """
    Filter set for IP Transits.
    Allows filtering by id, name, fabric site, ASN, and comments, as well as searching by name or comments.
    """
    class Meta:
        model = IPTransit
        fields = ('id', 'name', 'fabric_site', 'asn', 'comments')
        
    def search(self, queryset, name, value):
        return queryset.filter(Q(name__icontains=value) | Q(comments__icontains=value))

class SDATransitFilterSet(NetBoxModelFilterSet):
    """
    Filter set for SDA Transits.
    Allows filtering by id, name, transit type, fabric site, control plane node, and devices 
    as well as searching by name or comments.
    """
    transit_type = django_filters.CharFilter(field_name='transit_type', lookup_expr='exact')
    
    class Meta:
        model = SDATransit
        fields = ('id', 'name', 'transit_type', 'fabric_site', 'control_plane_node', 'devices', 'comments')
        
    def search(self, queryset, name, value):
        return queryset.filter(Q(name__icontains=value) | Q(comments__icontains=value))

class IPPoolFilterSet(NetBoxModelFilterSet):
    """
    Filter set for IP Pools.
    Allows filtering by ID, name, gateway, DHCP server, and DNS servers, as well as searching by name or comments.
    """
    class Meta:
        model = IPPool
        fields = ('id', 'name', 'gateway', 'dhcp_server', 'dns_servers', 'comments')
    
    def search(self, queryset, name, value):
        return queryset.filter(Q(name__icontains=value) | Q(comments__icontains=value))
    
class VirtualNetworkFilterSet(NetBoxModelFilterSet):
    """
    Filter set for Virtual Networks.
    Allows filtering by name, fabric site, and VRF, as well as searching by name.
    """

    class Meta:
        model = VirtualNetwork
        fields = ('id', 'name', 'fabric_site', 'vrf')

    def search(self, queryset, name, value):
        return queryset.filter(name_icontains=value)
