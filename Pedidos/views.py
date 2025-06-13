from rest_framework import viewsets
from .models import Pedido
from .serializers import PedidoSerializer
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = [
        "estado",
        "fechaDeAsignacion",
        "zonaId",
        "cadeteId",
        "trackingNumber",
    ]
    ordering_fields = ["fechaDeAsignacion", "estado", "trackingNumber"]
    ordering = ["fechaDeAsignacion"]
