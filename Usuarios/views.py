from http import HTTPStatus
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from Usuarios.serializers import UsuarioSerializer
from Usuarios.models import Usuario

# Create your views here.


class Clase_ListadoTenants_Para_SuperAdmin(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        # Si es superAdmin → devuelve tenants
        if user.role == "superadmin":
            usuarios = Usuario.objects.filter(role="tenant").order_by("first_name")
            if usuarios.exists():
                usuarios_serializados = UsuarioSerializer(usuarios, many=True)
                return JsonResponse(
                    {"tenants": usuarios_serializados.data},
                    status=HTTPStatus.OK,
                    safe=False,
                )
            else:
                return JsonResponse(
                    {"estado": "Error", "mensaje": "No hay tenants registrados"},
                    status=HTTPStatus.BAD_REQUEST,
                )


class Clase_ListadoAdminsSucursal_Para_Tenant(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        user = request.user

        if user.role == "tenant":
            usuariosAdmins = Usuario.objects.filter(
                role="adminSucursal", sucursal__tenantId=user
            )
        if usuariosAdmins.exists():
            usuarios_serializados = UsuarioSerializer(usuariosAdmins, many=True)
            return JsonResponse(
                {"admins_sucursal": usuarios_serializados.data},
                status=HTTPStatus.OK,
                safe=False,
            )
        else:
            return JsonResponse(
                {
                    "estado": "Error",
                    "mensaje": "No hay administradores de sucursal registrados",
                },
                status=HTTPStatus.BAD_REQUEST,
            )


class Clase_ListadoCadetes_Para_Tenant(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        if user.role == "tenant":
            # Filtramos para obtener solo los cadetes creados por este tenant
            cadetes = Usuario.objects.filter(role="cadete", tenantId=user)

            if cadetes.exists():
                cadetes_serializados = UsuarioSerializer(cadetes, many=True)
                return JsonResponse(
                    {"cadetes": cadetes_serializados.data},
                    status=HTTPStatus.OK,
                    safe=False,
                )
            else:
                return JsonResponse(
                    {
                        "estado": "Error",
                        "mensaje": "No hay cadetes registrados para este tenant",
                    },
                    status=HTTPStatus.BAD_REQUEST,
                )
        else:
            return JsonResponse(
                {
                    "estado": "Error",
                    "mensaje": "Solo los tenants pueden ver sus cadetes",
                },
                status=HTTPStatus.FORBIDDEN,
            )


# # Si es tenant → devuelve admins de sucursales de sus sucursales
#         elif user.role == "tenant":
#             usuariosAdmins = Usuario.objects.filter(
#                 role="adminSucursal", sucursal__tenantId=user
#             )
#             if usuariosAdmins.exists():
#                 usuarios_serializados = UsuarioSerializer(usuariosAdmins, many=True)
#                 return JsonResponse(
#                     {"admins_sucursal": usuarios_serializados.data},
#                     status=HTTPStatus.OK,
#                     safe=False,
#                 )
#             else:
#                 return JsonResponse(
#                     {
#                         "estado": "Error",
#                         "mensaje": "No hay administradores de sucursal registrados",
#                     },
#                     status=HTTPStatus.BAD_REQUEST,
#                 )

#         # Si es adminSucursal → devuelve cadetes de su sucursal
#         elif user.role == "adminSucursal":
#             usuarios = Usuario.objects.filter(role="cadete", sucursal=user.sucursal)
#             if usuarios.exists():
#                 usuarios_serializados = UsuarioSerializer(usuarios, many=True)
#                 return JsonResponse(
#                     {"cadetes": usuarios_serializados.data},
#                     status=HTTPStatus.OK,
#                     safe=False,
#                 )
#             else:
#                 return JsonResponse(
#                     {"estado": "Error", "mensaje": "No hay cadetes registrados"},
#                     status=HTTPStatus.BAD_REQUEST,
#                 )

#         # Otros roles → sin permiso
#         return JsonResponse(
#             {"estado": "Error", "mensaje": "No tienes permiso para esta función"},
#             status=HTTPStatus.FORBIDDEN,
#         )
