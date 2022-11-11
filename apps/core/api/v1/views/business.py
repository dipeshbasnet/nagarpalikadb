from rest_framework import viewsets
from rest_framework.response import Response

from ..serializer.business import BusinessSerializer
from ....models import Business


class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        count = queryset.count()
        return Response({'recordsTotal': count,
                         'recordsFiltered': count,
                         'data': serializer.data})
