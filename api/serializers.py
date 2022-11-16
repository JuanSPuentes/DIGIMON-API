from rest_framework import serializers
from api import models

class DigimonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Digimons
        fields = ('id', 'name', 'level', 'href')


class TrainingISerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TrainingI
        fields = ('id', 'name', 'url', 'urlImage', 'level', 'typeD', 'attribute', 
                  'specialMove', 'profile', 'xAntibody')

class TrainingIISerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TrainingII
        fields = ('id', 'name', 'url', 'urlImage', 'level', 'typeD', 'attribute', 
                  'specialMove', 'profile', 'xAntibody')

class RookieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rookie
        fields = ('id', 'name', 'url', 'urlImage', 'level', 'typeD', 'attribute', 
                  'specialMove', 'profile', 'xAntibody')

class ChampionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Champion
        fields = ('id', 'name', 'url', 'urlImage', 'level', 'typeD', 'attribute', 
                  'specialMove', 'profile', 'xAntibody')

class UltimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ultimate
        fields = ('id', 'name', 'url', 'urlImage', 'level', 'typeD', 'attribute', 
                  'specialMove', 'profile', 'xAntibody')

class MegaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mega
        fields = ('id', 'name', 'url', 'urlImage', 'level', 'typeD', 'attribute', 
                  'specialMove', 'profile', 'xAntibody')

class ArmorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Armor
        fields = ('id', 'name', 'url', 'urlImage', 'level', 'typeD', 'attribute', 
                  'specialMove', 'profile', 'xAntibody')

class HybridSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Hybrid
        fields = ('id', 'name', 'url', 'urlImage', 'level', 'typeD', 'attribute', 
                  'specialMove', 'profile', 'xAntibody')

class UnknownSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Unknown
        fields = ('id', 'name', 'url', 'urlImage', 'level', 'typeD', 'attribute', 
                  'specialMove', 'profile', 'xAntibody')

class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Attribute
        fields = ('id', 'attribute')

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Level
        fields = ('id', 'level')     

class TypeDSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TypeD
        fields = ('id', 'typeD')    

class SpecialMoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SpecialMove
        fields = ('id', 'specialMove')    