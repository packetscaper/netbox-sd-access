#!/usr/bin/env python

"""Tests for `netbox_sd_access` package."""

from django.urls import reverse
from rest_framework import status
from utilities.testing import APITestCase, APIViewTestCases

from dcim.models import Site
from ipam.models import ASN, RIR

from netbox_sd_access.models import *

class IPTransitTestCase(APIViewTestCases.APIViewTestCase):
    model = IPTransit
    view_namespace = 'plugins-api:netbox_sd_access'
    brief_fields = ['asn', 'display', 'fabric_site', 'id', 'name', 'url']
    
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
        
        rir1 = RIR.objects.create(name='RIR1', slug='rir1')
        
        asns = [
            ASN(asn='123', rir=rir1),
            ASN(asn='234', rir=rir1),
            ASN(asn='345', rir=rir1),
            ASN(asn='456', rir=rir1),
            ASN(asn='567', rir=rir1),
            ASN(asn='678', rir=rir1)
        ]
        
        ASN.objects.bulk_create(asns)
        
        ip_transits = [
            IPTransit(
                fabric_site=fabricsite_list[0],
                asn=asns[0]
            ),
            IPTransit(
                fabric_site=fabricsite_list[1],
                asn=asns[1]
            ),
            IPTransit(
                fabric_site=fabricsite_list[2],
                asn=asns[2]
            ),
        ]
        
        IPTransit.objects.bulk_create(ip_transits)
        
        cls.create_data = [
            {
                'name': 'IPTransit 4',
                'fabric_site': fabricsite_list[3].id,
                'asn': asns[3].id
            },
            {
                'name': 'IPTransit 5',
                'fabric_site': fabricsite_list[4].id,
                'asn': asns[4].id
            },
            {
            
                'name': 'IPTransit 6',
                'fabric_site': fabricsite_list[5].id,
                'asn': asns[5].id
            }
        ]