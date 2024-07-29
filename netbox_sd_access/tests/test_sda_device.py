#!/usr/bin/env python

"""Tests for SDA Device."""

from django.urls import reverse
from rest_framework import status

from django.test import TestCase
from utilities.testing import APITestCase, APIViewTestCases

from dcim.models import Site, Location, Device, DeviceRole, Manufacturer, DeviceType

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

class SDADeviceValidationTestCase(TestCase):
    def setUp(self):
        self.site1 = Site.objects.create(name='RTP', slug='rtp')
        self.site2 = Site.objects.create(name='San Jose', slug='sj')
        self.location1_1 = Location.objects.create(name='RTP Building 7', slug='rtp7', site=self.site1)
        self.location1_1_1 = Location.objects.create(
            name='RTP Building 7 Floor 4',
            slug='rtp7-4',
            parent=self.location1_1,
            site=self.site1
        )
        self.location1_2 = Location.objects.create(name='RTP Building 8', slug='rtp8', site=self.site1)
        
        self.location2_1 = Location.objects.create(name='Building 11', slug='sj11', site=self.site2)
        
        manufacturer1 = Manufacturer.objects.create(name='Cisco', slug='cisco')
        self.device_type1 = DeviceType.objects.create(model='Nexus 9000', slug='cisco-nexus-9k', manufacturer=manufacturer1)
        self.device_role1 = DeviceRole.objects.create(name='Switch', slug='switch')
        
        self.fabric_site1 = FabricSite.objects.create(name='Site 1', physical_site=self.site1)
        
        self.device1 = Device.objects.create(
            name='SW1',
            role=self.device_role1,
            device_type=self.device_type1,
            site=self.site1
        )
        
        self.sdadevice1 = SDADevice.objects.create(device=self.device1, fabric_site=self.fabric_site1, role='control')
        
        self.fabricsite2 = FabricSite.objects.create(
            name='Site 2',
            physical_site=self.site1,
            location=self.location1_1
        )
    
    def test_different_site(self):
        """
        Test error if fabric site and device belong to different sites
        """
        device2 = Device.objects.create(
            name='SW2',
            role=self.device_role1,
            device_type=self.device_type1,
            site=self.site2
        )
        sdadevice = SDADevice(device=device2, fabric_site=self.fabric_site1, role='external-border')
        self.assertRaises(ValidationError, sdadevice.full_clean)
    
    def test_different_location_1(self):
        """
        Test error if fabric site and device in separate locations
        """
        device3 = Device.objects.create(
            name='SW3',
            role=self.device_role1,
            device_type=self.device_type1,
            site=self.site1,
            location=self.location2_1
        )
        sdadevice = SDADevice(device=device3, fabric_site=self.fabricsite2, role='edge')
        self.assertRaises(ValidationError, sdadevice.full_clean)
    
    def test_sub_location_1(self):
        """
        Test valid if device belongs to a sub-location of fabric site
        """
        device4 = Device.objects.create(
            name='SW4',
            role=self.device_role1,
            device_type=self.device_type1,
            site=self.site1,
            location=self.location1_1_1
        )
        sdadevice4 = SDADevice.objects.create(device=device4, fabric_site=self.fabricsite2, role='internal-border')
        self.assertEqual(sdadevice4.device.name,'SW4')
    
    def test_sub_location_2(self):
        """
        Test error if fabric site belongs to sub-location of device location
        """
        fabricsite3 = FabricSite.objects.create(
            name='Site 3',
            physical_site=self.site1,
            location=self.location1_1_1
        )
        device5 = Device.objects.create(
            name='SW5',
            role=self.device_role1,
            device_type=self.device_type1,
            site=self.site1,
            location=self.location1_1
        )
        sdadevice = SDADevice(device=device5, fabric_site=fabricsite3, role='l2-border')
        self.assertRaises(ValidationError, sdadevice.full_clean)
    
    def test_sub_location_3(self):
        """
        Test valid if fabric site has no location but device has a location
        """
        device6 = Device.objects.create(
            name='SW6',
            role=self.device_role1,
            device_type=self.device_type1,
            site=self.site1,
            location=self.location1_1
        )
        sdadevice6 = SDADevice.objects.create(device=device6, fabric_site=self.fabric_site1, role='control')
        self.assertEqual(sdadevice6.fabric_site.name, 'Site 1')
    
    def test_sub_location_4(self):
        """
        Test error if device has no location but fabric site has a location
        """
        device7 = Device.objects.create(
            name='SW7',
            role=self.device_role1,
            device_type=self.device_type1,
            site=self.site1,
        )
        sdadevice = SDADevice(device=device7, fabric_site=self.fabricsite2, role='control')
        self.assertRaises(ValidationError, sdadevice.full_clean)
    
    def test_same_location(self):
        """
        Test valid if both have same location
        """
        device8 = Device.objects.create(
            name='SW8',
            role=self.device_role1,
            device_type=self.device_type1,
            site=self.site1,
            location=self.location1_1
        )
        sdadevice8 = SDADevice.objects.create(device=device8, fabric_site=self.fabricsite2)
        self.assertEqual(sdadevice8.device.location.name, 'RTP Building 7')