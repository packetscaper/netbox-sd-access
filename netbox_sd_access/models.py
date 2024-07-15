from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel


class SDAccess(NetBoxModel):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:netbox_sd_access:sdaccess", args=[self.pk])

class FabricSite(NetBoxModel):
    name = models.CharField(max_length=200)
    physical_site = models.ForeignKey(to='dcim.Site', on_delete=models.PROTECT)
    # locations is an optional field for if you make the fabric on a per floor basis
    location = models.OneToOneField(to='dcim.Location', on_delete=models.PROTECT, blank=True, null=True)
    ip_prefixes = models.ManyToManyField(to='ipam.Prefix')
    devices = models.ManyToManyField(to='dcim.Device', blank=True)
    
    class Meta:
        ordering = ("name",)
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('plugins:netbox_sd_access:fabricsite', args=[self.pk])
    

# class VirtualNetworkType(models.TextChoices):
#     VN3 = 'Layer 3 Virtual Network'
#     VN2 = 'Layer 2 Virutal Network'
class LayerThreeVirtualNetwork(NetBoxModel):
    name=models.CharField(max_length=200)
    fabric_site=models.ManyToManyField(to=FabricSite, on_delete=models.PROTECT, blank=True, null=True)
    vrf=models.OneToOneField(to='ipam.VRF', blank = True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('plugins:netbox-sd-access:virtualnetwork', args=[self.pk])

