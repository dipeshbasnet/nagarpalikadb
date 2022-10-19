from django.db import models

# Create your models here.
from apps.commons.models import BaseModel


class DemoModel(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()


class Business(BaseModel):
    name = models.CharField(max_length=150)
    location = models.PointField()  # use post gis?

    def __str__(self):
        return self.name


class TaxHistory(BaseModel):
    business = models.ForeignKey(Business, related_name='business_tax_histories')
    tax_amount = models.FloatField()
    payment_status = models.CharField(max_length=15)
