from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.response import Response

class MultipleFieldLookupMixin:
    def get_object(self):
        queryset = self.get_queryset()            
        queryset = self.filter_queryset(queryset)  
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs.get('pk'): 
                filter[field] = self.kwargs['pk']   
        try:
            obj = get_object_or_404(queryset, id = filter['id'])     
        except:
            obj = get_list_or_404(queryset, name__icontains = filter['name'])

        self.check_object_permissions(self.request, obj)
        return obj


class MultipleFieldLookupMixin_2:
    def get_object(self):
        queryset = self.get_queryset()            
        queryset = self.filter_queryset(queryset)  
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs.get('pk'): 
                filter[field] = self.kwargs['pk']   
        try:
            obj = get_object_or_404(queryset, id = filter['id'])     
        except:
            obj = get_list_or_404(queryset, name__icontains = filter['name'])

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
        """
        or you can use /{level}/{name}
        Example ---> /mega/Alphamon   this can list multiple objects
        """
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

