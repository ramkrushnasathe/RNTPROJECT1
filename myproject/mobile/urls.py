from django.contrib import admin
from django.urls import path
from mobile.views import *

urlpatterns = [
    
    path('mobile1/',mobile1,name='mobile1'),
    path('mobile2/',mobile2,name='mobile2'),
    path('mobile3/',mobile3,name='mobile3'),
    path('mobile4/',mobile4,name='mobile4'),


    
    
    
    
]