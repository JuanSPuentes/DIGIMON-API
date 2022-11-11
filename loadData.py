import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

import json
from api import models

json_index = ['training_I', 'training_II', 'rookie', 'champion', 
              'ultimate', 'mega', 'armor', 'hybrid', 'xros_wars', 'unknown']


def main():
    attribute = []
    level = []
    typeD = []
    specialMove = []
    models.Attribute.objects.all().delete()
    models.Level.objects.all().delete()
    models.TypeD.objects.all().delete()
    models.SpecialMove.objects.all().delete()
    print(models.SpecialMove.objects.all())
    models.TrainingI.objects.all().delete()
    models.TrainingII.objects.all().delete()
    models.Rookie.objects.all().delete()
    models.Champion.objects.all().delete()
    models.Ultimate.objects.all().delete()
    models.Mega.objects.all().delete()
    models.Armor.objects.all().delete()
    models.Hybrid.objects.all().delete()

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


            if digi['level'] == 'In-Training \u2160' or digi['level'] == 'In-Training \u2160 (Xros Wars)':
                objects = models.TrainingI.objects.create(name = digi['name'], url = digi['url'], 
                                                urlImage = digi['url_image'], level = level_,
                                                typeD = type_d, attribute = atribute_, 
                                                profile = digi['profile'])
                for b in specialMove_:
                    objects.specialMove.add(b)
            
            if digi['level'] == 'In-Training \u2161' or digi['level'] == 'In-Training \u2161 (Xros Wars)':
                objects = models.TrainingII.objects.create(name = digi['name'], url = digi['url'], 
                                                urlImage = digi['url_image'], level = level_,
                                                typeD = type_d, attribute = atribute_, 
                                                profile = digi['profile'])
                for b in specialMove_:
                    objects.specialMove.add(b)

            if digi['level'] == 'Rookie' or digi['level'] == 'Rookie (Xros Wars)':
                objects = models.Rookie.objects.create(name = digi['name'], url = digi['url'], 
                                                urlImage = digi['url_image'], level = level_,
                                                typeD = type_d, attribute = atribute_, 
                                                profile = digi['profile'])
                for b in specialMove_:
                    objects.specialMove.add(b)


            if digi['level'] == 'Champion' or digi['level'] == 'Champion (Xros Wars)':
                objects = models.Champion.objects.create(name = digi['name'], url = digi['url'], 
                                                urlImage = digi['url_image'], level = level_,
                                                typeD = type_d, attribute = atribute_, 
                                                profile = digi['profile'])
                for b in specialMove_:
                    objects.specialMove.add(b)


            if digi['level'] == 'Ultimate' or digi['level'] == 'Ultimate (Xros Wars)':
                objects = models.Ultimate.objects.create(name = digi['name'], url = digi['url'], 
                                                urlImage = digi['url_image'], level = level_,
                                                typeD = type_d, attribute = atribute_, 
                                                profile = digi['profile'])
                for b in specialMove_:
                    objects.specialMove.add(b)

            if digi['level'] == 'Mega' or digi['level'] == 'Mega (Xros Wars)':
                objects = models.Mega.objects.create(name = digi['name'], url = digi['url'], 
                                                urlImage = digi['url_image'], level = level_,
                                                typeD = type_d, attribute = atribute_, 
                                                profile = digi['profile'])
                for b in specialMove_:
                    objects.specialMove.add(b)

            if digi['level'] == 'Armor' or digi['level'] == 'Armor (Xros Wars)':
                objects = models.Armor.objects.create(name = digi['name'], url = digi['url'], 
                                                urlImage = digi['url_image'], level = level_,
                                                typeD = type_d, attribute = atribute_, 
                                                profile = digi['profile'])
                for b in specialMove_:
                    objects.specialMove.add(b)

            if digi['level'] == 'Hybrid' or digi['level'] == 'Hybrid (Xros Wars)':
                objects = models.Hybrid.objects.create(name = digi['name'], url = digi['url'], 
                                                urlImage = digi['url_image'], level = level_,
                                                typeD = type_d, attribute = atribute_, 
                                                profile = digi['profile'])
                for b in specialMove_:
                    objects.specialMove.add(b)

            if digi['level'] == 'Unknown' or digi['level'] == 'Unknown (Xros Wars)':
                objects = models.Unknown.objects.create(name = digi['name'], url = digi['url'], 
                                                urlImage = digi['url_image'], level = level_,
                                                typeD = type_d, attribute = atribute_, 
                                                profile = digi['profile'])
                for b in specialMove_:
                    objects.specialMove.add(b)


if __name__ == '__main__':
    main()