from django.db import models
from Sucursales.models import Sucursal

class Zona (models.Model) :
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=250, unique=False, null=False)
    sucursalId = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
    class Meta :
        db_table = 'Zonas'
        verbose_name = 'Zona'
        verbose_name_plural = 'Zonas'