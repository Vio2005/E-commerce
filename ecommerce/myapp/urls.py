from django.urls import path
from.views import *

urlpatterns=[
    path('home/',home,name='home'),
    path('createitem/',createitem,name='createitem'),
    path('createcategory/',createcategory,name='createcategory')
   
]