from api import models
from rest_framework import viewsets, permissions
from .serializers import (DigimonSerializer, TrainingISerializer, TrainingIISerializer,RookieSerializer,
                          ChampionSerializer, UltimateSerializer, MegaSerializer, ArmorSerializer,
                          HybridSerializer, UnknownSerializer, AttributeSerializer, LevelSerializer,
                          TypeDSerializer, SpecialMoveSerializer)
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .mixins import MultipleFieldLookupMixin, MultipleFieldLookupMixin_2
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100



class DigimonViewSet(MultipleFieldLookupMixin,viewsets.ModelViewSet):
    queryset = models.Digimons.objects.all().order_by('name')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = DigimonSerializer
    pagination_class = StandardResultsSetPagination
    lookup_fields = ['name', 'id']

    
    def retrieve(self, request, *args, **kwargs):   
        """
        or you can use /{name}
        Example ---> /Alphamon   this can list multiple objects
        """
        instance = self.get_object()
        data = []
        if type(instance) == list:
            for i in instance:
                    json_ = {}
                    json_['id'] = i.id
                    json_['name'] = i.name
                    json_['href'] = i.href
                    json_['level'] = i.level
                    data.append(json_)
            return Response(data)
        else:
            serializer = self.get_serializer(instance)
        return Response(serializer.data)



class TrainingIViewSet(MultipleFieldLookupMixin_2,viewsets.ModelViewSet):
    queryset = models.TrainingI.objects.all().order_by('id')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = TrainingISerializer
    pagination_class = StandardResultsSetPagination
    lookup_fields = ['name', 'id']



class TrainingIIViewSet(MultipleFieldLookupMixin_2, viewsets.ModelViewSet):
    queryset = models.TrainingII.objects.all().order_by('id')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = TrainingIISerializer
    pagination_class = StandardResultsSetPagination
    lookup_fields = ['name', 'id']



class RookieViewSet(MultipleFieldLookupMixin_2, viewsets.ModelViewSet):
    queryset = models.Rookie.objects.all().order_by('id')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = RookieSerializer
    pagination_class = StandardResultsSetPagination
    lookup_fields = ['name', 'id']


class ChampionViewSet(MultipleFieldLookupMixin_2, viewsets.ModelViewSet):
    queryset = models.Champion.objects.all().order_by('id')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ChampionSerializer
    pagination_class = StandardResultsSetPagination
    lookup_fields = ['name', 'id']



class UltimateViewSet(MultipleFieldLookupMixin_2, viewsets.ModelViewSet):
    queryset = models.Ultimate.objects.all().order_by('id')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UltimateSerializer
    pagination_class = StandardResultsSetPagination
    lookup_fields = ['name', 'id']



class MegaViewSet(MultipleFieldLookupMixin_2, viewsets.ModelViewSet):
    queryset = models.Mega.objects.all().order_by('id')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = MegaSerializer
    pagination_class = StandardResultsSetPagination
    lookup_fields = ['name', 'id']



class ArmorViewSet(MultipleFieldLookupMixin_2, viewsets.ModelViewSet):
    queryset = models.Armor.objects.all().order_by('id')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ArmorSerializer
    pagination_class = StandardResultsSetPagination
    lookup_fields = ['name', 'id']



class HybridViewSet(MultipleFieldLookupMixin_2, viewsets.ModelViewSet):
    queryset = models.Hybrid.objects.all().order_by('id')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = HybridSerializer
    pagination_class = StandardResultsSetPagination
    lookup_fields = ['name', 'id']


class UnknownViewSet(MultipleFieldLookupMixin_2, viewsets.ModelViewSet):
    queryset = models.Unknown.objects.all().order_by('id')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UnknownSerializer
    pagination_class = StandardResultsSetPagination
    lookup_fields = ['name', 'id']


class AttributeViewSet(viewsets.ModelViewSet):
    queryset = models.Attribute.objects.all().order_by('attribute')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = AttributeSerializer
    pagination_class = StandardResultsSetPagination
    lookup_field = 'id'


class LevelViewSet(viewsets.ModelViewSet):
    queryset = models.Level.objects.all().order_by('level')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LevelSerializer
    pagination_class = StandardResultsSetPagination
    lookup_field = 'id'

class TypeDViewSet(viewsets.ModelViewSet):
    queryset = models.TypeD.objects.all().order_by('typeD')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = TypeDSerializer
    pagination_class = StandardResultsSetPagination
    lookup_field = 'id'

class SpecialMoveViewSet(viewsets.ModelViewSet):
    queryset = models.SpecialMove.objects.all().order_by('specialMove')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SpecialMoveSerializer
    pagination_class = StandardResultsSetPagination
    lookup_field = 'id'
    