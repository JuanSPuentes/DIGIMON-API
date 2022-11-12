from rest_framework import serializers
from api import models

class DigimonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Digimons
        fields = ('id', 'name', 'level', 'href')
