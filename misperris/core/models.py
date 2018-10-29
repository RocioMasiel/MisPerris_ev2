from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Raza(models.Model):
    name=models.CharField(max_length=45,primary_key=True)
    def __str__(self):
        return self.name

class Estado(models.Model):
    name=models.CharField(max_length=45,primary_key=True)
    def __str__(self):
        return self.name

class Perro(models.Model):
    name=models.CharField(max_length=20,primary_key=True)
    foto=models.ImageField(upload_to='core/img/',default='DEFAULT VALUE')
    raza=models.ForeignKey(Raza,on_delete=models.CASCADE)
    estado=models.ForeignKey(Estado,on_delete=models.CASCADE,default='DEFAULT VALUE')
    descripcion=models.TextField()
    def __str__(self):
        return self.name

class Region(models.Model):
    name=models.CharField(max_length=40,primary_key=True)
    def __str__(self):
        return self.name

class Ciudad(models.Model):
    name=models.CharField(max_length=40,primary_key=True)
    def __str__(self):
        return self.name

class Vivienda(models.Model):
    name=models.CharField(max_length=30,primary_key=True)
    def __str__(self):
        return self.name

class Adoptante(models.Model):
    rut=models.CharField(max_length=10,primary_key=True)
    nombre=models.CharField(max_length=20)
    direccion=models.TextField(max_length=45)
    email=models.TextField(max_length=30)
    fecha=models.CharField(max_length=10)
    telefono=models.TextField(max_length=10)
    #region=models.ForeignKey(Region,on_delete=models.CASCADE)
    #ciudad=models.ForeignKey(Ciudad,on_delete=models.CASCADE)
    #vivienda=models.ForeignKey(Vivienda,on_delete=models.CASCADE)
    def __str__(self):
        return self.rut 


