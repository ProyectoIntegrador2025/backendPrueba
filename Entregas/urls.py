from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EntregaViewSet

# Configura el router para Entregas
router = DefaultRouter()
router.register(r'entregas', EntregaViewSet)

urlpatterns = [
    path('API/Entregas/', include(router.urls)),
]
