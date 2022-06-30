
from django.db import models

# Create your models here.
class Category(models.Model):
    Category_name=models.CharField(max_length=2000)

class Products(models.Model):
    Product_name=models.CharField(max_length=2000)
    Product_desc=models.CharField(max_length=2000)
    Price=models.FloatField()
    Quantity=models.IntegerField()
    Category=models.ForeignKey(Category,on_delete=models.PROTECT)

