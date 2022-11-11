from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..serializer.tax import TaxHistorySerializer
from ....models import TaxHistory


class TaxHistoryViewSet(viewsets.ModelViewSet):
    queryset = TaxHistory.objects.all()
    serializer_class = TaxHistorySerializer()

    @action(methods=['GET'], detail=False, url_name='top_tax_payer', url_path='top-tax-payers')
    def top_tax_data(self, request, *args, **kwargs):
        demo_json = dict(
            data=[
                {
                    'name': 'Awiskar Solutions',
                    'type': "PVT LTD",
                    'tax_amount': "52343.23"
                },
                {
                    'name': 'Dev Async',
                    'type': "PVT LTD",
                    'tax_amount': "50112.23"
                },
                {
                    'name': 'Cotiviti',
                    'type': "Domestic",
                    'tax_amount': "45343.23"
                },
                {
                    'name': 'Bhat Bhateni',
                    'type': "PVT LTD",
                    'tax_amount': "34534.3"
                },
                {
                    'name': 'Kritya',
                    'type': "Domestic",
                    'tax_amount': "5233.23"
                },

            ]
        )
        return Response(demo_json)
