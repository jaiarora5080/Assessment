# Generated by Django 3.2.7 on 2022-06-30 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkflowDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workflowName', models.CharField(max_length=500, unique=True)),
                ('workflowFor', models.CharField(max_length=100)),
                ('workflowDesc', models.CharField(max_length=1000)),
            ],
        ),
    ]
