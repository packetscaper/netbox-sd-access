from netbox.api.viewsets import NetBoxModelViewSet
from django.db.models import Count

from .. import filtersets, models
from .serializers import FabricSiteSerializer, VirtualNetworkSerializer

class FabricSiteViewSet(NetBoxModelViewSet):
    queryset = models.FabricSite.objects.prefetch_related('tags').annotate(
        device_count=Count('devices')
    )
    serializer_class = FabricSiteSerializer

class VirtualNetworkViewSet(NetBoxModelViewSet):
    queryset = models.VirtualNetwork.objects.prefetch_related('tags').annotated(
        device_count=Count('devices')
    )
    serializer_class = VirtualNetworkSerializer
    filterset_class = filtersets.VirtualNetworkFilterSet