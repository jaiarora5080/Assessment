from django.urls import path
from .views import *


urlpatterns = [
    path('saveWorkflowDetails/', WorkflowDetailsAPIView.as_view()),
]
