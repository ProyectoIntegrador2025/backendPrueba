from http import HTTPStatus
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from django.http import JsonResponse
from Seguridad.LogInSerializer import UserLoginSerializer
from Usuarios.serializers import *
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from Usuarios.serializers import UsuarioSerializer


class Clase_Seguridad_Registro_Tenant(APIView):
    
    permission_classes = [IsAuthenticated]

    def post(self, request):
        
        if request.user.role != "superadmin":
            return JsonResponse(
                {"Estado": "Error", "Mensaje": "No tienes permiso para esta funcion"},
                status=HTTPStatus.FORBIDDEN,
            )
        
        serializer = RegistroTenantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                {"Estado": "OK", "Mensaje": "Usuario creado correctamente"},
                status=HTTPStatus.CREATED,
            )
        return JsonResponse(
            {"Estado": "Error", "Errores": serializer.errors},
            status=HTTPStatus.BAD_REQUEST,
        )

    # FALTA VERIFICAR EL MAIL


class Clase_Seguridad_Registro_Admin_Sucursal(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        if request.user.role != "tenant":
            return JsonResponse(
                {"Estado": "Error", "Mensaje": "No tienes permiso para esta funcion"},
                status=HTTPStatus.FORBIDDEN,
            )

        serializer = RegistroAdminSucursalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                {"Estado": "OK", "Mensaje": "Usuario creado correctamente"},
                status=HTTPStatus.CREATED,
            )
        return JsonResponse(
            {"Estado": "Error", "Errores": serializer.errors},
            status=HTTPStatus.BAD_REQUEST,
        )

        # FALTA VERIFICAR EL MAIL


class Clase_Seguridad_Registro_Cadete(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        if request.user.role != "tenant":
            return JsonResponse(
                {"Estado": "Error", "Mensaje": "No tienes permiso para esta funcion"},
                status=HTTPStatus.FORBIDDEN,
            )

        serializer = RegistroCadeteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                {"Estado": "OK", "Mensaje": "Usuario creado correctamente"},
                status=HTTPStatus.CREATED,
            )
        return JsonResponse(
            {"Estado": "Error", "Errores": serializer.errors},
            status=HTTPStatus.BAD_REQUEST,
        )

    # FALTA VERIFICAR EL MAIL


class Clase_Seguridad_Validacion(APIView):

    def get(sel, request, token):
        pass


class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_data = UsuarioSerializer(serializer.validated_data["user"]).data
        return JsonResponse(
            {
                "user": user_data,
                "access_token": serializer.validated_data["access"],
                "refresh_token": serializer.validated_data["refresh"],
                "rol": user_data["role"]
            }
        )


class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        refresh_token = request.data.get(
            "refresh_token"
        )  # fíjate que el campo se llama "refresh_token"
        if not refresh_token:
            return JsonResponse(
                {"detail": "El refresh_token es requerido"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()  # Aquí invalidamos el refresh token
            return JsonResponse(
                {"detail": "Logout exitoso"}, status=HTTPStatus.RESET_CONTENT
            )
        except (TokenError, InvalidToken):
            return JsonResponse(
                {"detail": "Token inválido o expirado"},
                status=HTTPStatus.BAD_REQUEST,
            )
