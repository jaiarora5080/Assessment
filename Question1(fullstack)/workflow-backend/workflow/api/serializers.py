from rest_framework import serializers
from .models import *



class WorkflowDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkflowDetails
        fields = "__all__"