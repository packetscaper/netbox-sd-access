import django_tables2 as tables
from netbox.tables import NetBoxTable, ChoiceFieldColumn

from .models import *

"""Define what information is displayed in table for a model instance"""

class FabricSiteTable(NetBoxTable):
    """
    Defines table view for Fabric Sites.
    """
    name = tables.Column(linkify=True)
    
    class Meta(NetBoxTable.Meta):
        model = FabricSite
        fields = ("pk", "id", "name", "physical_site", "location", "ip_prefixes", "device_count", "actions")
        default_columns = ("name", "physical_site", "location", "device_count")

class VirtualNetworkTable(NetBoxTable):
    """
    Defines table view for Virtual Networks.
    """
    name = tables.Column(linkify=True)
    class Meta(NetBoxTable.Meta):
        model = VirtualNetwork   
        fields= ("pk", "id", "fabric_site", "name", "vrf", "actions")  
        default_columns=("name","fabric_site","vrf")   

class SDADeviceTable(NetBoxTable):
    """
    Defines table view for SDA Devices.
    """
    id = tables.Column(linkify=True)
    device = tables.Column(linkify=True)
    fabric_site = tables.Column(linkify=True)
    role = ChoiceFieldColumn()
    
    class Meta(NetBoxTable.Meta):
        model = SDADevice
        fields = ('pk', 'id', 'device', 'role', 'fabric_site', 'actions')
        default_columns = ('id', 'device', 'role', 'fabric_site')
        
class IPPoolTable(NetBoxTable):
    """
    Defines table view for IP Pools.
    """
    name = tables.Column(linkify=True)
    
    class Meta(NetBoxTable.Meta):
        model = IPPool
        fields = ("pk", "id", "name", "prefix", "gateway", "dhcp_server", "dns_servers", "actions")
        default_columns = ("name", "prefix", "gateway")

class IPTransitTable(NetBoxTable):
    """
    Defines table view for IP Transits.
    """
    name = tables.Column(linkify=True)
    fabric_site = tables.Column(linkify=True)
    asn = tables.Column(linkify=True)
    class Meta(NetBoxTable.Meta):
        model = IPTransit
        fields=("pk", "id", "name", "fabric_site", "asn", "actions")
        default_columns=("name", "fabric_site", "asn")
        
class SDATransitTable(NetBoxTable):
    """
    Defines table view for SDA Transits.
    """
    name = tables.Column(linkify=True)
    transit_type = ChoiceFieldColumn()
    fabric_site = tables.Column(linkify=True)
    control_plane_node = tables.Column(linkify=True)
    class Meta(NetBoxTable.Meta):
        model = SDATransit
        fields=("pk", "id", "transit_type", "name", "fabric_site", "control_plane_node", "device_count", "actions")
        default_columns=("name", "fabric_site", "transit_type", "device_count", "control_plane_node")