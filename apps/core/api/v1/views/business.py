from rest_framework import viewsets

from ..serializer.business import BusinessSerializer
from ....models import Business


class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
