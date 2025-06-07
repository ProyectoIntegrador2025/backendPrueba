from django.db import models
from Usuarios.models import Usuario


class Recibo (models.Model) :
    id = models.BigAutoField(primary_key=True)
    tenantId = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='Recibos') #ESE RELATED NAME LO QUE HACE ES QUE HACIENDO usuario.recibos.all() nos da la lista de recibos del usuario
    monto = models.FloatField(null=False, unique=False)
    fecha = models.DateTimeField(null=False, unique=False)
    estaPago = models.BooleanField(default=False, null=False, unique=False)
    
    def __str__(self):
        return self.estaPago
    
    class Meta :
        db_table = 'Recibos'
        verbose_name = 'Recibo'
        verbose_name_plural = 'Recibos'