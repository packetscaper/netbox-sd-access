from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet


class SDAccess(NetBoxModel):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:netbox_sd_access:sdaccess", args=[self.pk])
    
class IPPool(NetBoxModel):
    name = models.CharField(max_length=200)
    prefix = models.ForeignKey(to='ipam.Prefix', on_delete=models.PROTECT)
    gateway = models.ForeignKey(to='ipam.IPAddress', on_delete=models.PROTECT)
    dhcp_server = models.ForeignKey(to='ipam.IPAddress', on_delete=models.PROTECT, related_name='dhcp_server')
    dns_servers = models.ManyToManyField(to='ipam.IPAddress', related_name='dns_servers')
    
    class Meta:
        ordering = ("name",)
        verbose_name = 'IP Pool'
        verbose_name_plural = 'IP Pools'
    
    def get_absolute_url(self):
        return reverse("plugins:netbox_sd_access:ippool", args=[self.pk])
    
    def __str__(self) -> str:
        return self.name
    
class FabricSite(NetBoxModel):
    name = models.CharField(max_length=200)
    physical_site = models.ForeignKey(to='dcim.Site', on_delete=models.PROTECT)
    # locations is an optional field for if you make the fabric on a per floor basis
    location = models.OneToOneField(to='dcim.Location', on_delete=models.PROTECT, blank=True, null=True)
    ip_prefixes = models.ManyToManyField(to=IPPool)
    
    class Meta:
        ordering = ("name",)
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('plugins:netbox_sd_access:fabricsite', args=[self.pk])


class SDADeviceRoleChoices(ChoiceSet):
    
    CHOICES = [
        ('control', 'Control Plane Node', 'blue'),
        ('edge', 'Edge Node', 'red'),
        ('external-border', 'External Border Node', 'yellow'),
        ('internal-border', 'Internal Border Node', 'green'),
        ('l2-border', 'L2 Border Node', 'teal')
    ]
    
class SDADevice(NetBoxModel):
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
