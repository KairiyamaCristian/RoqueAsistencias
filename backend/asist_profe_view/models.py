
from email.policy import default
from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=20)
    correo = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre    

class Materia(models.Model):
    nombre = models.CharField(max_length=20)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombre
    
class Alumno(models.Model):
    nombre = models.CharField(max_length=20)
    materia = models.ForeignKey(Materia, on_delete = models.CASCADE)
    asistencia = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.nombre

class Fecha(models.Model):
    tipo = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.tipo

class Estado(models.Model):
    tipo = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.tipo

class Asistencia(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    fecha = models.ForeignKey(Fecha, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)


