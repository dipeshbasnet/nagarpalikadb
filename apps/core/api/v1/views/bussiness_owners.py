from rest_framework import viewsets

from ..serializer.business_owner import BusinessOwnerDetailSerializer
from ....models import BusinessOwnerDetail


class BusinessOwnerDetailViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BusinessOwnerDetailSerializer
    queryset = BusinessOwnerDetail.objects.all()
