import datetime

from email.policy import default
from django.db import models
from django.utils import timezone

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    correo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    contraseña= models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre    

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    contraseña= models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre  

class Materia(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nombre

class Alumno(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nombre
    

class Materia_Alumno(models.Model):
    nombre = models.CharField(max_length=20)
    alumno = models.ForeignKey(Alumno, on_delete = models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.nombre

class Fecha(models.Model):
    nombre = models.CharField(max_length=20)
    fecha = models.DateTimeField("Fecha de publicacion")
    
    def __str__(self) -> str:
        return self.nombre

    def fecha_reciente(self):
        return self.fecha >= timezone.now() - datetime.timedelta(days=1)

class Estado(models.Model):
    tipo = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.tipo

class Asistencia(models.Model):
    codigo = models.CharField(max_length=20)
    alumno = models.ForeignKey(Materia_Alumno, on_delete=models.CASCADE)
    fecha = models.ForeignKey(Fecha, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.codigo
