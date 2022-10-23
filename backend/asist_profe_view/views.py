from django.shortcuts import render

from django.http import HttpResponse

from backend.asist_profe_view.models import Materia
# Create your views here.
def index(request):
    return HttpResponse("Hello word")

def login(request):
    return HttpResponse("esto es el login")

def registro_materias(request, materia_id):
    return HttpResponse(f"esta es la materia {materia_id}")

def registro_asistencia_por_materia(request, alumno_id):
    return HttpResponse("esto es el id del alumno {alumno_id}")
