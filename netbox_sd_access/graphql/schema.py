import strawberry
import strawberry_django
from typing import Annotated
from .. import models
from .types import *

@strawberry.type
class Query:
    @strawberry.field
    def fabricsite(self, id: int) -> FabricSiteType:
        return models.FabricSite.objects.get(pk=id)
    fabricsite_list: list[FabricSiteType] = strawberry_django.field()

    @strawberry.field
    def virtualnetwork(self, id:int) -> VirtualNetworkType:
        return models.VirtualNetwork.objects.get(pk=id)
    virtualnetwork_list: list[VirtualNetworkType] = strawberry_django.field()
    
    @strawberry.field
    def iptransit(self,id:int) -> IPTransitType:
        return models.IPTransit.objects.get(pk=id)
    iptransit_list: list[IPTransitType] = strawberry_django.field()
    
    @strawberry.field
    def sdatransit(self,id:int) -> SDATransitType:
        return models.SDATransit.objects.get(pk=id)
    sdatransit_list: list[SDATransitType] = strawberry_django.field()

    @strawberry.field
    def sdadevice(self, id: int) -> SDADeviceType:
        return models.SDADevice.objects.get(pk=id)
    sdadevice_list: list[SDADeviceType] = strawberry_django.field()
    
    @strawberry.field
    def ippool(self, id: int) -> IPPoolType:
        return models.IPPool.objects.get(pk=id)
    ippool_list: list[IPPoolType] = strawberry_django.field()
    
schema = [Query]