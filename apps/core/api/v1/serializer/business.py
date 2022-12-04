import random

from rest_framework import serializers

from apps.commons.serializers import DynamicFieldsModelSerializer
from .tax import TaxHistorySerializer
from ....models import Business, BusinessOwnerRelation, LandLord


# not a good way to do it but we need form data

def _get_data(validated_data, obj_type, _fields):
    _index = 3 if obj_type in ['business_owner', 'land_lord'] else 0
    return dict(map(lambda _item:
                    (_item[_index:], validated_data.get(_item)), _fields))


class RegisterBusinessSerializer(serializers.Serializer):
    business_name = serializers.CharField(max_length=150)
    reg_number = serializers.CharField(max_length=50)
    status = serializers.CharField(max_length=20)
    business_type = serializers.CharField(max_length=15)
    capital_amt = serializers.IntegerField()
    email = serializers.EmailField(max_length=50)
    municipality = serializers.CharField(max_length=60)
    ward = serializers.CharField(max_length=10)
    street = serializers.CharField(max_length=200)
    house_no = serializers.CharField(max_length=10)
    location_lat = serializers.DecimalField(max_digits=9, decimal_places=6)
    location_lng = serializers.DecimalField(max_digits=9, decimal_places=6)
    contact_no = serializers.CharField(max_length=10)
    mobile_no = serializers.CharField(max_length=10)
    signboard_size_length = serializers.FloatField()
    signboard_size_width = serializers.FloatField()
    reg_doc = serializers.FileField()
    ward_doc = serializers.FileField()
    ocr_doc = serializers.FileField()
    bo_address_district = serializers.CharField(max_length=60)
    bo_address_ward = serializers.CharField(max_length=60)
    bo_address_street = serializers.CharField(max_length=200)
    bo_address_house_no = serializers.CharField(max_length=60)
    bo_temp_address_district = serializers.CharField(max_length=60)
    bo_temp_address_ward = serializers.CharField(max_length=60)
    bo_temp_address_street = serializers.CharField(max_length=20)
    bo_temp_address_house_no = serializers.CharField(max_length=60)
    bo_fathers_full_name = serializers.CharField(max_length=60)
    bo_grand_fathers_full_name = serializers.CharField(max_length=60)
    bo_citizenship_no = serializers.CharField(max_length=20)
    bo_citizenship_doc = serializers.FileField()
    ll_first_name = serializers.CharField(max_length=60)
    ll_middle_name = serializers.CharField(max_length=60)
    ll_last_name = serializers.CharField(max_length=60)
    ll_district = serializers.CharField(max_length=60)
    ll_ward = serializers.CharField(max_length=60)
    ll_street = serializers.CharField(max_length=200)
    ll_house_no = serializers.CharField(max_length=60)
    ll_fathers_full_name = serializers.CharField(max_length=50)
    ll_grand_fathers_full_name = serializers.CharField(max_length=50)
    ll_citizenship_no = serializers.CharField(max_length=50)
    ll_citizenship_doc = serializers.FileField()
    ll_land_ownership_certificate = serializers.FileField()

    def create(self, validated_data):
        _business_fields = [
            'business_name', 'reg_number', 'status', 'business_type', 'capital_amt', 'email',
            'municipality', 'ward', 'street', 'house_no', 'location_lat', 'location_lng', 'contact_no',
            'mobile_no', 'signboard_size_length', 'signboard_size_width', 'reg_doc', 'ward_doc',
            'ocr_doc'
        ]
        _bo_fields = [
            'bo_address_district', 'bo_address_ward', 'bo_address_street',
            'bo_address_house_no', 'bo_temp_address_district', 'bo_temp_address_ward',
            'bo_temp_address_street', 'bo_temp_address_house_no', 'bo_fathers_full_name',
            'bo_grand_fathers_full_name', 'bo_citizenship_no', 'bo_citizenship_doc'
        ]
        _ll_fields = [
            'll_first_name',
            'll_middle_name', 'll_last_name', 'll_district', 'll_ward', 'll_street', 'll_house_no',
            'll_fathers_full_name', 'll_grand_fathers_full_name', 'll_citizenship_no',
            'll_citizenship_doc', 'll_land_ownership_certificate'
        ]

        business_data = _get_data(validated_data, 'business', _business_fields)
        # business_owner_data = _get_data(validated_data, 'business_owner', _bo_fields)
        land_lord_data = _get_data(validated_data, 'land_lord', _ll_fields)
        ll_obj, _ = LandLord.objects.get_or_create(**land_lord_data)
        bo_obj = None
        business_data.update(
            owner=bo_obj,
            land_lord=ll_obj
        )
        instance = Business.objects.create(
            **business_data
        )
        return instance


class BusinessSerializer(DynamicFieldsModelSerializer):
    owner = serializers.SerializerMethodField()

    # tax_history = TaxHistorySerializer()

    class Meta:
        model = Business
        fields = '__all__'

    # aile hattar ma gareko, this needs to be changed
    def get_owner(self, obj):
        # static data
        return random.choice(['Anup Acharya', 'Sanjay Khadka', 'Susan Bhattarai', 'Utsav Lamicchane', 'Sagun Raj Lage',
                              'Kshitij Lohani'])
