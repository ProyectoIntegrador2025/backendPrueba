from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UsuarioManager

ROLE_CHOICES = (
    ("superadmin", "Super_Administrador"),
    ("adminSucursal", "Administrador_De_Sucursal"),
    ("cadete", "Cadete"),
    ("tenant", "Tenant"),
)

class Usuario(AbstractUser):
    username = None  
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    foto = models.CharField(max_length=100, null=True, blank=True)
    
    zona = models.ForeignKey("Zonas.Zona", on_delete=models.SET_NULL, null=True, blank=True)
    sucursal = models.ForeignKey("Sucursales.Sucursal", on_delete=models.SET_NULL, null=True, blank=True)
    tenantId = models.ForeignKey("Usuarios.Usuario", on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(unique=True, null=False, blank=False, max_length=254)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UsuarioManager()
    
    def __str__(self):
        return self.first_name
    
    class Meta :
        db_table = 'Usuarios'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
