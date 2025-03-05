from django.contrib import admin
from django.urls import path
from customer.views import *

urlpatterns = [
    path('login/',login,name='login'),
    path('bestseller/',bestseller,name='bestseller'),
    path('address/',address,name='address'),
    path('registration/',registration,name='registration'),
    path('cartview/',cartview,name='cartview'),
    path('cartdata/',cartdata,name='cartdata'),
    path('cartupdate/<int:id>/',cartupdate,name='cartupdate'),
    path('buyview/',buyview,name='buyview'),
    path('buydata/',buydata,name='buydata'),
    path('orderdetails/',orderdetails,name='orderdetails'),
    path('chekout/',chekout,name='chekout'),
    path('delete/<int:id>/',delete,name='delete'),
   
    
    path('logout/',logout,name='logout')
    
    
    
]