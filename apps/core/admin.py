from django.contrib import admin

# Register your models here.
from apps.core.models import Business, TaxHistory, BusinessOwnerDetail, BusinessPreviousRegistrationDetail, \
    BusinessOwnerRelation

admin.site.register([Business, TaxHistory, BusinessOwnerDetail, BusinessPreviousRegistrationDetail,
                     BusinessOwnerRelation])
