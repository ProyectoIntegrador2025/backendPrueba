from django.urls import path
from .views import *

urlpatterns = [
    path('Recibo', Clase_Recibo.as_view())
]