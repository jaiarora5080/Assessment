# Generated by Django 4.0.5 on 2022-06-30 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0002_remove_orderdetails_user_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetails',
            name='DeliveryStatus',
            field=models.TextField(default='Pending'),
            preserve_default=False,
        ),
    ]