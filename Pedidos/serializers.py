from rest_framework import serializers
from .models import Pedido


class PedidoSerializer(serializers.ModelSerializer):

    cadete = serializers.ReadOnlyField(source="cadeteId.first_name")
    zona = serializers.ReadOnlyField(source="zonaId.nombre")

    class Meta:
        model = Pedido
        fields = (
            "id",
            "direccion",
            "emailCliente",
            "telefonoCliente",
            "cedulaCliente",
            "fechaDeAsignacion",
            "estado",
            "trackingNumber",
            "empresaOrigen",
            "cadete",  # solo lectura
            "zona",  # solo lectura
        )
