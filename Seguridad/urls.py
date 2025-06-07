from django.urls import path
from .views import *

urlpatterns = [
    path('/Registro', Clase_Seguridad_Registro.as_view()),
    path('/Verificacion/<str:token>', Clase_Seguridad_Validacion.as_view()),
    path('/LogIn', Clase_Seguridad_LogIn.as_view()),
]