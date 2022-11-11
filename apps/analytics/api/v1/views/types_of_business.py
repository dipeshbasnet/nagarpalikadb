from django.db.models import Sum, Count, Q
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.models import TaxHistory, Business

# grab these from constants
PRIVATE_LTD = "PVT LTD"
HOUSEHOLD_DOMESTIC = "Domestic"
OTHERS = "Others"


class BusinessTypeAPIView(APIView):
    def get(self, request, *args, **kwargs):
        business_types = Business.objects.all().aggregate(
            private=Count('pk', filter=Q(type=PRIVATE_LTD)),
            domestic=Count('pk', filter=Q(type=HOUSEHOLD_DOMESTIC)),
            others=Count('pk', filter=Q(type=OTHERS))

        )
        return Response(business_types)
