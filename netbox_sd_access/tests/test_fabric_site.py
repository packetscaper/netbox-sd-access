#!/usr/bin/env python

"""Tests for `netbox_sd_access` package."""

from django.urls import reverse
from rest_framework import status
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
        
        prefix1 = Prefix.objects.create(prefix='10.0.0.0/24')
        address1 = IPAddress.objects.create(address='10.0.0.1/24')
        address2 = IPAddress.objects.create(address='10.0.0.2/24')
        
        pool1 = IPPool.objects.create(prefix=prefix1, gateway=address1, dhcp_server=address1)
        pool1.dns_servers.add(address1)
        pool1.dns_servers.add(address2)
        
        site2 = Site.objects.create(name='San Jose', slug='san-jose')
        prefix2 = Prefix.objects.create(prefix='172.16.0.0/16')
        address3 = IPAddress.objects.create(address='172.16.0.1/16')
        
        pool2 = IPPool.objects.create(prefix=prefix2, gateway=address3, dhcp_server=address3)
        
        fabricsite_list = [
            FabricSite(name='Fabric Site 1', physical_site=site1),
            FabricSite(name='Fabric Site 2', physical_site=site2),
            FabricSite(name='Fabric Site 3', physical_site=site1)
        ]
        FabricSite.objects.bulk_create(fabricsite_list)
        
        cls.create_data = [
            {
                'name': 'Fabric Site 4',
                'physical_site': site1.id,
                'location': location1.id,
                'ip_prefixes': [pool1.id],
            },
            {
                'name': 'Fabric Site 5',
                'physical_site': site1.id,
                'ip_prefixes': [pool1.id],
            },
            {
                'name': 'Fabric Site 6',
                'physical_site': site2.id,
                'ip_prefixes': [pool1.id, pool2.id]
            }
        ]