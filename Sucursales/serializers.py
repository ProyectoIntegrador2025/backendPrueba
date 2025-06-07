from rest_framework import serializers
from .models import *

class RecetaSerializer (serializers.ModelSerializer) :
    
    admin = serializers.ReadOnlyField(source='adminId.first_name')
    tenant = serializers.ReadOnlyField(source='tenantId.first_name')
    foto = serializers.SerializerMethodField()
    
    class Meta :
        model = Sucursal
        fields = ('id', 'nombre', 'direccion', 'tenant', 'admin', 'foto')
    
    def get_foto (self, obj) : #en el obj tenes disponibles todos los campos del modelo
        return f"http://127.0.0.1:8000/uploads/sucursales/{obj.foto}" #HAY QUE CAMBIAR LA URL BASE