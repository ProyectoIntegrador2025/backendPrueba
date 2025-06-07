from rest_framework import serializers
from .models import *

class ZonaSerializer (serializers.ModelSerializer) :
    
    sucursal = serializers.ReadOnlyField(source='sucursalId.nombre')

    
    class Meta :
        model = Zona
        fields = ('id', 'nombre')