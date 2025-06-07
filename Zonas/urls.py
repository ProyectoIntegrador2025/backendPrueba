from django.urls import path
from .views import *

urlpatterns = [
    path('Zona', Clase_Zona.as_view())
]