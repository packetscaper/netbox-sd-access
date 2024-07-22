import strawberry
import strawberry_django
from .. import filtersets, models
from netbox.graphql.filter_mixins import autotype_decorator, BaseFilterMixin

__all__ = (
    'FabricSiteFilter',
    'SDADeviceFilter',
    'IPTransitFilter',
    'SDATransitFilter',
    'IPPoolFilter',
    'VirtualNetworkFilter'
)

@strawberry_django.filter(models.FabricSite, lookups=True)
@autotype_decorator(filtersets.FabricSiteFilterSet)
class FabricSiteFilter(BaseFilterMixin):
    pass

@strawberry_django.filter(models.SDADevice, lookups=True)
@autotype_decorator(filtersets.SDADeviceFilterSet)
class SDADeviceFilter(BaseFilterMixin):
    pass

@strawberry_django.filter(models.IPTransit, lookups=True)
@autotype_decorator(filtersets.IPTransitFilterSet)
class IPTransitFilter(BaseFilterMixin):
    pass

@strawberry_django.filter(models.SDATransit, lookups=True)
@autotype_decorator(filtersets.SDATransitFilterSet)
class SDATransitFilter(BaseFilterMixin):
    pass

@strawberry_django.filter(models.IPPool, lookups=True)
@autotype_decorator(filtersets.IPPoolFilterSet)
class IPPoolFilter(BaseFilterMixin):
    pass

@strawberry_django.filter(models.VirtualNetwork, lookups = True)
@autotype_decorator(filtersets.VirtualNetworkFilterSet)
class VirtualNetworkFilter(BaseFilterMixin):
    pass