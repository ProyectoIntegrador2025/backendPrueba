from rest_framework import viewsets
from .models import Entrega
from .serializers import EntregaSerializer
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter


class EntregaViewSet(viewsets.ModelViewSet):
    queryset = Entrega.objects.all()
    serializer_class = EntregaSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["fechaDeEntrega"]
    ordering_fields = ["fechaDeEntrega", "latitud", "longitud"]
    ordering = ["fechaDeEntrega"]
