from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel
from django.core.exceptions import ValidationError


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
    
    
    
class SDATransitType(models.TextChoices):
    LISP = 'LISP', 'LISP'
    LISP_BGP = 'LISP-BGP', 'LISP-BGP'   
class SDA_Transit(NetBoxModel):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    transit_type=models.CharField(max_length=8, choices=SDATransitType.choices, default=SDATransitType.LISP, blank=False, null=False)
    fabric_site=models.OneToOneField(to=FabricSite, on_delete=models.PROTECT, blank=True, null=True)
    control_plane_node=models.OneToOneField(to='dcim.Device', on_delete=models.PROTECT, blank=False, related_name="transit_control_nodes")
    devices=models.ManyToManyField(to='dcim.Device', blank=True, related_name="transit_devices")
    
    class Meta:
        ordering = ("name",)
        
    def __str__(self):
        return str(FabricSite) + self.name
    
    def get_absolute_url(self):
        return reverse('plugins:netbox_sd_access:sdatransit', args=[self.pk])
    
    def clean (self):
        if self.transit_type == SDATransitType.LISP and self.devices.count() > 4: 
            raise ValidationError("A maximum of 4 devices are allowed for SDA transit type LISP")
        
        if self.transit_type == SDATransitType.LISP_BGP and self.devices.count() > 2: 
            raise ValidationError("A maximum of 2 devices are allowed for SDA transit type LISP-BGP")
    
        if self.control_plane_node in self.devices.all():
            raise ValidationError("A device in the fabric cannot also be the fabric's control plane node")
        
        fabric_site_devices = self.fabric_site.devices.all()
        for device in self.devices.all():
            if device not in fabric_site_devices:
                raise ValidationError(f"The device {device} is not part of fabric site {self.fabric_site}.")
        
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
class IP_Transit(NetBoxModel):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    fabric_site=models.OneToOneField(to=FabricSite, on_delete=models.PROTECT, blank=True, null=True)
    asn=models.CharField(max_length=200)
    
    class Meta:
        ordering = ("name",)
        
    def __str__(self):
        return str(FabricSite) + self.name
    
    def get_absolute_url(self):
        return reverse('plugins:netbox_sd_access:iptransit', args=[self.pk])