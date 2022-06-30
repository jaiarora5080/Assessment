from django.urls import path, include
from .views import *
urlpatterns = [
    #Product URLS
    path('Addproduct/',AddProduct.as_view()),
    path('GetProduct/',GetProduct.as_view()),
    #category URLS
    path('Addcategory/',CreateCategory.as_view()),
    path('Getcategory/',GetCategory.as_view()),


]