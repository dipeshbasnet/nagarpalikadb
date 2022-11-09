from apps.commons.serializers import DynamicFieldsModelSerializer
from ....models import TaxHistory


class TaxHistorySerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = TaxHistory
        fields = '__all__'
