from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PedidoViewSet

# Configura el router para Pedidos
router = DefaultRouter()
router.register(r'pedidos', PedidoViewSet)

urlpatterns = [
    path('API/Pedidos/', include(router.urls)),
]