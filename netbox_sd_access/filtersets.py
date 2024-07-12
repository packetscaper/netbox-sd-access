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

class IPPoolFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = IPPool
        fields = ('id', 'name', 'gateway', 'dhcp_server', 'dns_servers')
    
    def search(self, queryset, name, value):
        return queryset.filter(name__itcontains=value)