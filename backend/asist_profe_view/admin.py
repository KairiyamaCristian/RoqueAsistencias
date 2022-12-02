from django.contrib import admin
from .models import Materia, Alumno, Profesor, Usuario, Fecha, Estado, Asistencia, Materia_Alumno

class Materia_AlumnoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "materia")
    list_filter = ["materia"]

admin.site.register([Materia, Alumno, Profesor, Usuario, Fecha, Estado, 
Asistencia])
admin.site.register(Materia_Alumno,Materia_AlumnoAdmin)
