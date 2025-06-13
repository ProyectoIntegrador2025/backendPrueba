from rest_framework import viewsets
from .models import Zona
from .serializers import ZonaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class ZonaViewSet(viewsets.ModelViewSet):
    queryset = Zona.objects.all()
    serializer_class = ZonaSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ["nombre", "sucursalId"]
    ordering_fields = ['nombre', 'sucursalId']
    ordering = ['nombre']
    search_fields = ["nombre", "direccion", "adminId", "tenantId"]