# Generated by Django 4.0.5 on 2022-06-30 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='Product_Id',
        ),
        migrations.AddField(
            model_name='products',
            name='Price',
            field=models.FloatField(default=2.0),
            preserve_default=False,
        ),
    ]
