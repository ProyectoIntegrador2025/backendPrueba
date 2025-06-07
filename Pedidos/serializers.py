from rest_framework import serializers
from .models import *

class RecetaSerializer (serializers.ModelSerializer) :
    
    cadete = serializers.ReadOnlyField(source='cadeteId.first_name')
    zona = serializers.ReadOnlyField(source='zona.nombre')
    
    class Meta :
        model = Pedido
        fields = ('id', 'direccion', 'emailCliente', 'telefonoCliente', 'cedulaCliente', 'fechaDeAsignacion', 'estado', 'trackingNumber', 'empresaOrigen', 'cadete', 'zona')