from django.db import models

# Create your models here.

class WorkflowDetails(models.Model):

    workflowName = models.CharField(max_length=500, null=False, blank=False, unique=True)
    workflowFor = models.CharField(max_length=100, null=False, blank=False)
    workflowDesc = models.CharField(max_length=1000)
