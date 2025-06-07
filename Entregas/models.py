from django.db import models
from Pedidos.models import Pedido

class Entrega (models.Model) :
    id = models.BigAutoField(primary_key=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    firmaDelReceptor = models.CharField(max_length=50, null=False, unique=False)
    fechaDeEntrega =  models.DateTimeField(auto_now=True)
    latitud = models.FloatField(null=False, unique=False)
    longitud = models.FloatField(null=False, unique=False)
    
    def __str__(self):
        return self.firmaDelReceptor, self.fechaDeEntrega, self.pedido
    
    class Meta :
        db_table = 'Entregas'
        verbose_name = 'Entrega'
        verbose_name_plural = 'Entregas'
    