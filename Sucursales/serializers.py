from rest_framework import serializers
from .models import *
import os


class SucursalSerializer(serializers.ModelSerializer):
    admin = serializers.ReadOnlyField(source="adminId.first_name")
    tenant = serializers.ReadOnlyField(source="tenantId.first_name")
    foto = serializers.ImageField(use_url=True, required=False, allow_null=True)

    class Meta:
        model = Sucursal
        fields = (
            "id",
            "nombre",
            "direccion",
            "tenantId",
            "adminId",  # <- Campos para escritura
            "tenant",
            "admin",  # <- Campos solo lectura
            "foto",
        )

    def validate(self, data):
        tenant = data.get("tenantId")
        admin = data.get("adminId")

        if tenant.role != "tenant":
            raise serializers.ValidationError(
                {"tenantId": 'El usuario seleccionado no tiene rol tenant.'}
            )

        if admin.role != "adminSucursal":
            raise serializers.ValidationError(
                {"adminId": 'El usuario seleccionado no tiene rol adminSucursal.'}
            )
        
        if admin.sucursales_admin.exists() :
            raise serializers.ValidationError(
                {"adminId": "El usuario seleccionado ya tiene una sucursal asignada."}
            )

        return data

    def get_foto(self, obj):
        base_url = os.getenv("BASE_URL")
        return f"{base_url}uploads/sucursales/{obj.foto}"
