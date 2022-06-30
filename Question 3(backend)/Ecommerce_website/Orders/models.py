
from django.db import models
from django.contrib.auth import get_user_model
from Products.models import * 
from Products.models import Products
from userauthn.models import CustomUser
User = get_user_model()
# Create your models here.
class OrderDetails(models.Model):
    User_id=models.ForeignKey(CustomUser,on_delete=models.PROTECT)
    Product_id=models.ForeignKey(Products,on_delete=models.PROTECT)
    Product_quantity=models.IntegerField()
    Total_amount=models.FloatField(default=0)
    DeliveryStatus=models.TextField(default='Pending',blank=True)


