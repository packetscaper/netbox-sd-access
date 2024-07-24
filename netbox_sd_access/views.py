from django.db.models import Count

from netbox.views import generic
from . import filtersets, forms, models, tables

from dcim.tables import DeviceTable


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
        table = tables.SDADeviceTable(instance.devices.all())
        table.configure(request)
        
        return {
            'devices_table': table,
        }
        
class FabricSiteBulkDeleteView(generic.BulkDeleteView):
    queryset = models.FabricSite.objects.all()
    table = tables.FabricSiteTable
    
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

class FabricSiteImportView(generic.BulkImportView):
    queryset = models.FabricSite.objects.all()
    model_form = forms.FabricSiteImportForm
    
class FabricSiteDeleteView(generic.ObjectDeleteView):
    queryset = models.FabricSite.objects.all()

class VirtualNetworkListView(generic.ObjectListView):
    queryset = models.VirtualNetwork.objects.all()
    table = tables.VirtualNetworkTable

    filterset = filtersets.VirtualNetworkFilterSet
    filterset_form = forms.VirtualNetworkFilterForm

class VirtualNetworkEditView(generic.ObjectEditView):
    queryset = models.VirtualNetwork.objects.all()
    form = forms.VirtualNetworkForm

class VirtualNetworkDeleteView(generic.ObjectDeleteView):
    queryset = models.VirtualNetwork.objects.all()

class VirtualNetworkView(generic.ObjectView):
    queryset = models.VirtualNetwork.objects.all()

class SDADeviceView(generic.ObjectView):
    queryset = models.SDADevice.objects.all()
    
class SDADeviceListView(generic.ObjectListView):
    queryset = models.SDADevice.objects.all()
    table = tables.SDADeviceTable
    filterset = filtersets.SDADeviceFilterSet
    filterset_form = forms.SDADeviceFilterForm

class SDADeviceEditView(generic.ObjectEditView):
    queryset = models.SDADevice.objects.all()
    form = forms.SDADeviceForm

class SDADeviceBulkImportView(generic.BulkImportView):
    queryset = models.SDADevice.objects.all()
    model_form = forms.SDADeviceImportForm

class SDADeviceDeleteView(generic.ObjectDeleteView):
    queryset = models.SDADevice.objects.all()

class SDADeviceBulkDeleteView(generic.BulkDeleteView):
    queryset = models.SDADevice.objects.all()
    table = tables.SDADeviceTable

class IPPoolView(generic.ObjectView):
    queryset = models.IPPool.objects.all()
    
class IPPoolListView(generic.ObjectListView):
    queryset = models.IPPool.objects.all()
    table = tables.IPPoolTable
    filterset = filtersets.IPPoolFilterSet
    filterset_form = forms.IPPoolFilterForm

class IPPoolEditView(generic.ObjectEditView):
    queryset = models.IPPool.objects.all()
    form = forms.IPPoolForm
    
class IPPoolDeleteView(generic.ObjectDeleteView):
    queryset = models.IPPool.objects.all()

class IPPoolBulkDeleteView(generic.BulkDeleteView):
    queryset = models.IPPool.objects.all()
    table = tables.IPPoolTable

class IPPoolBulkImportView(generic.BulkImportView):
    queryset = models.IPPool.objects.all()
    model_form = forms.IPPoolImportForm
    
class IPTransitListView(generic.ObjectListView):
    # qs1 = 
    # qs2 = models.SDATransit.objects.annotate(
    #     device_count=Count('devices')
    # )
    queryset = models.IPTransit.objects.all()
    table = tables.IPTransitTable
    
    filterset = filtersets.IPTransitFilterSet
    filterset_form = forms.IPTransitFilterForm
    
    # def get_extra_context(self, request, instance):
    #     ip_transit_table = tables.IPTransitTable(self.qs1)
    #     sda_transit_table = tables.SDATransitTable(self.qs2)
        
    #     ip_transit_table.configure(request)
    #     sda_transit_table.configure(request)
        
    #     return {
    #         'ip_transit_table': ip_transit_table,
    #         'sda_transit_table': sda_transit_table
    #     }
    
class IPTransitEditView(generic.ObjectEditView):
    queryset = models.IPTransit.objects.all()
    form = forms.IPTransitForm
class IPTransitDeleteView(generic.ObjectDeleteView):
    queryset = models.IPTransit.objects.all()
    
class IPTransitView(generic.ObjectView):
    queryset = models.IPTransit.objects.all()
    
class IPTransitBulkImportView(generic.BulkImportView):
    queryset = models.IPTransit.objects.all()
    model_form = forms.IPTransitImportForm

class IPTransitBulkDeleteView(generic.BulkDeleteView):
    queryset = models.IPTransit.objects.all()
    table = tables.IPTransitTable

    
# class IPTransitBulkDeleteView(generic.BulkDeleteView):
#     queryset = models.IPTransit.objects.all()
#     filterset = filtersets.IPTransitFilterSet
#     table = tables.IPTransitTable
    
class SDATransitListView(generic.ObjectListView):
    queryset = models.SDATransit.objects.annotate(
        device_count = Count('devices')
    )
    table = tables.SDATransitTable
    filterset = filtersets.SDATransitFilterSet
    filterset_form = forms.SDATransitFilterForm
    
class SDATransitEditView(generic.ObjectEditView):
    queryset = models.SDATransit.objects.all()
    form = forms.SDATransitForm
    
class SDATransitDeleteView(generic.ObjectDeleteView):
    queryset = models.SDATransit.objects.all()
    
class SDATransitView(generic.ObjectView):
    queryset = models.SDATransit.objects.all()
    def get_extra_context(self, request, instance):
        table = tables.SDADeviceTable(instance.devices.all())
        table.configure(request)
        
        return {
            'devices_table': table,
        }

class SDATransitBulkImportView(generic.BulkImportView):
    queryset = models.SDATransit.objects.all()
    model_form = forms.SDATransitImportForm

class SDATransitBulkDeleteView(generic.BulkDeleteView):
    queryset = models.SDATransit.objects.all()
    table = tables.SDATransitTable

