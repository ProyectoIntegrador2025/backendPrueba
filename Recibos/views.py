from rest_framework import viewsets
from .models import Recibo
from .serializers import ReciboSerializer
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter

class ReciboViewSet(viewsets.ModelViewSet):
    queryset = Recibo.objects.all()
    serializer_class = ReciboSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['fecha', 'estaPago', 'tenantId']
