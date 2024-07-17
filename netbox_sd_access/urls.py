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
    path('fabric-sites/<int:pk>/', views.FabricSiteView.as_view(), name='fabricsite'),
    path('fabric-sites/<int:pk>/edit/', views.FabricSiteEditView.as_view(), name='fabricsite_edit'),
    path('fabric-sites/<int:pk>/delete/', views.FabricSiteDeleteView.as_view(), name='fabricsite_delete'),
    path('fabric-sites/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='fabricsite_changelog', 
         kwargs={'model': models.FabricSite}),

    #####Virtual Networks
    path("virtual-networks/", views.VirtualNetworkListView.as_view(), name='virtualnetwork_list'),
    path("virtual-networks/add/", views.VirtualNetworkEditView.as_view(), name='virtualnetwork_add'),
    path('virtual-networks/<int:pk>/', views.VirtualNetworkView.as_view(), name='virtualnetwork'),
    path("virtual-networks/<int:pk>/edit", views.VirtualNetworkEditView.as_view, name='virtualnetwork_edit'),
    path('virtual-networks/<int:pk>/delete/', views.VirtualNetworkDeleteView.as_view(), name = "virtualnetwork_delete"),
    path('virtual-networks/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='virtualnetwork_changelog',
        kwargs={'model': models.VirtualNetwork}),

)
