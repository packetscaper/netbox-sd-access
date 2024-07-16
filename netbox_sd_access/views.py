from django.db.models import Count

from netbox.views import generic
from dcim.models import Device
from dcim.tables import DeviceTable
from . import filtersets, forms, models, tables


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