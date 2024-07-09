import django_tables2 as tables
from netbox.tables import NetBoxTable, ChoiceFieldColumn

from .models import *


class SDAccessTable(NetBoxTable):
    name = tables.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = SDAccess
        fields = ("pk", "id", "name", "actions")
        default_columns = ("name",)

class FabricSiteTable(NetBoxTable):
    name = tables.Column(linkify=True)
    
    class Meta(NetBoxTable.Meta):
        model = FabricSite
        fields = ("pk", "id", "name", "physical_site", "location", "ip_prefixes", "device_count", "actions")
        default_columns = ("name", "physical_site", "location", "device_count")
        
class IPTransitTable(NetBoxTable):
    name = tables.Column(linkify=True)
    class Meta(NetBoxTable.Meta):
        model = IPTransit
        fields=("pk", "id", "name", "fabric_site", "asn")
        default_columns=("name", "fabric_site", "asn")
        
class SDATransitTable(NetBoxTable):
    name = tables.Column(linkify=True)
    class Meta(NetBoxTable.Meta):
        model = SDATransit
        fields=("pk", "id", "transit_type", "name", "fabric_site", "control_plane_node", "device_count")
        default_columns=("name", "fabric_site", "transit_type", "")