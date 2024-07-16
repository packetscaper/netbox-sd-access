from typing import Annotated, List
import strawberry
import strawberry_django
from netbox.graphql.types import NetBoxObjectType
from .. import models
from . import filters

@strawberry_django.type(
    models.FabricSite,
    fields='__all__',
    filters=filters.FabricSiteFilter
)
class FabricSiteType(NetBoxObjectType):
    id: int
    name: str
    physical_site: Annotated["SiteType", strawberry.lazy('dcim.graphql.types')]
    location: Annotated["LocationType", strawberry.lazy('dcim.graphql.types')]
    ip_prefixes: List[Annotated["PrefixType", strawberry.lazy('ipam.graphql.types')]]
    devices: List[Annotated["DeviceType", strawberry.lazy('dcim.graphql.types')]]

class VirtualNetworkType(NetBoxObjectType):
    id: int
    name: str
    fabric_site: FabricSiteType
    vrf: Annotated["VRFType", strawberry.lazy('ipam.graphql.types')]