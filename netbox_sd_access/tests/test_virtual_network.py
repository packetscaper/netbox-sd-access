#!/usr/bin/env python

"""Tests for Virtual Networks."""

from django.urls import reverse
from rest_framework import status
from django.db import IntegrityError

from django.test import TestCase
from utilities.testing import APITestCase, APIViewTestCases

from dcim.models import Site
from ipam.models import VRF

from netbox_sd_access.models import *

class VirtualNetworkTestCase(APIViewTestCases.APIViewTestCase):
    model = VirtualNetwork
    view_namespace = 'plugins-api:netbox_sd_access'
    brief_fields = ['fabric_site', 'id', 'name', 'url']
    
    @classmethod
    def setUpTestData(cls) -> None:
        site1 = Site.objects.create(name='RTP', slug='rtp')
        fabric_site1 = FabricSite.objects.create(name='Site 1', physical_site=site1)
        fabric_site2 = FabricSite.objects.create(name='Site 2', physical_site=site1)
        fabric_site3 = FabricSite.objects.create(name='Site 3', physical_site=site1)
        
        vrf1 = VRF.objects.create(name='VRF1')
        vrf2 = VRF.objects.create(name='VRF2')
        vrf3 = VRF.objects.create(name='VRF3')
        
        vn_list = [
            VirtualNetwork(
                name='VN1',
                vrf=vrf1
            ),
            VirtualNetwork(
                name='VN2',
                vrf=vrf2
            ),
            VirtualNetwork(
                name='VN3',
                vrf=vrf3
            ),
        ]
        
        VirtualNetwork.objects.bulk_create(vn_list)
        
        vrf4 = VRF.objects.create(name='VRF4')
        vrf5 = VRF.objects.create(name='VRF5')
        vrf6 = VRF.objects.create(name='VRF6')
        
        cls.create_data = [
            {
                'name': 'VN4',
                'fabric_site': [fabric_site1.id, fabric_site3.id],
                'vrf': vrf4.id
            },
            {
                'name': 'VN5',
                'fabric_site': [fabric_site3.id],
                'vrf': vrf5.id
            },
            {
                'name': 'VN6',
                'fabric_site': [fabric_site2.id, fabric_site3.id],
                'vrf': vrf6.id
            },
        ]

class VirtualNetworkValidationTestCase(TestCase):
    def setUp(self):
        self.vrf1 = VRF.objects.create(name='VRF1')
        self.vn1 = VirtualNetwork.objects.create(name='VN1', vrf=self.vrf1)
    
    def test_unique_name(self):
        vrf2 = VRF.objects.create(name='VRF2')
        with self.assertRaises(IntegrityError):
            VirtualNetwork.objects.create(name='VN1', vrf=vrf2)