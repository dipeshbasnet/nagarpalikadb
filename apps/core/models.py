from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from apps.commons.models import BaseModel
from apps.core.constants import BUSINESS_TYPES, BUSINESS_STATUS

USER = get_user_model()


class DemoModel(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()


class BusinessOwnerDetail(BaseModel):
    user = models.OneToOneField(USER, on_delete=models.CASCADE)
    address_district = models.CharField(max_length=60)
    address_ward = models.CharField(max_length=60)
    address_street = models.CharField(max_length=60)
    address_house_no = models.CharField(max_length=60)
    temp_address_district = models.CharField(max_length=60)
    temp_address_ward = models.CharField(max_length=60)
    temp_address_street = models.CharField(max_length=60)
    temp_address_house_no = models.CharField(max_length=60)
    fathers_full_name = models.CharField(max_length=60)
    grand_fathers_full_name = models.CharField(max_length=60)
    citizenship_no = models.CharField(max_length=20)
    citizenship_doc = models.FileField()


class Business(BaseModel):
    class Meta:
        verbose_name_plural = 'Business'

    name = models.CharField(max_length=150)
    reg_number = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=BUSINESS_STATUS)
    type = models.CharField(max_length=15, choices=BUSINESS_TYPES)
    capital_amt = models.PositiveBigIntegerField()
    email = models.EmailField(max_length=50)
    municipality = models.CharField(max_length=60)
    ward = models.CharField(max_length=10)
    street = models.CharField(max_length=10)
    house_no = models.CharField(max_length=10)
    # point_location = PointField()  # use post gis?
    location_lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    location_lng = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    contact_no = models.CharField(max_length=10)
    mobile_no = models.CharField(max_length=10)
    signboard_size_length = models.FloatField()
    signboard_size_width = models.FloatField()
    owner = models.ManyToManyField(USER, through='BusinessOwnerRelation')
    reg_doc = models.FileField(null=True, blank=True)
    ward_doc = models.FileField(null=True, blank=True)
    ocr_doc = models.FileField(null=True, blank=True)  # needs discussion

    def __str__(self):
        return self.name


class BusinessOwnerRelation(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='business_owners')
    owner = models.ForeignKey(USER, on_delete=models.CASCADE)
    role = models.CharField(max_length=60)


class BusinessPreviousRegistrationDetail(BaseModel):
    business = models.ForeignKey(Business, on_delete=models.CASCADE,
                                 related_name='business_previous_reg_detail',
                                 )  # onetoone field?
    reg_date = models.DateField()
    reg_number = models.CharField(max_length=50)
    reg_status = models.CharField(max_length=10)
    department_location = models.CharField(max_length=100)


class TaxHistory(BaseModel):
    class Meta:
        verbose_name_plural = 'Tax Histories'

    business = models.ForeignKey(
        Business,
        on_delete=models.CASCADE,
        related_name='business_tax_histories'
    )
    receipt_number = models.CharField(max_length=20)
    tax_amount = models.FloatField()
    payment_status = models.CharField(max_length=15)
    receipt = models.FileField()  # save two types of receipt? #add paid date or just use created_at?


class LandLord(BaseModel):
    district = models.CharField(max_length=60)
    ward = models.CharField(max_length=60)
    street = models.CharField(max_length=60)
    house_no = models.CharField(max_length=60)
    # do we need temp for this?
    fathers_full_name = models.CharField(max_length=50)
    grand_fathers_full_name = models.CharField(max_length=50)
    citizenship_no = models.CharField(max_length=50)
    citizenship_doc = models.FileField()
