from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Digimon API",
      default_version='v1',
      description="Api que contiene la data la wiki de digimon.net pagina oficial de digimon",
      terms_of_service="Digimon y otros medios relacionados con la franquicia son marcas registradas de Bandai, esta api es solo para el ambito educativo",
      contact=openapi.Contact(email="puentesjs903@gmail.com"),
      license=openapi.License(name='http://creativecommons.org/licenses/by/4.0/'),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('routers/', include('api.urls')),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
