from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from ..serializer.business import BusinessSerializer, RegisterBusinessSerializer
from ....models import Business


class RegisterBusinessAPIView(CreateAPIView):
    queryset = Business.objects.all()
    serializer_class = RegisterBusinessSerializer


class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    lookup_field = 'uuid'
    lookup_url_kwarg = 'uuid'
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('type',)
    search_fields = ('reg_number', 'name')

    @action(methods=['GET'], detail=False, url_name='datable', url_path='datatable')
    def datatable_response(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        count = queryset.count()
        return Response({'recordsTotal': count,
                         'recordsFiltered': 10,
                         'data': serializer.data})
