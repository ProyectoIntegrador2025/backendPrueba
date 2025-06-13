from rest_framework import serializers
from .models import Entrega

class EntregaSerializer(serializers.ModelSerializer):
    
    # Aquí puedes acceder a los detalles del pedido
    pedido = serializers.ReadOnlyField(source='pedido.direccion')
    
    class Meta:
        model = Entrega
        fields = ('id', 'pedido', 'firmaDelReceptor', 'fechaDeEntrega', 'latitud', 'longitud')