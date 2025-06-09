from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE_CHOICES = (
    ("supeadmin", "Super_Administrador"),
    ("adminSucursal", "Administrador_De_Sucursal"),
    ("cadete", "Cadete"),
    ("tenant", "Tenant"),
)

class Usuario(AbstractUser):
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    foto = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.first_name
    
    class Meta :
        db_table = 'Usuarios'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
