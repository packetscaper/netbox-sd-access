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
    
schema = [Query]