
from django.db import models


class Materia(models.Model):
    nombre = models.CharField(max_length=20)
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=20)
    correo = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

class Alumno(models.Model):
    nombre = models.CharField(max_length=20)
    correo = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)

class Asistencia(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)

class Fecha(models.Model):
    tipo = models.CharField(max_length=20)
    asistencia = models.ForeignKey(Asistencia, on_delete=models.CASCADE)

class Estado(models.Model):
    tipo = models.CharField(max_length=20)
    asistencia = models.ForeignKey(Asistencia, on_delete=models.CASCADE)
