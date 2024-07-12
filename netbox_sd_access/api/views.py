from netbox.api.viewsets import NetBoxModelViewSet
from django.db.models import Count

from .. import filtersets, models
from .serializers import FabricSiteSerializer

class FabricSiteViewSet(NetBoxModelViewSet):
    queryset = models.FabricSite.objects.prefetch_related('tags').annotate(
        device_count=Count('devices')
    )
    serializer_class = FabricSiteSerializer