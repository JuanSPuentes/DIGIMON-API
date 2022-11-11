import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

import json
from api import models

json_index = {'training_I':models.TrainingI, 'training_II': models.TrainingII, 
              'rookie':models.Rookie, 'champion':models.Champion, 
              'ultimate':models.Ultimate, 'mega':models.Mega, 'armor':models.Armor, 
              'hybrid': models.Hybrid, 'xros_wars':models.XrosWars, 'unknown':models.Unknown}


def SaveDataDigi(model=None, digi=None, type_d=None, level_=None, atribute_=None, specialMove_=None):
    """La funcion guarda los datos en la base de datos

    Args:
        model (object, optional): Modelo que se usa para guardar los datos.
        digi (dict, optional): diccionario que contenie la data.
        type_d (list, optional): lista que contiene el objeto.
        level_ (list, optional): lista que contiene el objeto.
        atribute_ (list, optional): lista que contiene el objeto.
        specialMove_ (list, optional): lista que contiene los objetos.
    """

    if digi['name'].find('(X Antibody)') != -1:
        x_Antibody = True
    else:
        x_Antibody = False

    object_ = model.objects.create(name = digi['name'], url = digi['url'], 
                                   urlImage = digi['url_image'], level = level_,
                                   typeD = type_d, attribute = atribute_, 
                                   profile = digi['profile'], xAntibody= x_Antibody)
    for b in specialMove_:
        object_.specialMove.add(b)


def main():
    attribute = []
    level = []
    typeD = []
    specialMove = []
    models.Attribute.objects.all().delete()
    models.Level.objects.all().delete()
    models.TypeD.objects.all().delete()
    models.SpecialMove.objects.all().delete()
    models.TrainingI.objects.all().delete()
    models.TrainingII.objects.all().delete()
    models.Rookie.objects.all().delete()
    models.Champion.objects.all().delete()
    models.Ultimate.objects.all().delete()
    models.Mega.objects.all().delete()
    models.Armor.objects.all().delete()
    models.Hybrid.objects.all().delete()
    models.Digimons.objects.all().delete()

    for i in json_index:
        with open('json/{}'.format(i+".json")) as file:
            data = json.load(file)

        #Save data in models
        for digi in data:
            #Atribute data
            if digi['attribute'] == '':
               digi['attribute'] = 'NA'

            if digi['attribute'] not in attribute:
                attribute.append(digi['attribute'])
                atribute_ = models.Attribute.objects.create(attribute = digi['attribute'])
            else:
                atribute_ = models.Attribute.objects.get(attribute = digi['attribute'])
                
            
            #Level data
            if digi['level'] == '':
               digi['level'] = 'NA'

            if digi['level'] not in level:
                level.append(digi['level'])
                level_ = models.Level.objects.create(level = digi['level'])
            else:
            
                level_ = models.Level.objects.get(level = digi['level'])
            
                

            #Type data
            if digi['type'] == '':
               digi['type'] = 'NA'

            if digi['type'] not in typeD:
                typeD.append(digi['type'])
                type_d = models.TypeD.objects.create(typeD = digi['type'])
            else:
                
                type_d = models.TypeD.objects.get(typeD = digi['type'])
                

            #special_Move data
            if digi['special_Move'] == '' or digi['special_Move'] == '\u30fb':
               digi['special_Move'] = '\u30fbNA'

            specMove = digi['special_Move']
            a = specMove.split('\u30fb')
            a.remove('')
            specialMove = models.SpecialMove.objects.all()
            specialMove_ = []
            for spc in a:
                if spc not in specialMove:
                    specialMove_.append(models.SpecialMove.objects.create(specialMove = spc))
                else:
                    print('entro al get')
                    specialMove_.append(models.SpecialMove.objects.get(specialMove = spc))

            """Funcion que guarda la data"""
            SaveDataDigi(model=json_index[i], digi=digi, type_d=type_d, level_=level_, atribute_=atribute_, specialMove_=specialMove_)

            models.Digimons.objects.create(name = digi['name'], level = level_)


if __name__ == '__main__':
    main()