from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ZonaViewSet
from .views import *

router = DefaultRouter()
router.register(r'zonas', ZonaViewSet, basename='zona')

urlpatterns = [
    path('', include(router.urls)),
]