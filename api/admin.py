from django.contrib import admin
from api import models
# Register your models here.

@admin.register(models.Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ['attribute',]
    
@admin.register(models.Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ['level',]

@admin.register(models.SpecialMove)
class SpecialMoveAdmin(admin.ModelAdmin):
    list_display = ['specialMove',]


@admin.register(models.TypeD)
class TypeDAdmin(admin.ModelAdmin):
    list_display = ['typeD',]

@admin.register(models.TrainingI)
class TrainingIAdmin(admin.ModelAdmin):
    list_display = ['name', 'typeD', 'attribute', 'xAntibody']

@admin.register(models.TrainingII)
class TrainingIIAdmin(admin.ModelAdmin):
    list_display = ['name', 'typeD', 'attribute', 'xAntibody']

@admin.register(models.Rookie)
class RookieAdmin(admin.ModelAdmin):
    list_display = ['name', 'typeD', 'attribute', 'xAntibody']


@admin.register(models.Champion)
class ChampionAdmin(admin.ModelAdmin):
    list_display = ['name', 'typeD', 'attribute', 'xAntibody']

@admin.register(models.Ultimate)
class UltimateAdmin(admin.ModelAdmin):
    list_display = ['name', 'typeD', 'attribute', 'xAntibody']

@admin.register(models.Mega)
class MegaAdmin(admin.ModelAdmin):
    list_display = ['name', 'typeD', 'attribute', 'xAntibody']


@admin.register(models.Armor)
class ArmorAdmin(admin.ModelAdmin):
    list_display = ['name', 'typeD', 'attribute', 'xAntibody']


@admin.register(models.Hybrid)
class HybridAdmin(admin.ModelAdmin):
    list_display = ['name', 'typeD', 'attribute', 'xAntibody']

@admin.register(models.Unknown)
class UnknownAdmin(admin.ModelAdmin):
    list_display = ['name', 'typeD', 'attribute', 'xAntibody']

@admin.register(models.XrosWars)
class XrosWarsAdmin(admin.ModelAdmin):
    list_display = ['name', 'typeD', 'attribute', 'xAntibody']

@admin.register(models.Digimons)
class DigimonsAdmin(admin.ModelAdmin):
    list_display = ['name', 'level']




