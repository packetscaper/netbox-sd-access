#!/usr/bin/env python

"""Tests for Fabric Site."""

from django.urls import reverse
from rest_framework import status
from django.db.utils import IntegrityError
from django.db.transaction import TransactionManagementError
from psycopg.errors import UniqueViolation

from django.test import TestCase
from utilities.testing import APITestCase, APIViewTestCases

from dcim.models import Site, Location
from ipam.models import Prefix, IPAddress

from netbox_sd_access.models import *

class FabricSiteTestCase(APIViewTestCases.APIViewTestCase):
    model = FabricSite
    view_namespace = 'plugins-api:netbox_sd_access'
    brief_fields = ['device_count', 'display', 'id', 'name', 'url']
    
    @classmethod
    def setUpTestData(cls) -> None:
        site1 = Site.objects.create(name='RTP', slug='rtp')
        location1 = Location.objects.create(name='Building 7', slug='rtp7', site_id=site1.id)
        location1_2 = Location.objects.create(name='Building 8', slug='rtp8', site_id=site1.id)
        location1_3 = Location.objects.create(name='Building 9', slug='rtp9', site_id=site1.id)
        
        prefix1 = Prefix.objects.create(prefix='10.0.0.0/24')
        address1 = IPAddress.objects.create(address='10.0.0.1/24')
        address2 = IPAddress.objects.create(address='10.0.0.2/24')
        
        pool1 = IPPool.objects.create(name='Pool1', prefix=prefix1, gateway=address1, dhcp_server=address1)
        pool1.dns_servers.add(address1)
        pool1.dns_servers.add(address2)
        
        site2 = Site.objects.create(name='San Jose', slug='san-jose')
        location2_1 = Location.objects.create(name='Building 11', slug='sj11', site_id=site2.id)
        location2_2 = Location.objects.create(name='Building 8', slug='sj8', site_id=site2.id)
        prefix2 = Prefix.objects.create(prefix='172.16.0.0/16')
        address3 = IPAddress.objects.create(address='172.16.0.1/16')
        
        pool2 = IPPool.objects.create(name='Pool2', prefix=prefix2, gateway=address3, dhcp_server=address3)
        
        fabricsite_list = [
            FabricSite(name='Fabric Site 1', physical_site=site1, location=location1_3),
            FabricSite(name='Fabric Site 2', physical_site=site2),
            FabricSite(name='Fabric Site 3', physical_site=site1, location=location1)
        ]
        FabricSite.objects.bulk_create(fabricsite_list)
        
        cls.create_data = [
            {
                'name': 'Fabric Site 4',
                'physical_site': site1.id,
                'location': location1_2.id,
                'ip_prefixes': [pool1.id],
            },
            {
                'name': 'Fabric Site 5',
                'physical_site': site1.id,
                'location': None,
                'ip_prefixes': [pool1.id],
            },
            {
                'name': 'Fabric Site 6',
                'physical_site': site2.id,
                'location': location2_1.id,
                'ip_prefixes': [pool1.id, pool2.id]
            }
        ]

class FabricSiteValidationTestCase(TestCase):
    def setUp(self):
        self.site1 = Site.objects.create(name='My Site 1', slug='site-1')
        self.location1 = Location.objects.create(name='Site 1 Building 1', slug='s1b1', site_id=self.site1.id)
        self.fabric_site1 = FabricSite.objects.create(name='Fabric 1', physical_site=self.site1, location=self.location1)
    
    def test_unique_names(self):
        with self.assertRaises(IntegrityError):
            FabricSite.objects.create(name='Fabric 1', physical_site=self.site1)
