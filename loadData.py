import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

import json
from api import models

json_index = {'training_i':models.TrainingI, 'training_ii': models.TrainingII, 
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

    return object_

def main():
    attribute = []
    level = []
    typeD = []
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


    current_directory = os.getcwd()
    print(current_directory)
    contents = os.listdir('/opt/render/project/src/json/')
    print(contents)

    for i in json_index:
        with open('/opt/render/project/src/json/{}'.format(i+".json"),'r',) as file:
            data = json.load(file)

        #Guardando la data en los modelos
        for digi in data:
            #Attribute data
            if digi['attribute'] == '':
               digi['attribute'] = 'NA'
            #Verifica si el attribute ya esta guardado en el modelo y
            # guarda el objeto en una lista
            if digi['attribute'] not in attribute:
                attribute.append(digi['attribute'])
                atribute_ = models.Attribute.objects.create(attribute = digi['attribute'])
            else:
                atribute_ = models.Attribute.objects.get(attribute = digi['attribute'])
                
            
            #Level data
            if digi['level'] == '':
               digi['level'] = 'NA'
            # Verifica si el level ya esta guardados en la db
            # Y extrae el objeto y lo guarda en una lista
            if digi['level'] not in level:
                level.append(digi['level'])
                level_ = models.Level.objects.create(level = digi['level'])
            else:
                level_ = models.Level.objects.get(level = digi['level'])
            
            #Type data
            if digi['type'] == '':
               digi['type'] = 'NA'
            # Verifica si el Type ya esta guardado en la db
            # Y extrae el objeto y lo guarda en una lista
            if digi['type'] not in typeD:
                typeD.append(digi['type'])
                type_d = models.TypeD.objects.create(typeD = digi['type'])
            else:
                type_d = models.TypeD.objects.get(typeD = digi['type'])
                

            # special_Move data
            # divide la lista de los movimientos
            if digi['special_Move'] == '' or digi['special_Move'] == '\u30fb':
               digi['special_Move'] = '\u30fb'
            # Elimina los campos vacios
            specMove = digi['special_Move']
            a = specMove.split('\u30fb')
            a.remove('')
            if '' in a:
               a[0] = 'NA'
            # Busca '\n' y si lo encuentra lo elimina
            for y,z in enumerate(a):
                if z.find('\n') != -1:
                    a[y] = z[:-2]

            specialMove_ = []
            """Consulta en la tabla SpecialMove el movimiento especial
            Verifica si el query esta vacio para guardarlo en la db y en una lista
            Si no esta en la db crea el objeto y lo guarda en una lista"""
            for spc in a:
                specialMove = models.SpecialMove.objects.filter(specialMove = spc)  
                if specialMove.exists():specialMove_.append(models.SpecialMove.objects.get(specialMove = spc))
                else:specialMove_.append(models.SpecialMove.objects.create(specialMove = spc))

            # Elimina del profile 'Profile\n' fragmento inecesario en el texto
            digi.update({'profile': digi['profile'].replace('Profile\n', '')})

            """Funcion que guarda la data y se recupera el objeto guardado"""
            digi_object = SaveDataDigi(model=json_index[i], digi=digi, type_d=type_d, level_=level_, atribute_=atribute_, specialMove_=specialMove_)
            
            """ Creacion del link para ver el detalle del Digimon
                i : nombre del nivel del digimon
                digi_object: objeto guardado en la db
                digi_object.id: id del objeto guardado en la db    
            """
            href = 'http://digimon-api-drf.onrender.com/routers/api/{}/{}/'.format(i, digi_object.id)
            models.Digimons.objects.create(name = digi['name'], href = href, level = level_.level)
            


if __name__ == '__main__':
    main()