from django.db.models import Count
from django.shortcuts import render
from netbox.views import generic
from dcim.models import Device
from dcim.tables import DeviceTable
from . import filtersets, forms, models, tables
from django_tables2 import RequestConfig


class SDAccessView(generic.ObjectView):
    queryset = models.SDAccess.objects.all()


class SDAccessListView(generic.ObjectListView):
    queryset = models.SDAccess.objects.all()
    table = tables.SDAccessTable


class SDAccessEditView(generic.ObjectEditView):
    queryset = models.SDAccess.objects.all()
    form = forms.SDAccessForm


class SDAccessDeleteView(generic.ObjectDeleteView):
    queryset = models.SDAccess.objects.all()

class FabricSiteView(generic.ObjectView):
    queryset = models.FabricSite.objects.all()
    
    def get_extra_context(self, request, instance):
        table = DeviceTable(instance.devices.all())
        table.configure(request)
        
        return {
            'devices_table': table,
        }
    
class FabricSiteListView(generic.ObjectListView):
    queryset = models.FabricSite.objects.annotate(
        device_count=Count('devices')
    )
    table = tables.FabricSiteTable
    filterset = filtersets.FabricSiteFilterSet
    filterset_form = forms.FabricSiteFilterForm

class FabricSiteEditView(generic.ObjectEditView):
    queryset = models.FabricSite.objects.all()
    form = forms.FabricSiteForm
    
class FabricSiteDeleteView(generic.ObjectDeleteView):
    queryset = models.FabricSite.objects.all()
    
class IPTransitListView(generic.ObjectListView):
    # qs1 = 
    # qs2 = models.SDATransit.objects.annotate(
    #     device_count=Count('devices')
    # )
    queryset = models.IPTransit.objects.all()
    table = tables.IPTransitTable
    
    # def get_extra_context(self, request, instance):
    #     ip_transit_table = tables.IPTransitTable(self.qs1)
    #     sda_transit_table = tables.SDATransitTable(self.qs2)
        
    #     ip_transit_table.configure(request)
    #     sda_transit_table.configure(request)
        
    #     return {
    #         'ip_transit_table': ip_transit_table,
    #         'sda_transit_table': sda_transit_table
    #     }
    
    
class SDATransitListView(generic.ObjectListView):
    
    queryset = models.SDATransit.objects.annotate(
        device_count = Count('devices')
    )
    table = tables.SDATransitTable