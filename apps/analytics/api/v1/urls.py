from django.urls import path
from rest_framework import routers

from .views.card_data import CardDataAPIView
from .views.month_wise_business import MonthWiseBusinessRegistrationView
from .views.month_wise_tax import MonthWiseTaxCollectionView
from .views.types_of_business import BusinessTypeAPIView

ROUTER = routers.DefaultRouter()

urlpatterns = [
                  path('card-data/', CardDataAPIView.as_view()),
                  path('month-wise-registration/', MonthWiseBusinessRegistrationView.as_view()),
                  path('month-wise-collection/', MonthWiseTaxCollectionView.as_view()),
                  path('type-of-business/', BusinessTypeAPIView.as_view()),
              ] + ROUTER.urls
