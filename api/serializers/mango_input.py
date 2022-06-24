from rest_framework import serializers
from ..models.mango import Mango


class MangoInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mango
        fields = ('id', 'color', 'ripe', 'mango_shop')