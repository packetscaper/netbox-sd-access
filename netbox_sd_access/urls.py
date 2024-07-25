from django.urls import path
from netbox.views.generic import ObjectChangeLogView

from . import models, views


urlpatterns = (
    # path("sd-accesss/", views.SDAccessListView.as_view(), name="sdaccess_list"),
    # path("sd-accesss/add/", views.SDAccessEditView.as_view(), name="sdaccess_add"),
    # path("sd-accesss/<int:pk>/", views.SDAccessView.as_view(), name="sdaccess"),
    # path("sd-accesss/<int:pk>/edit/", views.SDAccessEditView.as_view(), name="sdaccess_edit"),
    # path("sd-accesss/<int:pk>/delete/", views.SDAccessDeleteView.as_view(), name="sdaccess_delete"),
    # path(
    #     "sd-accesss/<int:pk>/changelog/",
    #     ObjectChangeLogView.as_view(),
    #     name="sdaccess_changelog",
    #     kwargs={"model": models.SDAccess},
    # ),
    
    path("fabric-sites/", views.FabricSiteListView.as_view(), name='fabricsite_list'),
    path("fabric-sites/add/", views.FabricSiteEditView.as_view(), name='fabricsite_add'),
    path('fabric-sites/import/', views.FabricSiteImportView.as_view(), name='fabricsite_import'),
    path('fabric-sites/delete/', views.FabricSiteBulkDeleteView.as_view(), name='fabricsite_bulk_delete'),
    path('fabric-sites/<int:pk>/', views.FabricSiteView.as_view(), name='fabricsite'),
    path('fabric-sites/<int:pk>/edit/', views.FabricSiteEditView.as_view(), name='fabricsite_edit'),
    path('fabric-sites/<int:pk>/delete/', views.FabricSiteDeleteView.as_view(), name='fabricsite_delete'),
    path('fabric-sites/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='fabricsite_changelog', 
         kwargs={'model': models.FabricSite}),

    #####Virtual Networks
    path("virtual-networks/", views.VirtualNetworkListView.as_view(), name='virtualnetwork_list'),
    path("virtual-networks/add/", views.VirtualNetworkEditView.as_view(), name='virtualnetwork_add'),
    path("virtual-networks/import/", views.VirtualNetworkImportView.as_view(), name='virtualnetwork_import'),
    path("virtual-networks/delete/", views.VirtualNetworkBulkDeleteView.as_view(), name='virtualnetwork_bulk_delete'),
    path('virtual-networks/<int:pk>/', views.VirtualNetworkView.as_view(), name='virtualnetwork'),
    path("virtual-networks/<int:pk>/edit/", views.VirtualNetworkEditView.as_view(), name='virtualnetwork_edit'),
    path('virtual-networks/<int:pk>/delete/', views.VirtualNetworkDeleteView.as_view(), name = "virtualnetwork_delete"),
    path('virtual-networks/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='virtualnetwork_changelog',
         kwargs={'model': models.VirtualNetwork}),
    
    #### TRANSITS
    path("ip-transits/", views.IPTransitListView.as_view(), name='iptransit_list'),
    path("ip-transits/add/", views.IPTransitEditView.as_view(), name='iptransit_add'),
    path('ip-transits/<int:pk>/', views.IPTransitView.as_view(), name='iptransit'),
    path('ip-transits/<int:pk>/edit/', views.IPTransitEditView.as_view(), name='iptransit_edit'),
    path('ip-transits/<int:pk>/delete/', views.IPTransitDeleteView.as_view(), name='iptransit_delete'),
    path('ip-transits/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='iptransit_changelog', 
         kwargs={'model': models.IPTransit}),
    path('ip-transits/import/', views.IPTransitBulkImportView.as_view(), name='iptransit_import'),
    path('ip-transits/delete/', views.IPTransitBulkDeleteView.as_view(), name='iptransit_bulk_delete'),
        
    path("sda-transits/", views.SDATransitListView.as_view(), name='sdatransit_list'),
    path("sda-transits/add/", views.SDATransitEditView.as_view(), name='sdatransit_add'),
    path('sda-transits/<int:pk>/', views.SDATransitView.as_view(), name='sdatransit'),
    path('sda-transits/<int:pk>/edit/', views.SDATransitEditView.as_view(), name='sdatransit_edit'),
    path('sda-transits/<int:pk>/delete/', views.SDATransitDeleteView.as_view(), name='sdatransit_delete'),
    path('sda-transits/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='sdatransit_changelog', 
         kwargs={'model': models.SDATransit}),
    path('sda-transits/import/', views.SDATransitBulkImportView.as_view(), name='sdatransit_import'),
    path('sda-transits/delete/', views.SDATransitBulkDeleteView.as_view(), name='sdatransit_bulk_delete'),
    
    #### SDA Devices
    path("sda-devices/", views.SDADeviceListView.as_view(), name='sdadevice_list'),
    path("sda-devices/add/", views.SDADeviceEditView.as_view(), name='sdadevice_add'),
    path('sda-devices/import/', views.SDADeviceBulkImportView.as_view(), name='sdadevice_import'),
    path('sda-device/delete/', views.SDADeviceBulkDeleteView.as_view(), name='sdadevice_bulk_delete'),
    path('sda-devices/<int:pk>/', views.SDADeviceView.as_view(), name='sdadevice'),
    path('sda-devices/<int:pk>/edit/', views.SDADeviceEditView.as_view(), name='sdadevice_edit'),
    path('sda-devices/<int:pk>/delete/', views.SDADeviceDeleteView.as_view(), name='sdadevice_delete'),
    path('sda-devices/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='sdadevice_changelog', 
         kwargs={'model': models.SDADevice}),

    #### IP Pools
    path("ip-pools/", views.IPPoolListView.as_view(), name='ippool_list'),
    path("ip-pools/add/", views.IPPoolEditView.as_view(), name='ippool_add'),
    path("ip-pools/import/", views.IPPoolBulkImportView.as_view(), name='ippool_import'),
    path('ip-pools/delete/', views.IPPoolBulkDeleteView.as_view(), name='ippool_bulk_delete'),
    path('ip-pools/<int:pk>/', views.IPPoolView.as_view(), name='ippool'),
    path('ip-pools/<int:pk>/edit/', views.IPPoolEditView.as_view(), name='ippool_edit'),
    path('ip-pools/<int:pk>/delete/', views.IPPoolDeleteView.as_view(), name='ippool_delete'),
    path('ip-pools/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='ippool_changelog', 
         kwargs={'model': models.IPPool}),
)
