from django.urls import path
from rest_framework import routers

from .views.business import BusinessViewSet, RegisterBusinessAPIView
from .views.bussiness_owners import BusinessOwnerDetailViewSet
from .views.demo import DemoView, DemoViewSet
from .views.tax import TaxHistoryViewSet

ROUTER = routers.DefaultRouter()

# ROUTER.register('demo', DemoViewSet, basename='demo-viewset')
ROUTER.register('business', BusinessViewSet, basename='business')
ROUTER.register('business-owner', BusinessOwnerDetailViewSet, basename='business_owner')
ROUTER.register('tax-history', TaxHistoryViewSet, basename='tax_hisotry')

urlpatterns = [
                  path('register-business/', RegisterBusinessAPIView.as_view())
              ] + ROUTER.urls
