from rest_framework import serializers
from ..models.mango import Mango
from ..serializers.mango_shop import MangoShopSerializer


class MangoOutputSerializer(serializers.ModelSerializer):
    mango_shop = MangoShopSerializer(many=False)
    class Meta:
        model = Mango
        fields = ('id', 'color', 'ripe', 'mango_shop')