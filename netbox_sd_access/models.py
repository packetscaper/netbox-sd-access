from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet
from django.core.exceptions import ValidationError

import netaddr

class IPPool(NetBoxModel):
    """
    IP Pool model groups existing IP prefix, gateway, DHCP, and DNS server. IP pools are associated with a given fabric site.
    """
    name = models.CharField(max_length=200)
    prefix = models.ForeignKey(to='ipam.Prefix', on_delete=models.PROTECT)
    gateway = models.ForeignKey(to='ipam.IPAddress', on_delete=models.PROTECT)
    dhcp_server = models.ForeignKey(to='ipam.IPAddress', on_delete=models.PROTECT, related_name='dhcp_server')
    dns_servers = models.ManyToManyField(to='ipam.IPAddress', related_name='dns_servers')
    comments = models.TextField(blank=True)
    
    class Meta:
        ordering = ("name",)
        verbose_name = 'IP Pool'
        verbose_name_plural = 'IP Pools'
        constraints = (
            models.UniqueConstraint(
                fields=('name',),
                name='netbox_sd_access_ip_pool_unique_name'
            ),
        )
    
    def get_absolute_url(self):
        return reverse("plugins:netbox_sd_access:ippool", args=[self.pk])
    
    def __str__(self) -> str:
        return self.name
    
    def clean(self):
        """
        Verify that the gateway is in the same subnet as the prefix.
        """
        if netaddr.IPNetwork(self.gateway.address) != self.prefix.prefix:
            raise ValidationError('Gateway must be in the same subnet as prefix.')

    
class FabricSite(NetBoxModel):
    """
    All SD-Access features can be associated with a fabric site. 
    """
    name = models.CharField(max_length=200)
    physical_site = models.ForeignKey(to='dcim.Site', on_delete=models.PROTECT)
    # locations is an optional field for if you make the fabric on a per floor basis
    location = models.OneToOneField(to='dcim.Location', on_delete=models.PROTECT, blank=True, null=True)
    ip_prefixes = models.ManyToManyField(to=IPPool)
    comments = models.TextField(blank=True)
    
    class Meta:
        ordering = ("name",)
        constraints = (
            models.UniqueConstraint(
                fields=('name',),
                name='netbox_sd_access_fabric_site_unique_name'
            ),
        )
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('plugins:netbox_sd_access:fabricsite', args=[self.pk])


class SDADeviceRoleChoices(ChoiceSet):
    """
    Set possible SD device roles
    """
    CHOICES = [
        ('control', 'Control Plane Node', 'blue'),
        ('edge', 'Edge Node', 'red'),
        ('external-border', 'External Border Node', 'yellow'),
        ('internal-border', 'Internal Border Node', 'green'),
        ('l2-border', 'L2 Border Node', 'teal')
    ]
    


class SDATransitTypeChoices(ChoiceSet):
    """
    Set possible SD Transit types
    """
    CHOICES = [
        ('lisp', 'LISP', 'yellow'),
        ('lisp-bgp', 'LISP-BGP', 'green')
    ]
    
class SDADevice(NetBoxModel):
    """
    SD Device assigns existing Netbox device to one of a given set of roles and a Fabric Site. 
    """
    device = models.OneToOneField(to='dcim.Device', on_delete=models.CASCADE, related_name='sda_info')
    role = models.CharField(max_length=50, choices=SDADeviceRoleChoices, blank=True, null=True)
    fabric_site = models.ForeignKey(to=FabricSite, on_delete=models.CASCADE, related_name='devices')
    comments = models.TextField(blank=True)
    
    class Meta:
        ordering = ('fabric_site','device',)
        verbose_name = 'SDA Device'
        verbose_name_plural = 'SDA Devices'
    
    def __str__(self):
        return self.device.name

    def get_absolute_url(self):
        return reverse("plugins:netbox_sd_access:sdadevice", args=[self.pk])
    
    def get_role_color(self):
        return SDADeviceRoleChoices.colors.get(self.role)
    
    def clean(self):
        """
        Fabric site and device must belong to the same site
        """
        if (self.fabric_site.physical_site != self.device.site):
            raise ValidationError('Fabric site and device must belong to the same site and location')
        
        if (self.fabric_site.location):
            device_location = self.device.location
            
            while device_location and device_location != self.fabric_site.location:
                device_location = device_location.parent
            
            if not device_location:
                raise ValidationError('Fabric site and device must belong to the same site and location')
            
    
class SDATransit(NetBoxModel):
    """
    Transit between site and outside network
    """
    name=models.CharField(max_length=200)
    transit_type=models.CharField(max_length=8, choices=SDATransitTypeChoices, default=SDATransitTypeChoices.CHOICES[0], blank=False, null=False)
    fabric_site=models.OneToOneField(to=FabricSite, on_delete=models.PROTECT, blank=True, null=True)
    control_plane_node=models.OneToOneField(to=SDADevice, on_delete=models.PROTECT, blank=False, related_name="transit_control_nodes")
    devices=models.ManyToManyField(to=SDADevice, blank=True, related_name="transit_devices")
    comments=models.TextField(blank=True)
    
    class Meta:
        ordering = ("name",)
        verbose_name = "SDA Transit"
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('plugins:netbox_sd_access:sdatransit', args=[self.pk])
    
    def get_role_color(self):
        return SDATransitTypeChoices.colors.get(self.role)
    

class IPTransit(NetBoxModel):
    """
    Transit between site and outside network using BGP. Applys existing ASN configuration to SDA transit.
    """
    name=models.CharField(max_length=200)
    fabric_site=models.OneToOneField(to=FabricSite, on_delete=models.PROTECT, blank=True, null=True)
    asn=models.OneToOneField(to='ipam.ASN',on_delete=models.PROTECT,null=True, blank=True)
    comments=models.TextField(blank=True)
    
    class Meta:
        ordering = ("name",)
        verbose_name = "IP Transit"
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('plugins:netbox_sd_access:iptransit', args=[self.pk])


class VirtualNetwork(NetBoxModel):
    """
    Virtual Network is VRF for SD-Access. Can contain multiple fabric sites.
    """
    name=models.CharField(max_length=200, default = "Virtual Network")
    #fabric_site=models.ForeignKey(to=FabricSite, on_delete=models.CASCADE, related_name='virtual_networks')
    fabric_site=models.ManyToManyField(to=FabricSite, blank= True,related_name = 'virtual_networks')
    
    vrf=models.OneToOneField(to='ipam.VRF', on_delete = models.PROTECT)

    class Meta:
        ordering = ("name",)
        constraints = (
            models.UniqueConstraint(
                fields=('name',),
                name='netbox_sd_access_vns_unique_name',
            ),
        )
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('plugins:netbox_sd_access:virtualnetwork', args=[self.pk])

