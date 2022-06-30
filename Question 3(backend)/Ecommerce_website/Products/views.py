# Create your views here.
from django.shortcuts import render
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView


class AddProduct(GenericAPIView):
    serializer_class=ProductsSerializer
    def post(self,request):
       try:
        serializer=ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success'})
        else:
            return Response({'status': 'error'})
       except Exception as e:
           print(e) 
           return Response({'status': 'error'})
class GetProduct(GenericAPIView):
    serializer_class=ProductsSerializer
    def get(self,request):
     try:
        products=Products.objects.all()
        print(products)
        serializer=ProductsSerializer(instance=products,many=True)
        print(serializer.data)           
        return Response({'status': 'true',"data":serializer.data})
     except Exception as e:
           print(e) 
           return Response({'status': 'error'})
class CreateCategory(GenericAPIView):
      serializer_class=CategorySerializer
      def post(self,request):
       try:
        serializer=CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success'})
        else:
            return Response({'status': 'error'})
       except Exception as e:
           print(e) 
           return Response({'status': 'error'})
class GetCategory(GenericAPIView):
    serializer_class=CategorySerializer
    def get(self,request):
     try:
        products=Category.objects.all()
        serializer=CategorySerializer(instance=products,many=True)
        return Response({'status': 'true',"data":serializer.data})
     except Exception as e:
           return Response({'status': 'error'})           