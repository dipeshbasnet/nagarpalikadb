from django.db.models import Sum, Count, Q
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.models import TaxHistory, Business

# grab these from constants
PRIVATE_LTD = "PRIVATE LTD"
HOUSEHOLD_DOMESTIC = "HOUSEHOLD/DOMESTIC"
OTHERS = "OTHERS"


class BusinessTypeAPIView(APIView):
    def get(self, request, *args, **kwargs):
        business_types = Business.objects.all().aggregate(
            private=Count('pk', filter=Q(type=PRIVATE_LTD)),
            domestic=Count('pk', filter=Q(status=HOUSEHOLD_DOMESTIC)),
            others=Count('pk', filter=Q(status=OTHERS))

        )
        return Response(business_types)
