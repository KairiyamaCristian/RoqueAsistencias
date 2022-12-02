from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from asist_profe_view.models import Materia,Alumno,Profesor,Fecha,Estado,Asistencia

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
