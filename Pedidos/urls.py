from django.urls import path
from .views import *

urlpatterns = [
    path('Pedido', Clase_Pedido.as_view())
]