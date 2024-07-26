#!/usr/bin/env python

"""Tests for `netbox_sd_access` package."""

from django.urls import reverse
from rest_framework import status
from utilities.testing import APITestCase, APIViewTestCases

from dcim.models import Site, Location, Device, DeviceRole, Manufacturer, DeviceType
from ipam.models import Prefix, IPAddress

from netbox_sd_access.models import *

class SDTransitTestCase(APIViewTestCases.APIViewTestCase):
    model = SDATransit
    view_namespace = 'plugins-api:netbox_sd_access'
    brief_fields = ['control_plane_node', 'display', 'fabric_site', 'id', 'name', 'transit_type', 'url']
    
    @classmethod
    def setUpTestData(cls) -> None:
        site1 = Site.objects.create(name='RTP', slug='rtp')
        
        fabricsite_list = [
            FabricSite(name='Fabric Site 1', physical_site=site1),
            FabricSite(name='Fabric Site 2', physical_site=site1),
            FabricSite(name='Fabric Site 3', physical_site=site1),
            FabricSite(name='Fabric Site 4', physical_site=site1),
            FabricSite(name='Fabric Site 5', physical_site=site1),
            FabricSite(name='Fabric Site 6', physical_site=site1)
        ]
        FabricSite.objects.bulk_create(fabricsite_list)
        
        manufacturer1 = Manufacturer.objects.create(name='Cisco', slug='cisco')
        device_type1 = DeviceType.objects.create(model='Nexus 9000', slug='cisco-nexus-9k', manufacturer=manufacturer1)
        device_role1 = DeviceRole.objects.create(name='Switch', slug='switch')
        
        devices_list: list[Device] = []
        
        for i in range(6):
            devices_list.append(Device.objects.create(
                name=f'SW{i + 1}',
                role=device_role1,
                site=site1,
                device_type=device_type1,
            ))
        
        sda_devices = [
            SDADevice(
                device=devices_list[0],
                fabric_site=fabricsite_list[0],
                role='control',
            ),
            SDADevice(
                device=devices_list[1],
                fabric_site=fabricsite_list[1],
                role='edge',
            ),
            SDADevice(
                device=devices_list[2],
                fabric_site=fabricsite_list[2],
                role='external-border',
            ),
            SDADevice(
                device=devices_list[3],
                fabric_site=fabricsite_list[3],
                role='control',
            ),
            SDADevice(
                device=devices_list[4],
                fabric_site=fabricsite_list[4],
                role='edge',
            ),
            SDADevice(
                device=devices_list[5],
                fabric_site=fabricsite_list[5],
                role='external-border',
            ),
        ]
        
        SDADevice.objects.bulk_create(sda_devices)
        
        sda_transits = [
            SDATransit(
                control_plane_node=sda_devices[0],
                fabric_site=fabricsite_list[0],
                transit_type='lisp'
            ),
            SDATransit(
                control_plane_node=sda_devices[1],
                fabric_site=fabricsite_list[1],
                transit_type='lisp-bgp'
            ),
            SDATransit(
                control_plane_node=sda_devices[2],
                fabric_site=fabricsite_list[2],
                transit_type='lisp'
            ),
        ]
        
        SDATransit.objects.bulk_create(sda_transits)
        
        cls.create_data = [
            {
                'name': 'SDTransit 4',
                'transit_type': 'lisp',
                'fabric_site': fabricsite_list[3].id,
                'control_plane_node': sda_devices[3].id,
            },
            {
                'name': 'SDTransit 5',
                'transit_type': 'lisp-bgp',
                'fabric_site': fabricsite_list[4].id,
                'control_plane_node': sda_devices[4].id,
            },
            {
            
                'name': 'SDTransit 6',
                'transit_type': 'lisp',
                'fabric_site': fabricsite_list[5].id,
                'control_plane_node': sda_devices[5].id,
            }
        ]