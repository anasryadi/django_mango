from rest_framework import serializers
from ..models.mango_shop import MangoShop


class MangoShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = MangoShop
        fields = ('id', 'name', 'location', 'mangos')
