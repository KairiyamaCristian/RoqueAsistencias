from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("login/materia/", views.registro_materias, name="Materias"),
    path("login/materia/<int:alumno_id>/", views.registro_asistencia_por_materia, name="Alumnos"),
]