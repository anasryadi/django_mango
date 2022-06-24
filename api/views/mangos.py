from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models.mango import Mango 
from ..serializers.mango_input import MangoInputSerializer
from ..serializers.mango_output import MangoOutputSerializer

class MangosView(APIView):
    def get(self, request):
        mangos = Mango.objects.all()
        data = MangoOutputSerializer(mangos, many=True).data
        return Response(data)

    def post(self, request):
        mango = MangoInputSerializer(data=request.data)
        if mango.is_valid():
            mango.save()
            return Response(mango.data, status=status.HTTP_201_CREATED)
        else:
            return Response(mango.errors, status=status.HTTP_400_BAD_REQUEST) 

class MangoView(APIView):
    def get(self, request, pk):
        mango = get_object_or_404(Mango, pk=pk)
        data = MangoOutputSerializer(mango).data
        return Response(data)
    
    def delete(self, request, pk):
        mango = get_object_or_404(Mango, pk=pk)
        mango.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        mango = get_object_or_404(Mango, pk=pk)
        updated_mango = MangoInputSerializer(mango, data=request.data)
        if updated_mango.is_valid():
            updated_mango.save()
            return Response(updated_mango.errors)
        else:
            return Response(updated_mango.errors, status=status.HTTP_400_BAD_REQUEST)