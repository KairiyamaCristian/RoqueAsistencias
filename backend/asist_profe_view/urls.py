from django.urls import path
from . import views

urlpatterns = [
    #asist_profe_view/
    path("", views.index, name="index"),
    #asist_profe_view/login/
    path("login/", views.login, name="login"),
    #asist_profe_view/materia/
    path("materia/", views.registro_materias, name="Materias"),
    #asist_profe_view/materia/1
    path("materia/<int:materia_id>/", views.registro_asistencia_por_materia, name="alumnos"),
]
#ver como hacer las partes de materia y alumnos