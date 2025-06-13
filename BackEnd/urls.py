from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

#SWAGGER
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Tesis",
        default_version='V1',
        description="API para la tesis",
        terms_of_service="http://127.0.0.1:8000/Documentacion/",
        contact=openapi.Contact(email="camachopanizza@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('API/Usuarios/', include('Usuarios.urls')),
    
    path('API/Entregas/', include('Entregas.urls')),
    
    path('API/Sucursales/', include('Sucursales.urls')),
    
    path('API/Zonas/', include('Zonas.urls')),
    
    path('API/Pedidos/', include('Pedidos.urls')),
    
    path('API/Recibos/', include('Recibos.urls')),
    
    path('API/Seguridad', include('Seguridad.urls')),
    
    #SWAGGER
    path('Documentacion<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    
    path('Documentacion/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-json-ui'),
    
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)