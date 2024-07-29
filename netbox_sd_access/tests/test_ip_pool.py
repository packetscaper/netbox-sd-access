#!/usr/bin/env python

"""Tests for IP Pools."""

from django.urls import reverse
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

from rest_framework import status
from utilities.testing import APITestCase, APIViewTestCases

from ipam.models import Prefix, IPAddress

from netbox_sd_access.models import *

class IPPoolTestCase(APIViewTestCases.APIViewTestCase):
    model = IPPool
    view_namespace = 'plugins-api:netbox_sd_access'
    brief_fields = ['display', 'id', 'prefix', 'url']
    
    @classmethod
    def setUpTestData(cls) -> None:
        prefix1 = Prefix.objects.create(prefix='10.0.0.0/24')
        prefix2 = Prefix.objects.create(prefix='10.0.1.0/24')
        prefix3 = Prefix.objects.create(prefix='10.0.2.0/24')
        
        gateway1 = IPAddress.objects.create(address='10.0.0.1/24')
        gateway2 = IPAddress.objects.create(address='10.0.1.1/24')
        gateway3 = IPAddress.objects.create(address='10.0.2.0/24')
        
        dhcp2 = IPAddress.objects.create(address='10.0.1.2/24')
        
        dns1 = IPAddress.objects.create(address='192.168.1.1/24')
        dns2 = IPAddress.objects.create(address='192.168.1.2/24')
        
        ippool_list = (
            IPPool(name='Pool1', prefix=prefix1, gateway=gateway1, dhcp_server=gateway1),
            IPPool(name='Pool2', prefix=prefix2, gateway=gateway2, dhcp_server=dhcp2),
            IPPool(name='Pool3', prefix=prefix3, gateway=gateway3, dhcp_server=gateway3),
        )
        
        for pool in ippool_list:
            pool.save()
            pool.dns_servers.add(dns1)
            pool.dns_servers.add(dns2)
            
        prefix4 = Prefix.objects.create(prefix='10.0.3.0/24')
        prefix5 = Prefix.objects.create(prefix='10.0.4.0/24')
        prefix6 = Prefix.objects.create(prefix='10.0.5.0/24')
        
        gateway4 = IPAddress.objects.create(address='10.0.3.1/24')
        gateway5 = IPAddress.objects.create(address='10.0.4.1/24')
        gateway6 = IPAddress.objects.create(address='10.0.5.0/24')
        
        dhcp5 = IPAddress.objects.create(address='10.0.4.2/24')
        
        cls.create_data = [
            {
                'name':'Pool4',
                'prefix': prefix4.id,
                'gateway': gateway4.id,
                'dhcp_server': gateway5.id,
                'dns_servers': [dns1.id, dns2.id]
            },
            {
                'name':'Pool5',
                'prefix': prefix5.id,
                'gateway': gateway5.id,
                'dhcp_server': dhcp5.id,
                'dns_servers': [dns1.id,]
            },
            {
                'name':'Pool6',
                'prefix': prefix6.id,
                'gateway': gateway6.id,
                'dhcp_server': gateway6.id,
            },
        ]

class IPPoolValidationTestCase(TestCase):
    def setUp(self):
        self.prefix1 = Prefix.objects.create(prefix='10.0.0.0/24')
        self.address1 = IPAddress.objects.create(address='10.0.0.1/24')
        self.address2 = IPAddress.objects.create(address='10.0.1.1/24')
    
    def test_gateway_oob(self):
        ippool = IPPool(
            name='Pool1',
            prefix=self.prefix1,
            gateway=self.address2,
            dhcp_server=self.address1,
        )
        self.assertRaises(ValidationError, ippool.full_clean)

class IPPoolValidationTestCase(TestCase):
    def setUp(self):
        self.prefix1 = Prefix.objects.create(prefix='10.0.0.0/24')
        self.address1 = IPAddress.objects.create(address='10.0.0.1/24')
        self.pool1 = IPPool.objects.create(
            name='Pool1',
            prefix=self.prefix1,
            gateway=self.address1,
            dhcp_server=self.address1
        )
    
    def test_unique_names(self):
        with self.assertRaises(IntegrityError):
            IPPool.objects.create(
                name='Pool1',
                prefix=self.prefix1,
                gateway=self.address1,
                dhcp_server=self.address1
            )