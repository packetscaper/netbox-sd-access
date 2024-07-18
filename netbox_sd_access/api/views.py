from netbox.api.viewsets import NetBoxModelViewSet
from django.db.models import Count

from .. import filtersets, models
from .serializers import FabricSiteSerializer, IPTransitSerializer, SDATransitSerializer

class FabricSiteViewSet(NetBoxModelViewSet):
    queryset = models.FabricSite.objects.prefetch_related('tags').annotate(
        device_count=Count('devices')
    )
    serializer_class = FabricSiteSerializer
    
class IPTransitViewSet(NetBoxModelViewSet):
    queryset = models.IPTransit.objects.prefetch_related('tags').all()
    serializer_class = IPTransitSerializer
    
class SDATransitViewSet(NetBoxModelViewSet):
    queryset = models.SDATransit.objects.prefetch_related('tags').all()
    serializer_class = SDATransitSerializer