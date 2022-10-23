
from django.contrib import admin
from .models import Materia, Profesor, Alumno, Asistencia, Fecha, Estado


admin.site.register([Materia, Profesor, Alumno, Asistencia, Fecha, Estado])

