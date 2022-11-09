from apps.commons.serializers import DynamicFieldsModelSerializer
from .tax import TaxHistorySerializer
from ....models import Business


class BusinessSerializer(DynamicFieldsModelSerializer):
    tax_history = TaxHistorySerializer()

    class Meta:
        model = Business
        fields = '__all__'
