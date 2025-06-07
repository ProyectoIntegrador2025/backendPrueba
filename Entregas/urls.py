from django.urls import path
from .views import *

urlpatterns = [
    path('Entrega', Clase_Entrega.as_view())
]