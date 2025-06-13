from django.urls import path
from .views import *

urlpatterns = [
    path('/Registro/Tenant', Clase_Seguridad_Registro_Tenant.as_view()),
    path('/Registro/AdminSucursal', Clase_Seguridad_Registro_Admin_Sucursal.as_view()),
    path('/Registro/Cadete', Clase_Seguridad_Registro_Cadete.as_view()),
    path('/Verificacion/<str:token>', Clase_Seguridad_Validacion.as_view()),
    path("/LogIn", LoginAPIView.as_view(), name="user-login"),
    path('/LogOut', LogoutAPIView.as_view(), name='logout'),
]