from django.urls import path
from .views import *

urlpatterns = [
    path('Usuario', Clase_Usuario.as_view())
]