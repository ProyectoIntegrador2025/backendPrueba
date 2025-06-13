from rest_framework import serializers
from .models import Zona

class ZonaSerializer(serializers.ModelSerializer):
    sucursal = serializers.ReadOnlyField(source='sucursalId.nombre')

    class Meta:
        model = Zona
        fields = (
            'id',
            'nombre',
            'sucursalId',  # para escritura
            'sucursal',    # solo lectura
        )

    def validate_nombre(self, value):
        # Si estamos actualizando, excluimos el objeto actual de la validación
        zona_id = self.instance.id if self.instance else None
        if Zona.objects.exclude(id=zona_id).filter(nombre=value).exists():
            raise serializers.ValidationError("Ya existe una zona con ese nombre.")
        return value
