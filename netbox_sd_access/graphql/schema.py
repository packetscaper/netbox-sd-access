import strawberry
import strawberry_django
from typing import Annotated
from .. import models
from .types import *

@strawberry.type
class NetBoxSDAQuery:
    @strawberry.field
    def fabric_site(self, id: int) -> FabricSiteType:
        return models.FabricSite.objects.get(pk=id)
    fabric_site_list: list[FabricSiteType] = strawberry_django.field()

    @strawberry.field
    def virtual_network(self, id:int) -> VirtualNetworkType:
        return models.VirtualNetwork.objects.get(pk=id)
    virtual_network_list: list[VirtualNetworkType] = strawberry_django.field()
    
    @strawberry.field
    def ip_transit(self,id:int) -> IPTransitType:
        return models.IPTransit.objects.get(pk=id)
    ip_transit_list: list[IPTransitType] = strawberry_django.field()
    
    @strawberry.field
    def sda_transit(self,id:int) -> SDATransitType:
        return models.SDATransit.objects.get(pk=id)
    sda_transit_list: list[SDATransitType] = strawberry_django.field()

    @strawberry.field
    def sda_device(self, id: int) -> SDADeviceType:
        return models.SDADevice.objects.get(pk=id)
    sda_device_list: list[SDADeviceType] = strawberry_django.field()
    
    @strawberry.field
    def ip_pool(self, id: int) -> IPPoolType:
        return models.IPPool.objects.get(pk=id)
    ip_pool_list: list[IPPoolType] = strawberry_django.field()
