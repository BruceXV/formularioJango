from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Genero , Alumno

from .forms import GeneroForm

# Create your views here.
def index(request):
    alumnos = Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request,"alumnos/index.html",context)

def crud(request):
    alumnos = Alumno.objects.all()
    context={"alumnos":alumnos}
    return render(request,"alumnos/alumnos_list.html",context)

def alumnosAdd(request):
    if request.method != "POST":
        #No es un post , por lo tanto se muestra el formulario para agregar
        generos = Genero.objects.all()
        context={"generos":generos}
        return render(request,"alumnos/alumnos_add.html",context)
    else:        
        #Es un post , por lo tanto se recuperan los datos del formulario
        #y se graban en la tabla
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        aPaterno = request.POST["paterno"]
        aMaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        activo = "1"

        objGenero = Genero.objects.get(id_genero = genero)
        obj=Alumno.objects.create(
            rut = rut,
            nombre = nombre,
            apellido_paterno = aPaterno,
            apellido_materno = aMaterno,
            fecha_nacimiento = fechaNac,
            id_genero = objGenero,
            telefono = telefono,
            email = email,
            direccion = direccion,
            activo=1
        )
        obj.save()
        context = {"mensaje":"Ok , datos guardados....."}
        return render(request,"alumnos/alumnos_add.html",context)

def alumnos_del(request):
    return "hola"

def alumnos_findEdit(request,pk):
    if pk != "":
        alumno=Alumno.objects.get(rut=pk)
        generos = Genero.objects.all()

        print(type(alumno.id_genero.genero))

        context = {'alumno':alumno,'generos':generos}

        if alumno:
            return render(request,"alumnos/alumnos_edit.html",context)
        else:
            context={"mensaje":"Error, rut no existe"}
            return render(request,"alumnos/alumnos_edit.html",context)

def alumnosUpdate(request):
   if request.method != "POST":
        #No es un post , por lo tanto se muestra el formulario para agregar
   
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        aPaterno = request.POST["paterno"]
        aMaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        activo = "1"

        objGenero = Genero.objects.get(id_genero = genero)
   
        alumno = Alumno()
        alumno.rut=rut
        alumno.nombre=nombre
        alumno.apellido_paterno=aPaterno
        alumno.apellido_materno=aMaterno
        alumno.fecha_nacimiento=fechaNac
        alumno.id_genero=objGenero
        alumno.telefono=telefono
        alumno.email=email
        alumno.direccion=direccion
        alumno.activo=1
        alumno.save()

        genero=Genero.objects.all()
        context={'mensaje':"OK, datos actualizados...",'generos':genero,'alumno':alumno}
        return render(request, 'alumnos/aumnos_edit.html', context)
   else:
       
       alumno = Alumno.objects.all()
       context={'alumno':alumno}
       return render(request, 'alumnos/alumnos_list.html', context)
   
def crud_generos(resquest):
    generos=Genero.objects.all()
    context = {'generos':generos}
    print("enviadoi datos generos_list")
    return render(resquest,"alumnos/generos_list.html", context)

def generosAdd(request):
    print("estoy en controlador generosAdd...")
    context={}

    if request.method == "POST":
        print("controlador es un post...")
        form = GeneroForm(request.POST)
        if form.is_valid:
            print("estoy en agregar, is_valid")
            form.save()

            #limpiar form
            form=GeneroForm()

            context={'mensaje':"Ok, datos grabados...","form":form}
            return render(request,"alumnos/generos_add.html",context)
        else:
            form = GeneroForm()
            context={'form':form}
            return render(request, 'alumnos/generos_add.html', context)


