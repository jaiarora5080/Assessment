# Generated by Django 4.0.5 on 2022-06-30 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0003_orderdetails_deliverystatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='DeliveryStatus',
            field=models.TextField(default='Pending'),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='Product_quantity',
            field=models.IntegerField(),
        ),
    ]