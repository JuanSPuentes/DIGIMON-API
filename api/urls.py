from rest_framework import routers
from .views import DigimonViewSet

router = routers.DefaultRouter()

router.register('api/digimon', DigimonViewSet, 'digimons')

urlpatterns = router.urls
