from rest_framework import serializers
from .models import *
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from Usuarios.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):

    foto = serializers.SerializerMethodField()

    class Meta:
        model = Usuario
        fields = ["id", "email", "first_name", "last_name", "role", "foto"]

    def get_foto(self, obj):  # en el obj tenes disponibles todos los campos del modelo
        return f"http://127.0.0.1:8000/uploads/usuarios/{obj.foto}"  # HAY QUE CAMBIAR LA URL BASE


class RegistroTenantSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Usuario
        fields = [
            "first_name",
            "last_name",
            "email",
            "password",
            "password2",
            "role",
        ]

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Las contraseñas no coinciden."}
            )
        return attrs

    def create(self, validated_data):
        # Si no se proporcionó un username, lo generamos
        username = validated_data.get("username", None)
        role = validated_data.get("role", "tenant")
        if not username:
             username = validated_data["email"].split("@")[
                 0
            ]  # Usamos el correo como base

        validated_data.pop("password2")
        user = Usuario.objects.create(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            username=username,  # Usamos el username generado o proporcionado
            role=role,
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class RegistroAdminSucursalSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Usuario
        fields = [
            "first_name",
            "last_name",
            "email",
            "password",
            "password2",
            "role",
        ]

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Las contraseñas no coinciden."}
            )
        return attrs

    def create(self, validated_data):
        # Si no se proporcionó un username, lo generamos
        username = validated_data.get("username", None)
        role = validated_data.get("role", "adminSucursal")
        if not username:
            username = validated_data["email"].split("@")[
                0
            ]  # Usamos el correo como base

        validated_data.pop("password2")
        user = Usuario.objects.create(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            username=username,  # Usamos el username generado o proporcionado
            role=role,
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class RegistroCadeteSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Usuario
        fields = [
            "first_name",
            "last_name",
            "email",
            "password",
            "password2",
            "role",
            "zona",
            "sucursal",
        ]

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Las contraseñas no coinciden."}
            )

        # Forzamos que el rol sea "cadete"
        if attrs.get("role") != "cadete":
            raise serializers.ValidationError(
                {"role": "Este formulario solo permite registrar cadetes."}
            )

        # Validamos zona y sucursal
        if not attrs.get("zona"):
            raise serializers.ValidationError(
                {"zona": "La zona es obligatoria para un cadete."}
            )
        if not attrs.get("sucursal"):
            raise serializers.ValidationError(
                {"sucursal": "La sucursal es obligatoria para un cadete."}
            )

        return attrs

    def create(self, validated_data):
        request = self.context.get("request")
        tenant = request.user

        # Validamos que el creador sea un tenant
        if tenant.role != "tenant":
            raise serializers.ValidationError(
                {"autorización": "Solo los tenants pueden crear cadetes."}
            )

        validated_data.pop("password2")
        password = validated_data.pop("password")
        username = (
            validated_data.get("username") or validated_data["email"].split("@")[0]
        )

        user = Usuario.objects.create(
            username=username,
            role="cadete",
            tenantId=tenant,
            **validated_data,
        )
        user.set_password(password)
        user.save()
        return user