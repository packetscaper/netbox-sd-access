#!/usr/bin/env python

"""Tests for SDA Device."""

from django.urls import reverse
from rest_framework import status
from utilities.testing import APITestCase, APIViewTestCases

from dcim.models import Site, Device, DeviceRole, Manufacturer, DeviceType

from netbox_sd_access.models import *

class SDADeviceTestCase(APIViewTestCases.APIViewTestCase):
    model = SDADevice
    view_namespace = 'plugins-api:netbox_sd_access'
    brief_fields = ['device', 'display', 'fabric_site', 'id', 'role', 'url']
    
    @classmethod
    def setUpTestData(cls) -> None:
        site1 = Site.objects.create(name='RTP', slug='rtp')
        
        manufacturer1 = Manufacturer.objects.create(name='Cisco', slug='cisco')
        device_type1 = DeviceType.objects.create(model='Nexus 9000', slug='cisco-nexus-9k', manufacturer=manufacturer1)
        device_role1 = DeviceRole.objects.create(name='Switch', slug='switch')
        
        fabric_site1 = FabricSite.objects.create(name='Site 1', physical_site=site1)
        
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
                fabric_site=fabric_site1,
                role='control',
            ),
            SDADevice(
                device=devices_list[1],
                fabric_site=fabric_site1,
                role='edge',
            ),
            SDADevice(
                device=devices_list[2],
                fabric_site=fabric_site1,
                role='external-border',
            ),
        ]
        
        SDADevice.objects.bulk_create(sda_devices)
        
        cls.create_data = [
            {
                'device': devices_list[3].id,
                'fabric_site': fabric_site1.id,
                'role': 'internal-border'
            },
            {
                'device': devices_list[4].id,
                'fabric_site': fabric_site1.id,
                'role': 'l2-border'
            },
            {
                'device': devices_list[5].id,
                'fabric_site': fabric_site1.id,
                'role': 'edge'
            },
        ]