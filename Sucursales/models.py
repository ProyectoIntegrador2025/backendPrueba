from django.db import models
from Usuarios.models import Usuario

class Sucursal (models.Model) :
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True, null=False)
    direccion = models.CharField(max_length=250, unique=True, null=False)
    tenantId = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='sucursales_tenant')
    adminId = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='sucursales_admin')
    foto = models.ImageField(upload_to='sucursales/', null=True, blank=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta :
        db_table = 'Sucursales'
        verbose_name = 'Sucursal'
        verbose_name_plural = 'Sucursales'