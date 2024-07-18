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