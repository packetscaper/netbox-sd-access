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


class SDADeviceRoleChoices(ChoiceSet):
    
    CHOICES = [
        ('control', 'Control Plane Node', 'gray'),
        ('edge', 'Edge Node', 'red'),
        ('external-border', 'External Border Node', 'yellow'),
        ('internal-border', 'Internal Border Node', 'green'),
        ('l2-border', 'L2 Border Node', 'white')
    ]
    
class SDADeviceRole(NetBoxModel):
    device = models.OneToOneField(to='dcim.Device', on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=SDADeviceRoleChoices)
    
    class Meta:
        ordering = ('id',)
        verbose_name = 'Device Role'
        verbose_name_plural = 'Device Roles'
    
    def __str__(self):
        return self.device.name

    def get_absolute_url(self):
        return reverse("plugins:netbox_sd_access:sdadevicerole", args=[self.pk])
    
    def get_role_color(self):
        return SDADeviceRoleChoices.colors.get(self.role)
    

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