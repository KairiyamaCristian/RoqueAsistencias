from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from asist_profe_view.models import Materia,Alumno,Profesor,Usuario,Fecha,Estado,Asistencia, Materia_Alumno

from .models import Materia
# Create your views here.
def index(request):
# class Asistencia(models.Model):
    return render(request, "asistencia/login.html")

def signup(request):
    return render(request, "asistencia/signup.html")

def login(request):
    return render(request, "asistencia/home.html")

def registro_materias(request):
    latest_materia_list= Materia.objects.all()
    return render(request,"asistencia/materias.html",{"latest_materia_list": latest_materia_list})

def registro_asistencia_por_materia(request, materia_id):
    materia = get_object_or_404(Materia, pk=materia_id)
    # materia = Alumno.objects.all()
    return render(request,"asistencia/matematica.html",{"materia": materia})

    # return HttpResponse("Esto es el registro de asistencia por materia") FUNCIONA


# def insercion(request):
#     materia_alumno= request.POST("")
#     fecha= request.POST("")
#     estado= request.POST("")
    
#     asistencia=Asistencia.objects.create(materia_alumno=,estado=)
#     # materia = Alumno.objects.all()
#     return redirect("/")
