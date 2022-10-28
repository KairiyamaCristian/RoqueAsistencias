from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from asist_profe_view.models import Materia,Alumno

from .models import Materia
# Create your views here.
def index(request):
# class Asistencia(models.Model):
    return HttpResponse("Hello word")

def login(request):
    return HttpResponse("esto es el login nuevo")

def registro_materias(request):
    latest_materia_list= Materia.objects.all()
    return render(request,"asistencia/materias.html",{"latest_materia_list": latest_materia_list})

def registro_asistencia_por_materia(request, materia_id):
    materia = get_object_or_404(Materia, pk=materia_id)
    return render(request,"asistencia/alumnos.html",{"materia": materia})
