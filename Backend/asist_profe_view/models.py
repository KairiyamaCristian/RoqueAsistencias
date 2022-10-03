
from django.db import models

class Materia(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.nombre
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    correo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombre

class Alumno(models.Model):
    nombre = models.CharField(max_length=30)
    correo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre

class Asistencia(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)

class Fecha(models.Model):
    tipo = models.CharField(max_length=30)
    asistencia = models.ForeignKey(Asistencia, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.tipo
class Estado(models.Model):
    tipo = models.CharField(max_length=30)
    asistencia = models.ForeignKey(Asistencia, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.tipo
