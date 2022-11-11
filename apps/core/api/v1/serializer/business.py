from rest_framework import serializers

from apps.commons.serializers import DynamicFieldsModelSerializer
from .tax import TaxHistorySerializer
from ....models import Business, BusinessOwnerRelation


class BusinessSerializer(DynamicFieldsModelSerializer):
    owner = serializers.SerializerMethodField()

    # tax_history = TaxHistorySerializer()

    class Meta:
        model = Business
        fields = '__all__'

    #aile hattar ma gareko, this needs to be changed
    #aile hattar ma gareko, this needs to be changed
    def get_owner(self, obj):
        try:
            obj = BusinessOwnerRelation.objects.filter(
                business=obj
            ).first().owner
            return f"{obj.first_name} {obj.last_name}"
        except AttributeError:
            return None
