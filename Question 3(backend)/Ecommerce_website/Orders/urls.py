from django.urls import path, include
from .views import *
urlpatterns = [
    path('CreateOrder/',CreateOrder.as_view()),
    path('Getorder/<str:pk>/',Getorder.as_view()),

]