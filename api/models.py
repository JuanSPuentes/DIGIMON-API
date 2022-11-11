from django.db import models

# Create your models here.

class Attribute(models.Model):
    attribute = models.CharField(max_length=50)

    def __str__(self):
        return self.attribute   

class Level(models.Model):
    level = models.CharField(max_length=50)

    def __str__(self):
        return self.level   

class TypeD(models.Model):
    typeD = models.CharField(max_length=50)

    def __str__(self):
        return self.typeD   

class SpecialMove(models.Model):
    specialMove = models.CharField(max_length=50)

    def __str__(self):
        return self.specialMove   

class TrainingI(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    url = models.URLField(max_length=200, null=False, blank=False)
    urlImage = models.URLField(max_length=200, null=False, blank=False)
    level = models.ForeignKey(Level, verbose_name=("Level"), on_delete=models.CASCADE, null=True, blank=True)
    typeD = models.ForeignKey(TypeD, verbose_name=("Type"), on_delete=models.CASCADE, null=True, blank=True)
    attribute = models.ForeignKey(Attribute, verbose_name=("Attribute"), on_delete=models.CASCADE, null=True, blank=True)
    specialMove = models.ManyToManyField(SpecialMove, verbose_name=("SpecialMove"),  blank=True)
    profile = models.TextField(max_length=2000, verbose_name=("Description"), null=False, blank=False)
    xAntibody = models.BooleanField(default=False, null=False, blank=False)


class TrainingII(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    url = models.URLField(max_length=200, null=False, blank=False)
    urlImage = models.URLField(max_length=200, null=False, blank=False)
    level = models.ForeignKey(Level, verbose_name=("Level"), on_delete=models.CASCADE, null=True, blank=True)
    typeD = models.ForeignKey(TypeD, verbose_name=("Type"), on_delete=models.CASCADE, null=True, blank=True)
    attribute = models.ForeignKey(Attribute, verbose_name=("Attribute"), on_delete=models.CASCADE, null=True, blank=True)
    specialMove = models.ManyToManyField(SpecialMove, verbose_name=("SpecialMove"),  blank=True)
    profile = models.TextField(max_length=2000, verbose_name=("Description"), null=False, blank=False)
    xAntibody = models.BooleanField(default=False, null=False, blank=False)


class Rookie(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    url = models.URLField(max_length=200, null=False, blank=False)
    urlImage = models.URLField(max_length=200, null=False, blank=False)
    level = models.ForeignKey(Level, verbose_name=("Level"), on_delete=models.CASCADE, null=True, blank=True)
    typeD = models.ForeignKey(TypeD, verbose_name=("Type"), on_delete=models.CASCADE, null=True, blank=True)
    attribute = models.ForeignKey(Attribute, verbose_name=("Attribute"), on_delete=models.CASCADE, null=True, blank=True)
    specialMove = models.ManyToManyField(SpecialMove, verbose_name=("SpecialMove"),  blank=True)
    profile = models.TextField(max_length=2000, verbose_name=("Description"), null=False, blank=False)
    xAntibody = models.BooleanField(default=False, null=False, blank=False)


class Champion(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    url = models.URLField(max_length=200, null=False, blank=False)
    urlImage = models.URLField(max_length=200, null=False, blank=False)
    level = models.ForeignKey(Level, verbose_name=("Level"), on_delete=models.CASCADE, null=True, blank=True)
    typeD = models.ForeignKey(TypeD, verbose_name=("Type"), on_delete=models.CASCADE, null=True, blank=True)
    attribute = models.ForeignKey(Attribute, verbose_name=("Attribute"), on_delete=models.CASCADE, null=True, blank=True)
    specialMove = models.ManyToManyField(SpecialMove, verbose_name=("SpecialMove"),  blank=True)
    profile = models.TextField(max_length=2000, verbose_name=("Description"), null=False, blank=False)
    xAntibody = models.BooleanField(default=False, null=False, blank=False)


class Ultimate(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    url = models.URLField(max_length=200, null=False, blank=False)
    urlImage = models.URLField(max_length=200, null=False, blank=False)
    level = models.ForeignKey(Level, verbose_name=("Level"), on_delete=models.CASCADE, null=True, blank=True)
    typeD = models.ForeignKey(TypeD, verbose_name=("Type"), on_delete=models.CASCADE, null=True, blank=True)
    attribute = models.ForeignKey(Attribute, verbose_name=("Attribute"), on_delete=models.CASCADE, null=True, blank=True)
    specialMove = models.ManyToManyField(SpecialMove, verbose_name=("SpecialMove"),  blank=True)
    profile = models.TextField(max_length=2000, verbose_name=("Description"), null=False, blank=False)
    xAntibody = models.BooleanField(default=False, null=False, blank=False)


class Mega(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    url = models.URLField(max_length=200, null=False, blank=False)
    urlImage = models.URLField(max_length=200, null=False, blank=False)
    level = models.ForeignKey(Level, verbose_name=("Level"), on_delete=models.CASCADE, null=True, blank=True)
    typeD = models.ForeignKey(TypeD, verbose_name=("Type"), on_delete=models.CASCADE, null=True, blank=True)
    attribute = models.ForeignKey(Attribute, verbose_name=("Attribute"), on_delete=models.CASCADE, null=True, blank=True)
    specialMove = models.ManyToManyField(SpecialMove, verbose_name=("SpecialMove"),  blank=True)
    profile = models.TextField(max_length=2000, verbose_name=("Description"), null=False, blank=False)
    xAntibody = models.BooleanField(default=False, null=False, blank=False)


class Armor(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    url = models.URLField(max_length=200, null=False, blank=False)
    urlImage = models.URLField(max_length=200, null=False, blank=False)
    level = models.ForeignKey(Level, verbose_name=("Level"), on_delete=models.CASCADE, null=True, blank=True)
    typeD = models.ForeignKey(TypeD, verbose_name=("Type"), on_delete=models.CASCADE, null=True, blank=True)
    attribute = models.ForeignKey(Attribute, verbose_name=("Attribute"), on_delete=models.CASCADE, null=True, blank=True)
    specialMove = models.ManyToManyField(SpecialMove, verbose_name=("SpecialMove"),  blank=True)
    profile = models.TextField(max_length=2000, verbose_name=("Description"), null=False, blank=False)
    xAntibody = models.BooleanField(default=False, null=False, blank=False)


class Hybrid(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    url = models.URLField(max_length=200, null=False, blank=False)
    urlImage = models.URLField(max_length=200, null=False, blank=False)
    level = models.ForeignKey(Level, verbose_name=("Level"), on_delete=models.CASCADE, null=True, blank=True)
    typeD = models.ForeignKey(TypeD, verbose_name=("Type"), on_delete=models.CASCADE, null=True, blank=True)
    attribute = models.ForeignKey(Attribute, verbose_name=("Attribute"), on_delete=models.CASCADE, null=True, blank=True)
    specialMove = models.ManyToManyField(SpecialMove, verbose_name=("SpecialMove"),  blank=True)
    profile = models.TextField(max_length=2000, verbose_name=("Description"), null=False, blank=False)
    xAntibody = models.BooleanField(default=False, null=False, blank=False)


class Unknown(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    url = models.URLField(max_length=200, null=False, blank=False)
    urlImage = models.URLField(max_length=200, null=False, blank=False)
    level = models.ForeignKey(Level, verbose_name=("Level"), on_delete=models.CASCADE, null=True, blank=True)
    typeD = models.ForeignKey(TypeD, verbose_name=("Type"), on_delete=models.CASCADE, null=True, blank=True)
    attribute = models.ForeignKey(Attribute, verbose_name=("Attribute"), on_delete=models.CASCADE, null=True, blank=True)
    specialMove = models.ManyToManyField(SpecialMove, verbose_name=("SpecialMove"),  blank=True)
    profile = models.TextField(max_length=2000, verbose_name=("Description"), null=False, blank=False)
    xAntibody = models.BooleanField(default=False, null=False, blank=False)


class XrosWars(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    url = models.URLField(max_length=200, null=False, blank=False)
    urlImage = models.URLField(max_length=200, null=False, blank=False)
    level = models.ForeignKey(Level, verbose_name=("Level"), on_delete=models.CASCADE, null=True, blank=True)
    typeD = models.ForeignKey(TypeD, verbose_name=("Type"), on_delete=models.CASCADE, null=True, blank=True)
    attribute = models.ForeignKey(Attribute, verbose_name=("Attribute"), on_delete=models.CASCADE, null=True, blank=True)
    specialMove = models.ManyToManyField(SpecialMove, verbose_name=("SpecialMove"),  blank=True)
    profile = models.TextField(max_length=2000, verbose_name=("Description"), null=False, blank=False)
    xAntibody = models.BooleanField(default=False, null=False, blank=False)


class Digimons(models.Model):
    name = models.CharField(max_length=50)
    href = models.URLField(max_length=200)
    level= models.CharField(max_length=50)

