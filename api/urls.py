from rest_framework import routers
from .views import (DigimonViewSet, TrainingIViewSet, TrainingIIViewSet, RookieViewSet,
                    ChampionViewSet, UltimateViewSet, MegaViewSet, ArmorViewSet, HybridViewSet,
                    UnknownViewSet, AttributeViewSet, LevelViewSet, TypeDViewSet, SpecialMoveViewSet)

router = routers.DefaultRouter()

router.register('api/digimon', DigimonViewSet, 'digimons')
router.register('api/training_i', TrainingIViewSet, 'trainingi')
router.register('api/training_ii', TrainingIIViewSet, 'trainingii')
router.register('api/rookie', RookieViewSet, 'rookie')
router.register('api/champion', ChampionViewSet, 'champion')
router.register('api/ultimate', UltimateViewSet, 'ultimate')
router.register('api/mega', MegaViewSet, 'mega')
router.register('api/armor', ArmorViewSet, 'armor')
router.register('api/hybrid', HybridViewSet, 'hybrid')
router.register('api/unknown', UnknownViewSet, 'unknown')
router.register('api/attribute', AttributeViewSet, 'attribute')
router.register('api/level', LevelViewSet, 'level')
router.register('api/type', TypeDViewSet, 'type')
router.register('api/specialmove', SpecialMoveViewSet, 'specialmove')


urlpatterns = router.urls
