from django.db.models import Count

from netbox.views import generic
from . import filtersets, forms, models, tables

from dcim.tables import DeviceTable


"Views define application logic for each model"

class FabricSiteView(generic.ObjectView):
    """
    Defines the view for the FabricSite model.
    """
    queryset = models.FabricSite.objects.all()
    
    def get_extra_context(self, request, instance):
        """define an additional table of SD devices"""
        table = tables.SDADeviceTable(instance.devices.all())
        table.configure(request)
        
        return {
            'devices_table': table,
        }
        
class FabricSiteBulkDeleteView(generic.BulkDeleteView):
    """
    Defines the bulk delete view for the FabricSite model.
    """
    queryset = models.FabricSite.objects.all()
    table = tables.FabricSiteTable
    
class FabricSiteListView(generic.ObjectListView):
    """
    Defines the list view for the FabricSite model.
    """
    queryset = models.FabricSite.objects.annotate(
        device_count=Count('devices')
    )
    table = tables.FabricSiteTable
    filterset = filtersets.FabricSiteFilterSet
    filterset_form = forms.FabricSiteFilterForm

class FabricSiteEditView(generic.ObjectEditView):
    """
    Defines the edit/create view for the FabricSite model.
    """
    queryset = models.FabricSite.objects.all()
    form = forms.FabricSiteForm

class FabricSiteImportView(generic.BulkImportView):
    """
    Defines the bulk import view for the FabricSite model.
    """
    queryset = models.FabricSite.objects.all()
    model_form = forms.FabricSiteImportForm
    
class FabricSiteDeleteView(generic.ObjectDeleteView):
    """
    Defines the delete view for the FabricSite model.
    """
    queryset = models.FabricSite.objects.all()

class VirtualNetworkListView(generic.ObjectListView):
    """
    Defines the list view for the VirtualNetwork model.
    """
    queryset = models.VirtualNetwork.objects.all()
    table = tables.VirtualNetworkTable

    filterset = filtersets.VirtualNetworkFilterSet
    filterset_form = forms.VirtualNetworkFilterForm

class VirtualNetworkEditView(generic.ObjectEditView):
    """
    Defines the edit/create view for the VirtualNetwork model.
    """
    queryset = models.VirtualNetwork.objects.all()
    form = forms.VirtualNetworkForm

class VirtualNetworkDeleteView(generic.ObjectDeleteView):
    """
    Defines the delete view for the VirtualNetwork model.
    """
    queryset = models.VirtualNetwork.objects.all()

class VirtualNetworkView(generic.ObjectView):
    """
    Defines the view for the VirtualNetwork model.
    """
    queryset = models.VirtualNetwork.objects.all()

class VirtualNetworkImportView(generic.BulkImportView):
    """
    Defines the bulk import view for the VirtualNetwork model.
    """
    queryset = models.VirtualNetwork.objects.all()
    model_form = forms.VirtualNetworkImportForm

class VirtualNetworkBulkDeleteView(generic.BulkDeleteView):
    """
    Defines the bulk delete view for the VirtualNetwork model.
    """
    queryset = models.VirtualNetwork.objects.all()
    table = tables.VirtualNetworkTable

class SDADeviceView(generic.ObjectView):
    """
    Defines the view for the SDADevice model.
    """
    queryset = models.SDADevice.objects.all()
    
class SDADeviceListView(generic.ObjectListView):
    """
    Defines the list view for the SDADevice model.
    """
    queryset = models.SDADevice.objects.all()
    table = tables.SDADeviceTable
    filterset = filtersets.SDADeviceFilterSet
    filterset_form = forms.SDADeviceFilterForm

class SDADeviceEditView(generic.ObjectEditView):
    """
    Defines the edit/create view for the SDADevice model.
    """
    queryset = models.SDADevice.objects.all()
    form = forms.SDADeviceForm

class SDADeviceBulkImportView(generic.BulkImportView):
    """
    Defines the bulk import view for the SDADevice model.
    """
    queryset = models.SDADevice.objects.all()
    model_form = forms.SDADeviceImportForm

class SDADeviceDeleteView(generic.ObjectDeleteView):
    """
    Defines the delete view for the SDADevice model.
    """
    queryset = models.SDADevice.objects.all()

