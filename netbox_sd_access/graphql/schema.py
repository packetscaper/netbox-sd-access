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
    def sdadevice(self, id: int) -> SDADeviceType:
        return models.SDADevice.objects.get(pk=id)
    sdadevice_list: list[SDADeviceType] = strawberry_django.field()
    
schema = [Query]