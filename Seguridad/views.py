from http import HTTPStatus
from django.http import JsonResponse
from rest_framework.views import APIView
from Usuarios.serializers import *


class Clase_Seguridad_Registro_Tenant(APIView):

    def post(self, request):
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

    def post(self, request):
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

    def post(self, request):
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

    def get(self, request, token):
        pass


class Clase_Seguridad_LogIn(APIView):

    def post(self, request):
        pass
