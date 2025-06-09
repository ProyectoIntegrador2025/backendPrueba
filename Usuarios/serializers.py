from rest_framework import serializers
from .models import *
from django.contrib.auth.password_validation import validate_password


class UsuarioSerializer(serializers.ModelSerializer):

    foto = serializers.SerializerMethodField()


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
            "username",  # Aseguramos que esté en fields
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
            "username",  # Aseguramos que esté en fields
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
            "username",  # Aseguramos que esté en fields
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
        role = validated_data.get("role", "cadete")
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

    class Meta:
        model = Usuario
        fields = ("id", "first_name", "last_name", "email")

    def get_foto(self, obj):  # en el obj tenes disponibles todos los campos del modelo
        return f"http://127.0.0.1:8000/uploads/usuarios/{obj.foto}"  # HAY QUE CAMBIAR LA URL BASE
