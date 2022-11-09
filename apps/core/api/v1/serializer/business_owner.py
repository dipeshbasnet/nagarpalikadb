from apps.commons.serializers import DynamicFieldsModelSerializer
from apps.core.models import BusinessOwnerDetail


class BusinessOwnerDetailSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = BusinessOwnerDetail
        fields = '__all__'
