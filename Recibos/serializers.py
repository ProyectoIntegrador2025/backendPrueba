from rest_framework import serializers
from .models import *

class RecetaSerializer (serializers.ModelSerializer) :
    
    tenant = serializers.ReadOnlyField(source='tenantId.first_name')
    
    class Meta :
        model = Recibo
        fields = ('id', 'tenant', 'monto', 'fecha', 'estaPago')