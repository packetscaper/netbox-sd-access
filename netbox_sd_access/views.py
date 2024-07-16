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

class SDADeviceRoleView(generic.ObjectView):
    queryset = models.SDADeviceRole.objects.all()
    
class SDADeviceRoleListView(generic.ObjectListView):
    queryset = models.SDADeviceRole.objects.all()
    table = tables.SDADeviceRoleTable
    filterset = filtersets.SDADeviceRoleFilterSet
    filterset_form = forms.SDADeviceRoleFilterForm

class SDADeviceRoleEditView(generic.ObjectEditView):
    queryset = models.SDADeviceRole.objects.all()
    form = forms.SDADeviceRoleForm
    
class SDADeviceRoleDeleteView(generic.ObjectDeleteView):
    queryset = models.SDADeviceRole.objects.all()