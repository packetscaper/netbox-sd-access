import django_filters
from netbox.filtersets import NetBoxModelFilterSet
from .models import *
from dcim.models import Site
from django.db.models import F

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

class SDADeviceRoleFilterSet(NetBoxModelFilterSet):
    role = django_filters.CharFilter(field_name='role', lookup_expr='exact')
    site = django_filters.NumberFilter(method='filter_location')
    
    class Meta:
        model = SDADeviceRole
        fields = ('role','site',)
        fields = ('role',)
    
    def filter_location(self, queryset, name, value):
        print(value)
        print(type(value))
        queryset = queryset.annotate(site_id=F('device__site__id'))
        queryset = queryset.filter(site_id=value)
        return queryset