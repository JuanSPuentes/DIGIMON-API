from api import models
from rest_framework import viewsets, permissions
from .serializers import (DigimonSerializer, TrainingISerializer, TrainingIISerializer,RookieSerializer,
                          ChampionSerializer, UltimateSerializer, MegaSerializer, ArmorSerializer,
                          HybridSerializer, UnknownSerializer, AttributeSerializer, LevelSerializer,
                          TypeDSerializer, SpecialMoveSerializer)
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.shortcuts import get_list_or_404, get_object_or_404


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100



class DigimonViewSet(viewsets.ModelViewSet):
    queryset = models.Digimons.objects.all().order_by('name')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = DigimonSerializer
    pagination_class = StandardResultsSetPagination
    lookup_field = 'name'

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        try:
            obj = get_object_or_404(queryset, id = filter_kwargs['name'])     
        except:
            obj = get_list_or_404(queryset, name__icontains = filter_kwargs['name'])

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj


    
    def retrieve(self, request, *args, **kwargs):
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



class TrainingIViewSet(viewsets.ModelViewSet):
    queryset = models.TrainingI.objects.all().order_by('id')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = TrainingISerializer
    pagination_class = StandardResultsSetPagination
    lookup_field = 'name'

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        try:
            obj = get_object_or_404(queryset, id = filter_kwargs['name'])     
        except:

            obj = get_list_or_404(queryset, name__icontains = filter_kwargs['name'])

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj

    def json_create(self, values = None):
        json_ = {}
        json_['id'] = values.id
        json_['name'] = values.name
        json_['url'] = values.url
        json_['urlImage'] = values.urlImage
        json_['level'] =  [{'id':values.level.id,'level':values.level.level}]
        json_['typeD'] = [{'id':values.typeD.id,'type':values.typeD.typeD}]
        json_['attribute'] = [{'id':values.attribute.id,'attribute':values.attribute.attribute}]
        json_['specialMove'] = [{'id':j.id, 'special move':j.specialMove}  for j in values.specialMove.all()]
        json_['profile'] = values.profile
        json_['xAntibody'] = values.xAntibody
        return json_

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        data = []
        if type(instance) == list:
            for i in instance:
                json_ = self.json_create(i)
                data.append(json_)
        else:
            json_ = self.json_create(instance)
            data.append(json_)
        return Response(data)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        data = []
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            for i in page:
                json_ = self.json_create(i)
                data.append(json_)
            return self.get_paginated_response(data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class TrainingIIViewSet(viewsets.ModelViewSet):
    queryset = models.TrainingII.objects.all().order_by('id')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = TrainingIISerializer
    pagination_class = StandardResultsSetPagination
    lookup_field = 'name'

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        try:
            obj = get_object_or_404(queryset, id = filter_kwargs['name'])     
        except:

            obj = get_list_or_404(queryset, name__icontains = filter_kwargs['name'])

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj

    def json_create(self, values = None):
        json_ = {}
        json_['id'] = values.id
        json_['name'] = values.name
        json_['url'] = values.url
        json_['urlImage'] = values.urlImage
        json_['level'] =  [{'id':values.level.id,'level':values.level.level}]
        json_['typeD'] = [{'id':values.typeD.id,'type':values.typeD.typeD}]
        json_['attribute'] = [{'id':values.attribute.id,'attribute':values.attribute.attribute}]
        json_['specialMove'] = [{'id':j.id, 'special move':j.specialMove}  for j in values.specialMove.all()]
        json_['profile'] = values.profile
        json_['xAntibody'] = values.xAntibody
        return json_

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        data = []
        if type(instance) == list:
            for i in instance:
                json_ = self.json_create(i)
                data.append(json_)
        else:
            json_ = self.json_create(instance)
            data.append(json_)
        return Response(data)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        data = []
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            for i in page:
                json_ = self.json_create(i)
                data.append(json_)
            return self.get_paginated_response(data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class RookieViewSet(viewsets.ModelViewSet):
    queryset = models.Rookie.objects.all().order_by('id')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = RookieSerializer
    pagination_class = StandardResultsSetPagination
    lookup_field = 'name'

  

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        try:
            obj = get_object_or_404(queryset, id = filter_kwargs['name'])     
        except:

            obj = get_list_or_404(queryset, name__icontains = filter_kwargs['name'])

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj

    def json_create(self, values = None):
        json_ = {}
        json_['id'] = values.id
        json_['name'] = values.name
        json_['url'] = values.url
        json_['urlImage'] = values.urlImage
        json_['level'] =  [{'id':values.level.id,'level':values.level.level}]
        json_['typeD'] = [{'id':values.typeD.id,'type':values.typeD.typeD}]
        json_['attribute'] = [{'id':values.attribute.id,'attribute':values.attribute.attribute}]
        json_['specialMove'] = [{'id':j.id, 'special move':j.specialMove}  for j in values.specialMove.all()]
        json_['profile'] = values.profile
        json_['xAntibody'] = values.xAntibody
        return json_

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        data = []
        if type(instance) == list:
            for i in instance:
                json_ = self.json_create(i)
                data.append(json_)
        else:
            json_ = self.json_create(instance)
            data.append(json_)
        return Response(data)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        data = []
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            for i in page:
                json_ = self.json_create(i)
                data.append(json_)
            return self.get_paginated_response(data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class ChampionViewSet(viewsets.ModelViewSet):
    queryset = models.Champion.objects.all().order_by('id')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ChampionSerializer
    pagination_class = StandardResultsSetPagination
    lookup_field = 'name'

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        try:
            obj = get_object_or_404(queryset, id = filter_kwargs['name'])     
        except:

            obj = get_list_or_404(queryset, name__icontains = filter_kwargs['name'])

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj

    def json_create(self, values = None):
        json_ = {}
        json_['id'] = values.id
        json_['name'] = values.name
        json_['url'] = values.url
        json_['urlImage'] = values.urlImage
        json_['level'] =  [{'id':values.level.id,'level':values.level.level}]
        json_['typeD'] = [{'id':values.typeD.id,'type':values.typeD.typeD}]
        json_['attribute'] = [{'id':values.attribute.id,'attribute':values.attribute.attribute}]
        json_['specialMove'] = [{'id':j.id, 'special move':j.specialMove}  for j in values.specialMove.all()]
        json_['profile'] = values.profile
        json_['xAntibody'] = values.xAntibody
        return json_

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        data = []
        if type(instance) == list:
            for i in instance:
                json_ = self.json_create(i)
                data.append(json_)
        else:
            json_ = self.json_create(instance)
            data.append(json_)
        return Response(data)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        data = []
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            for i in page:
                json_ = self.json_create(i)
                data.append(json_)
            return self.get_paginated_response(data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class UltimateViewSet(viewsets.ModelViewSet):
    queryset = models.Ultimate.objects.all().order_by('id')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UltimateSerializer
    pagination_class = StandardResultsSetPagination
    lookup_field = 'name'

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        try:
            obj = get_object_or_404(queryset, id = filter_kwargs['name'])     
        except:

            obj = get_list_or_404(queryset, name__icontains = filter_kwargs['name'])

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj

    def json_create(self, values = None):
        json_ = {}
        json_['id'] = values.id
        json_['name'] = values.name
        json_['url'] = values.url
        json_['urlImage'] = values.urlImage
        json_['level'] =  [{'id':values.level.id,'level':values.level.level}]
        json_['typeD'] = [{'id':values.typeD.id,'type':values.typeD.typeD}]
        json_['attribute'] = [{'id':values.attribute.id,'attribute':values.attribute.attribute}]
        json_['specialMove'] = [{'id':j.id, 'special move':j.specialMove}  for j in values.specialMove.all()]
        json_['profile'] = values.profile
        json_['xAntibody'] = values.xAntibody
        return json_

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        data = []
        if type(instance) == list:
            for i in instance:
                json_ = self.json_create(i)
                data.append(json_)
        else:
            json_ = self.json_create(instance)
            data.append(json_)
        return Response(data)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        data = []
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            for i in page:
                json_ = self.json_create(i)
                data.append(json_)
            return self.get_paginated_response(data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class MegaViewSet(viewsets.ModelViewSet):
    queryset = models.Mega.objects.all().order_by('id')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = MegaSerializer
    pagination_class = StandardResultsSetPagination
    lookup_field = 'name'

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        try:
            obj = get_object_or_404(queryset, id = filter_kwargs['name'])     
        except:
            obj = get_list_or_404(queryset, name__icontains = filter_kwargs['name'])
        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj

    def json_create(self, values = None):
        json_ = {}
        json_['id'] = values.id
        json_['name'] = values.name
        json_['url'] = values.url
        json_['urlImage'] = values.urlImage
        json_['level'] =  [{'id':values.level.id,'level':values.level.level}]
        json_['typeD'] = [{'id':values.typeD.id,'type':values.typeD.typeD}]
        json_['attribute'] = [{'id':values.attribute.id,'attribute':values.attribute.attribute}]
        json_['specialMove'] = [{'id':j.id, 'special move':j.specialMove}  for j in values.specialMove.all()]
        json_['profile'] = values.profile
        json_['xAntibody'] = values.xAntibody
        return json_

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        data = []
        if type(instance) == list:
            for i in instance:
                json_ = self.json_create(i)
                data.append(json_)
        else:
            json_ = self.json_create(instance)
            data.append(json_)
        return Response(data)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        data = []
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            for i in page:
                json_ = self.json_create(i)
                data.append(json_)
            return self.get_paginated_response(data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class ArmorViewSet(viewsets.ModelViewSet):
    queryset = models.Armor.objects.all().order_by('id')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ArmorSerializer
    pagination_class = StandardResultsSetPagination
    lookup_field = 'name'

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        try:
            obj = get_object_or_404(queryset, id = filter_kwargs['name'])     
        except:

            obj = get_list_or_404(queryset, name__icontains = filter_kwargs['name'])

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj

    def json_create(self, values = None):
        json_ = {}
        json_['id'] = values.id
        json_['name'] = values.name
        json_['url'] = values.url
        json_['urlImage'] = values.urlImage
        json_['level'] =  [{'id':values.level.id,'level':values.level.level}]
        json_['typeD'] = [{'id':values.typeD.id,'type':values.typeD.typeD}]
        json_['attribute'] = [{'id':values.attribute.id,'attribute':values.attribute.attribute}]
        json_['specialMove'] = [{'id':j.id, 'special move':j.specialMove}  for j in values.specialMove.all()]
        json_['profile'] = values.profile
        json_['xAntibody'] = values.xAntibody
        return json_

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        data = []
        if type(instance) == list:
            for i in instance:
                json_ = self.json_create(i)
                data.append(json_)
        else:
            json_ = self.json_create(instance)
            data.append(json_)
        return Response(data)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        data = []
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            for i in page:
                json_ = self.json_create(i)
                data.append(json_)
            return self.get_paginated_response(data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class HybridViewSet(viewsets.ModelViewSet):
    queryset = models.Hybrid.objects.all().order_by('id')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = HybridSerializer
    pagination_class = StandardResultsSetPagination
    lookup_field = 'name'

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        try:
            obj = get_object_or_404(queryset, id = filter_kwargs['name'])     
        except:

            obj = get_list_or_404(queryset, name__icontains = filter_kwargs['name'])

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj

    def json_create(self, values = None):
        json_ = {}
        json_['id'] = values.id
        json_['name'] = values.name
        json_['url'] = values.url
        json_['urlImage'] = values.urlImage
        json_['level'] =  [{'id':values.level.id,'level':values.level.level}]
        json_['typeD'] = [{'id':values.typeD.id,'type':values.typeD.typeD}]
        json_['attribute'] = [{'id':values.attribute.id,'attribute':values.attribute.attribute}]
        json_['specialMove'] = [{'id':j.id, 'special move':j.specialMove}  for j in values.specialMove.all()]
        json_['profile'] = values.profile
        json_['xAntibody'] = values.xAntibody
        return json_

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        data = []
        if type(instance) == list:
            for i in instance:
                json_ = self.json_create(i)
                data.append(json_)
        else:
            json_ = self.json_create(instance)
            data.append(json_)
        return Response(data)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        data = []
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            for i in page:
                json_ = self.json_create(i)
                data.append(json_)
            return self.get_paginated_response(data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class UnknownViewSet(viewsets.ModelViewSet):
    queryset = models.Unknown.objects.all().order_by('id')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UnknownSerializer
    pagination_class = StandardResultsSetPagination
    lookup_field = 'name'

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        try:
            obj = get_object_or_404(queryset, id = filter_kwargs['name'])     
        except:
            obj = get_list_or_404(queryset, name__icontains = filter_kwargs['name'])

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj

    def json_create(self, values = None):
        json_ = {}
        json_['id'] = values.id
        json_['name'] = values.name
        json_['url'] = values.url
        json_['urlImage'] = values.urlImage
        json_['level'] =  [{'id':values.level.id,'level':values.level.level}]
        json_['typeD'] = [{'id':values.typeD.id,'type':values.typeD.typeD}]
        json_['attribute'] = [{'id':values.attribute.id,'attribute':values.attribute.attribute}]
        json_['specialMove'] = [{'id':j.id, 'special move':j.specialMove}  for j in values.specialMove.all()]
        json_['profile'] = values.profile
        json_['xAntibody'] = values.xAntibody
        return json_

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        data = []
        if type(instance) == list:
            for i in instance:
                json_ = self.json_create(i)
                data.append(json_)
        else:
            json_ = self.json_create(instance)
            data.append(json_)
        return Response(data)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        data = []
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            for i in page:
                json_ = self.json_create(i)
                data.append(json_)
            return self.get_paginated_response(data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


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
    