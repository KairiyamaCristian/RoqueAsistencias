from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello word")

def login(request):
    return HttpResponse("esto es el login")

def registro_materias(request):
    return HttpResponse("esto es materias")

def registro_asistencia_por_materia(request):
    return HttpResponse("esto es registro de asistencia por materia")
