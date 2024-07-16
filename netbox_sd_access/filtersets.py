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
        fields = ('id', 'name', 'physical_site', 'location', 'ip_prefixes')
    
    def search(self, queryset, name, value):
        return queryset.filter(name__icontains=value)

class SDADeviceFilterSet(NetBoxModelFilterSet):
    role = django_filters.CharFilter(field_name='role', lookup_expr='exact')
    
    class Meta:
        model = SDADevice
        fields = ('role','fabric_site',)
    
    def search(self, queryset, name, value):
        return queryset.filter(comments__icontains=value)