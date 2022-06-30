# Create your views here.
from django.shortcuts import render
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
import json

class CreateOrder(GenericAPIView):
    serializer_class=OrderSerializer
    def post(self,request):
       try:
        data2=json.loads(json.dumps((request.data)))
        price=Products.objects.get(id=data2['Product_id'])
        Price=price.Price
        Quantity=data2['Product_quantity']
        print(float(Quantity)*float(Price))
        data2['Total_amount']=float(Quantity)*float(Price)
        serializer=OrderSerializerToGet(data=data2)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success'})
        else:
            return Response({'status': 'error'})
       except Exception as e:
           return Response({'status': 'error'})
class Getorder(GenericAPIView):
    serializer_class=OrderSerializer
    def get(self,request,pk):
     try:
        products=OrderDetails.objects.filter(User_id=pk)
        serializer=OrderSerializerToGet(instance=products,many=True)
        return Response({'status': 'true',"data":serializer.data})
     except Exception as e:
           return Response({'status': 'error'})