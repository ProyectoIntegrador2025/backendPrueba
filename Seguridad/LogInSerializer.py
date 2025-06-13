# from rest_framework import serializers
# from django.contrib.auth import authenticate
# from django.conf import settings
# from datetime import datetime, timedelta
# import time
# from jose import jwt
# from Usuarios.models import Usuario


# class LoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(write_only=True)

#     def validate(self, data):
#         email = data.get("email")
#         password = data.get("password")

#         if not email or not password:
#             raise serializers.ValidationError("Email y contraseña son requeridos.")

#         try:
#             user = Usuario.objects.get(email=email)
#         except Usuario.DoesNotExist:
#             raise serializers.ValidationError("Credenciales incorrectas.")

#         auth = authenticate(email=email, password=password)

#         if auth is None:
#             raise serializers.ValidationError("Credenciales incorrectas.")

#         fecha = datetime.now()
#         despues = fecha + timedelta(days=1)
#         payload = {
#             "id": user.id,
#             "ISS": "http://127.0.0.1:8000",
#             "iat": int(time.time()),
#             "ext": int(datetime.timestamp(despues)),
#         }

#         token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS512")

#         return {
#             "id": user.id,
#             "nombre": user.first_name,
#             "token": token,
#         }


# from rest_framework import serializers
# from django.contrib.auth import authenticate
# from Usuarios.models import Usuario
# from rest_framework.exceptions import AuthenticationFailed
# from rest_framework_simplejwt.tokens import RefreshToken

# class UserLoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(write_only=True)

#     def validate(self, data):
#         email = data.get("email")
#         password = data.get("password")

#         user = authenticate(username=email, password=password)

#         if user is None:
#             raise AuthenticationFailed("Email o contraseña incorrectos.")
#         if not user.is_active:
#             raise AuthenticationFailed("Usuario inactivo.")

#         refresh = RefreshToken.for_user(user)
#         return {
#             "user": user,
#             "refresh": str(refresh),
#             "access": str(refresh.access_token),
#         }

from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

User = get_user_model()


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise AuthenticationFailed("Email o contraseña incorrectos.")

        if not user.check_password(password):
            raise AuthenticationFailed("Email o contraseña incorrectos.")

        if not user.is_active:
            raise AuthenticationFailed("Usuario inactivo.")

        refresh = RefreshToken.for_user(user)
        return {
            "user": user,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }