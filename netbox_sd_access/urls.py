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
    
    path("device-roles/", views.SDADeviceRoleListView.as_view(), name='sdadevicerole_list'),
    path("device-roles/add/", views.SDADeviceRoleEditView.as_view(), name='sdadevicerole_add'),
    path('device-roles/<int:pk>/', views.SDADeviceRoleView.as_view(), name='sdadevicerole'),
    path('device-roles/<int:pk>/edit/', views.SDADeviceRoleEditView.as_view(), name='sdadevicerole_edit'),
    path('device-roles/<int:pk>/delete/', views.SDADeviceRoleDeleteView.as_view(), name='sdadevicerole_delete'),
    path('device-roles/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='sdadevicerole_changelog', 
         kwargs={'model': models.SDADeviceRole}),
)
