from rest_framework import viewsets

from ..serializer.tax import TaxHistorySerializer
from ....models import TaxHistory


class TaxHistoryViewSet(viewsets.ModelViewSet):
    queryset = TaxHistory.objects.all()
    serializer_class = TaxHistorySerializer()
