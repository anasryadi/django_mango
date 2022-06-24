from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models.mango_shop import MangoShop 
from ..serializers.mango_shop import MangoShopSerializer 

class MangoShopsView(APIView):
    def get(self, request):
        mango_shops = MangoShop.objects.all()
        data = MangoShopSerializer(mango_shops, many=True).data
        return Response(data)

    def post(self, request):
        mango_shop = MangoShopSerializer(data=request.data)
        if mango_shop.is_valid():
            mango_shop.save()
            return Response(mango_shop.data, status=status.HTTP_201_CREATED)
        else:
            return Response(mango_shop.errors, status=status.HTTP_400_BAD_REQUEST) 

class MangoShopView(APIView):
    def get(self, request, pk):
        mango_shop = get_object_or_404(MangoShop, pk=pk)
        data = MangoShopSerializer(mango_shop).data
        return Response(data)
    
    def delete(self, request, pk):
        mango_shop = get_object_or_404(MangoShop, pk=pk)
        mango_shop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        mango_shop = get_object_or_404(MangoShop, pk=pk)
        updated_mango_shop = MangoShopSerializer(mango_shop, data=request.data)
        if updated_mango_shop.is_valid():
            updated_mango_shop.save()
            return Response(updated_mango_shop.errors)
        else:
            return Response(updated_mango_shop.errors, status=status.HTTP_400_BAD_REQUEST)