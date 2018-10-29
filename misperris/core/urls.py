from django.contrib import admin
from django.urls import path,include
from .views import index,login,registrar,solicitudadopcion

urlpatterns = [
    
    path('',index,name='home'),
    path('login/',login,name='login'),  
    path('registrar/',registrar,name='reg'), 
    path('solicitudadopcion/',solicitudadopcion,name='adop'),  
    
]