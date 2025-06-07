from django.urls import path
from .views import *

urlpatterns = [
    path('Sucursal', Clase_Sucursal.as_view())
]