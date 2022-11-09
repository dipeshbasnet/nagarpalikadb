from django.urls import path
from rest_framework import routers

from .views.card_data import CardDataAPIView
from .views.month_wise_business import MonthWiseBusinessRegistrationView
from .views.month_wise_tax import MonthWiseTaxCollectionView

ROUTER = routers.DefaultRouter()

urlpatterns = [
                  path('card-data/', CardDataAPIView.as_view()),
                  path('month-wise-registration/', MonthWiseBusinessRegistrationView.as_view()),
                  path('month-wise-collection/', MonthWiseTaxCollectionView.as_view()),
              ] + ROUTER.urls
