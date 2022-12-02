
from django.contrib import admin
from .models import Materia, Alumno, Profesor, Usuario, Fecha, Estado, Asistencia, Materia_Alumno

admin.site.register([Materia, Alumno, Profesor, Fecha, Estado, Asistencia, Usuario, Materia_Alumno])

