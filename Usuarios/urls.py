from django.urls import path
from .views import *

urlpatterns = [
    path('Usuario/ListadoSuperAdmin', Clase_ListadoTenants_Para_SuperAdmin.as_view()),
    path('Usuarios/ListadoAdminsSucursal', Clase_ListadoAdminsSucursal_Para_Tenant.as_view()),
    path('Usuarios/ListadoAdminsSucursal', Clase_ListadoCadetes_Para_Tenant.as_view())
]