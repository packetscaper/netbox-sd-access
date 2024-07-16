from django.db.models import Count

from netbox.views import generic
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
        table = tables.SDADeviceTable(instance.devices.all())
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
    
class SDADeviceDeleteView(generic.ObjectDeleteView):
    queryset = models.SDADevice.objects.all()