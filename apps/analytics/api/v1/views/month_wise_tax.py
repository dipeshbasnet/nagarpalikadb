import calendar

from django.db.models import Sum, Q
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.models import TaxHistory


class MonthWiseTaxCollectionView(APIView):
    def get(self, request, *args, **kwargs):
        year = timezone.now().year
        month_number = timezone.now().month
        months = list(calendar.month_abbr)[1:month_number + 1]
        _aggregate_query = {
            month[1]: Sum('tax_amount',
                          filter=Q(
                              created_at__month=month[0],
                              created_at__year=year)
                          )
            for month in enumerate(months, 1)
        }

        data = TaxHistory.objects.all().aggregate(
            **_aggregate_query
        )
        return Response(data)