class SDADeviceBulkDeleteView(generic.BulkDeleteView):
    """
    Defines the bulk delete view for the SDADevice model.
    """
    queryset = models.SDADevice.objects.all()
    table = tables.SDADeviceTable

class IPPoolView(generic.ObjectView):
    """
    Defines the view for the IPPool model.
    """
    queryset = models.IPPool.objects.all()
    
class IPPoolListView(generic.ObjectListView):
    """
    Defines the list view for the IPPool model.
    """
    queryset = models.IPPool.objects.all()
    table = tables.IPPoolTable
    filterset = filtersets.IPPoolFilterSet
    filterset_form = forms.IPPoolFilterForm

class IPPoolEditView(generic.ObjectEditView):
    """
    Defines the edit/create view for the IPPool model.
    """
    queryset = models.IPPool.objects.all()
    form = forms.IPPoolForm
    
class IPPoolDeleteView(generic.ObjectDeleteView):
    """
    Defines the delete view for the IPPool model.
    """
    queryset = models.IPPool.objects.all()

class IPPoolBulkDeleteView(generic.BulkDeleteView):
    """
    Defines the bulk delete view for the IPPool model.
    """
    queryset = models.IPPool.objects.all()
    table = tables.IPPoolTable

class IPPoolBulkImportView(generic.BulkImportView):
    """
    Defines the bulk import view for the IPPool model.
    """
    queryset = models.IPPool.objects.all()
    model_form = forms.IPPoolImportForm
    
class IPTransitListView(generic.ObjectListView):
    """
    Defines the list view for the IPTransit model.
    """
    queryset = models.IPTransit.objects.all()
    table = tables.IPTransitTable
    
    filterset = filtersets.IPTransitFilterSet
    filterset_form = forms.IPTransitFilterForm
    
class IPTransitEditView(generic.ObjectEditView):
    """
    Defines the edit/create view for the IPTransit model.
    """
    queryset = models.IPTransit.objects.all()
    form = forms.IPTransitForm

class IPTransitDeleteView(generic.ObjectDeleteView):
    """
    Defines the delete view for the IPTransit model.
    """
    queryset = models.IPTransit.objects.all()
    
class IPTransitView(generic.ObjectView):
    """
    Defines the view for the IPTransit view.
    """
    queryset = models.IPTransit.objects.all()
    
class IPTransitBulkImportView(generic.BulkImportView):
    """
    Defines the bulk import view for the IPTransit model.
    """
    queryset = models.IPTransit.objects.all()
    model_form = forms.IPTransitImportForm

class IPTransitBulkDeleteView(generic.BulkDeleteView):
    """
    Defines the bulk delete view for the IPTransit model.
    """
    queryset = models.IPTransit.objects.all()
    table = tables.IPTransitTable

class SDATransitListView(generic.ObjectListView):
    """
    Defines the list view for the SDATransit model.
    """
    queryset = models.SDATransit.objects.annotate(
        device_count = Count('devices')
    )
    table = tables.SDATransitTable
    filterset = filtersets.SDATransitFilterSet
    filterset_form = forms.SDATransitFilterForm
    
class SDATransitEditView(generic.ObjectEditView):
    """
    Defines the edit/create view for the SDATransit model.
    """
    queryset = models.SDATransit.objects.all()
    form = forms.SDATransitForm
    
class SDATransitDeleteView(generic.ObjectDeleteView):
    """
    Defines the delete view for the SDATransit model.
    """
    queryset = models.SDATransit.objects.all()
    
class SDATransitView(generic.ObjectView):
    """
    Defines the view for the SDATransit model.
    """
    queryset = models.SDATransit.objects.all()
    
    def get_extra_context(self, request, instance):
        """Define extra table of attached SDA devices """
        table = tables.SDADeviceTable(instance.devices.all())
        table.configure(request)
        
        return {
            'devices_table': table,
        }

class SDATransitBulkImportView(generic.BulkImportView):
    """
    Defines the bulk import view from the SDATransit model.
    """
    queryset = models.SDATransit.objects.all()
    model_form = forms.SDATransitImportForm

class SDATransitBulkDeleteView(generic.BulkDeleteView):
    """
    Defines the bulk delete view from the SDATransit model.
    """
    queryset = models.SDATransit.objects.all()
    table = tables.SDATransitTable

