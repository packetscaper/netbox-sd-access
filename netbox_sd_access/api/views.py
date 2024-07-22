from netbox.api.viewsets import NetBoxModelViewSet
from django.db.models import Count

from .. import filtersets, models
from .serializers import *

class FabricSiteViewSet(NetBoxModelViewSet):
    queryset = models.FabricSite.objects.prefetch_related('tags').annotate(
        device_count=Count('devices')
    )
    serializer_class = FabricSiteSerializer
    filterset_class = filtersets.FabricSiteFilterSet
    
class IPTransitViewSet(NetBoxModelViewSet):
    queryset = models.IPTransit.objects.prefetch_related('tags').all()
    serializer_class = IPTransitSerializer
    filterset_class = filtersets.IPTransitFilterSet
    
class SDATransitViewSet(NetBoxModelViewSet):
    queryset = models.SDATransit.objects.prefetch_related('tags').all()
    serializer_class = SDATransitSerializer
    filterset_class = filtersets.SDATransitFilterSet

class SDADeviceViewSet(NetBoxModelViewSet):
    queryset = models.SDADevice.objects.prefetch_related('tags').all()
    serializer_class = SDADeviceSerializer
    filterset_class = filtersets.SDADeviceFilterSet

class IPPoolViewSet(NetBoxModelViewSet):
    queryset = models.IPPool.objects.prefetch_related('tags').all()
    serializer_class = IPPoolSerializer
    filterset_class = filtersets.IPPoolFilterSet

class VirtualNetworkViewSet(NetBoxModelViewSet):
    queryset = models.VirtualNetwork.objects.prefetch_related('tags').all()
    serializer_class = VirtualNetworkSerializer
    filterset_class = filtersets.VirtualNetworkFilterSet