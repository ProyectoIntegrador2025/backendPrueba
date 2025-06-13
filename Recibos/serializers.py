from rest_framework import serializers
from .models import Recibo


class ReciboSerializer(serializers.ModelSerializer):
    tenant = serializers.ReadOnlyField(source="tenantId.first_name")  # solo lectura

    class Meta:
        model = Recibo
        fields = ("id", "tenantId", "tenant", "monto", "fecha", "estaPago")
