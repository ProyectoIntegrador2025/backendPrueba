from rest_framework import serializers
from .models import *

class RecetaSerializer (serializers.ModelSerializer) :
    
    foto = serializers.SerializerMethodField()
    
    class Meta :
        model = Usuario
        fields = ('id', 'first_name', 'last_name', 'email', 'foto')
    
    def get_foto (self, obj) : #en el obj tenes disponibles todos los campos del modelo
        return f"http://127.0.0.1:8000/uploads/usuarios/{obj.foto}" #HAY QUE CAMBIAR LA URL BASE