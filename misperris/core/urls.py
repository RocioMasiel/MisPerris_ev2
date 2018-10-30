from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from .views import index,login,registrar,solicitudadopcion,listar,logout,eliminar,buscar

urlpatterns = [
    
    path('',index,name='home'),
    path('login/',login,name='login'),  
    path('registrar/',registrar,name='reg'), 
    path('solicitudadopcion/',solicitudadopcion,name='adop'),  
    path('listar/',listar,name='listar'),
    path('logout/',logout,name='logout'),
    path('eliminar/',eliminar,name='eli'),
    path('galeria/',buscar,name='gal'),
    
]