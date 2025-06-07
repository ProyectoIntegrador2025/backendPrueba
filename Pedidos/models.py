from django.db import models, transaction, IntegrityError
import random
from Usuarios.models import Usuario
from Zonas.models import Zona

ORDER_STATE_TYPES = {
    "pendiente": "Pendiente",
    "en_transito": "En transito",
    "entregado": "Entregado",
    "cancelado": "Cancelado"
}

ORDER_STATE_CHOICES = (
    ("pendiente", "Pendiente"),
    ("en_transito", "En transito"),
    ("entregado", "Entregado"),
    ("cancelado", "Cancelado"),
)


def generar_tracking_number():
    return str(random.randint(10000000, 99999999))


class Pedido(models.Model):
    id = models.BigAutoField(primary_key=True)
    direccion = models.CharField(max_length=250)
    emailCliente = models.EmailField(max_length=100)
    telefonoCliente = models.CharField(max_length=45, null=True, blank=True)
    cedulaCliente = models.CharField(max_length=45, unique=False, null=True)
    fechaDeAsignacion = models.DateTimeField()
    estado = models.CharField(
        max_length=16, choices=ORDER_STATE_CHOICES, default="pending"
    )
    trackingNumber = models.CharField(
        max_length=8, unique=True, editable=False, blank=True, null=True
    )
    zonaId = models.ForeignKey(Zona, on_delete=models.CASCADE, related_name='Pedidos')
    cadeteId = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='Pedidos_Asignados') #EL .SET_NULL, hace que si se le saca el cadete al pedido no se borre el pedido y se le pueda asignar otro cadete
    empresaOrigen = models.CharField(max_length=25, unique=False)

    def save(self, *args, **kwargs):
        if not self.trackingNumber:
            for _ in range(10):
                nuevo_tracking = generar_tracking_number()
                if not Pedido.objects.filter(trackingNumber=nuevo_tracking).exists():
                    self.trackingNumber = nuevo_tracking
                    break
            else:
                raise ValueError(
                    "No se pudo generar un número de tracking único después de varios intentos."
                )

        try:
            with transaction.atomic():
                super().save(*args, **kwargs)
        except IntegrityError:
            raise ValueError("Error: El número de tracking ya existe.")

    def __str__(self):
        return self.direccion
    
    class Meta :
        db_table = 'Pedidos'
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
