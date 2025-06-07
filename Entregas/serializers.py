from rest_framework import serializers
from .models import *

class RecetaSerializer (serializers.ModelSerializer) :
    
    pedido = serializers.ReadOnlyField(source='pedido.direccion')
    
    class Meta :
        model = Pedido
        fields = ('id', 'pedido', 'firmaDelReceptor', 'fechaDeEntrega', 'latitud', 'longitud')