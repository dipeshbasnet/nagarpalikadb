from django.db.models import Sum, Count, Q
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.models import TaxHistory, Business

PENDING = "PENDING"
APPROVED = "APPROVED"
REJECTED = "REJECTED"  # grab these from constants


class CardDataAPIView(APIView):
    def get(self, request, *args, **kwargs):
        business = Business.objects.all().aggregate(
            registered=Count('pk', filter=Q(status=APPROVED)),
            pending=Count('pk', filter=Q(status=PENDING)),
            rejected=Count('pk', filter=Q(status=REJECTED))

        )
        tax_collected = TaxHistory.objects.all().aggregate(
            collected=Sum('tax_amount')
        )
        return Response({
            'registered': business.get('registered'),
            'pending': business.get('pending'),
            'rejected': business.get('rejected'),
            'total_tax_collected': tax_collected.get('collected')
        }
        )
