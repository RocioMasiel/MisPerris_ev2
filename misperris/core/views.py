from django.shortcuts import render
from .models import Raza,Estado,Perro,Region,Adoptante
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'core/home.html')

def logout(request):
    auth.logout(request)
    return render(request,'core/login.html')

def login(request):
    if request.POST:
        usu=request.POST["txtUsuario"]
        pas=request.POST["txtPass"]
        user=auth.authenticate(username=usu,password=pas)
        if user is not None and user.is_active:
            auth.login(request,user)
            return render(request,'core/home.html',{'usuario':user.username})
        else:
            return render(request,'core/error.html')

    return render(request,'core/login.html')

def registrar(request):
    ra=Raza.objects.all()
    est=Estado.objects.all()
    resp=False
    if request.POST:
        nombre=request.POST.get("nombre","")
        foto=request.POST.get("foto","")
        ra=request.POST.get("raza","")
        obj_raza=Raza.objects.get(name=ra)
        descripcion=request.POST.get("desc","")
        est=request.POST.get("estado","")
        obj_estado=Estado.objects.get(name=est)
        perro=Perro(
            name=nombre,
            foto=foto,
            raza=obj_raza,
            descripcion=descripcion,
            estado=obj_estado
        )
        perro.save()
        resp=True
    return render(request,'core/registrar.html',{'raza':ra,'estado':est,'respuesta':resp})

def solicitudadopcion(request):
    return render(request,'core/solicitudadopcion.html')
