from .models import Sucursal
from .serializers import SucursalSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
import os
from django.conf import settings
from django.http.response import JsonResponse
from http import HTTPStatus
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated


class SucursalViewSet(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    #AYTHENTICATION BEGINS
    permission_classes = [IsAuthenticated]
    #AYTHENTICATION ENDS
    serializer_class = SucursalSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ["nombre", "direccion", "tenantId", "adminId"]
    ordering_fields = ["nombre", "direccion", "adminId", "tenantId"] #TE DA LAS CHANCES POR LO QUE PODES ORDENAR
    ordering = ["nombre"] #ORDENA POR DEFECTO POR EL NOMBRE
    search_fields = ["nombre", "direccion", "adminId", "tenantId"]
    parser_classes = [MultiPartParser, FormParser]  # Para permitir subir archivos

    @action(detail=True, methods=["post"])
    def subir_foto(self, request, pk=None):
        sucursal = self.get_object()
        archivo = request.FILES.get("foto")

        if not archivo:
            return JsonResponse(
                {"error": "No se envió ningún archivo."},
                HTTPStatus.BAD_REQUEST,
            )

        # Guardar manualmente el archivo
        nombre_archivo = archivo.name
        ruta_destino = os.path.join(settings.MEDIA_ROOT, "sucursales", nombre_archivo)

        with open(ruta_destino, "wb+") as destino:
            for chunk in archivo.chunks():
                destino.write(chunk)

        # Guardar el nombre en el campo
        sucursal.foto = nombre_archivo
        sucursal.save()

        return JsonResponse(
            {"mensaje": "Imagen subida y guardada correctamente."}, status=HTTPStatus.OK
        )

    @action(detail=True, methods=["delete"])
    def eliminar_admin(self, request, pk=None):
        sucursal = self.get_object()

        # Verificar si tiene un admin asignado
        if sucursal.adminId:
            # Establecer adminId a NULL sin eliminar el admin de la base de datos
            sucursal.adminId = None
            sucursal.save()

            # Esto debería establecer adminId a NULL gracias a on_delete=models.SET_NULL
            return JsonResponse(
                {"mensaje": "Admin desvinculado y campo adminId actualizado a NULL."},
                status=HTTPStatus.OK,
            )
        else:
            return JsonResponse(
                {"error": "Esta sucursal no tiene un admin asignado."},
                status=HTTPStatus.BAD_REQUEST,
            )
