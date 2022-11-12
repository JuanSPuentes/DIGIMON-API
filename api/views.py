from api import models
from rest_framework import viewsets, permissions
from .serializers import DigimonSerializer
from rest_framework.pagination import PageNumberPagination
from django.http import response

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class DigimonViewSet(viewsets.ModelViewSet):
    queryset = models.Digimons.objects.all().order_by('id')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = DigimonSerializer
    pagination_class = StandardResultsSetPagination
    lookup_field = 'name'

