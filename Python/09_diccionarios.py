#LECCIÓN 10 : DICCIONARIOS EN PYTHON

print("\n<----------- CREACCIÓN DE UN DICCIONARIO ----------->\n")


"""
No se si habréis visto los diccionarios en Java o en otros lenguajes de programación, pero, ¿Qué son los diccionarios?
Un diccionario es una colección de tipos de datos emparejados (clave: valor) no ordenados y modificables (mutables).

    -> Para crear un diccionario utilizamos llaves, {} o la función incorporada dict() 
        empty_dict = {} Vacío
        dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'} Con valores desde el inicio

"""


person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

print(person)








print("\n<----------- LONGITUD DE UN DICCIONARIO ----------->\n")

"""
El diccionario anterior muestra que un valor podría ser cualquier tipo de datos: cadena, booleano, lista, tupla, conjunto o un diccionario.
También podemos comprobar la longitud del mismo con la funcion len()
"""

print(len(person)) # 7








print("\n<----------- ACCEDER A LOS ELEMENTOS DE UN DICCIONARIO ----------->\n")

"""
En los diccionarios tenemos una manera más sencilla de acceder a un elemento, podemos acceder a ellos consultando su nombre de clave.
La sintaxis es la siguiente :

    ->  dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
        print(dct['key1']) # value1
        print(dct['key4']) # value4
"""

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person['first_name']) # Asabeneh
print(person['country'])    # Finland
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Space street
#print(person['city'])       # Error



print("\n<-- none -->\n")

"""
Efectivamente, si la clave no se encuentra en el diccionario e intentamos utilizarla, fallará.
Acceder a un elemento por el nombre de la clave genera un error si la clave no existe.
Para evitar este error, primero debemos verificar si existe una clave o podemos usar el método get() .
El método get() devuelve None, que es un tipo de datos de objeto NoneType, si la clave no existe.
"""

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person.get('first_name')) # Asabeneh
print(person.get('country'))    # Finland
print(person.get('skills')) #['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None









print("\n<----------- AGREGAR ELEMENTOS A UN DICCIONARIO ----------->\n")

"""
Podemos agregar nuevos pares de clave y valor a un diccionario con la siguiente sintaxis :

    ->  dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
        dct['key5'] = 'value5'
"""

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
        }
}
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)







print("\n<----------- MODIFICAR ELEMENTOS DE UN DICCIONARIO ----------->\n")

"""
Así como podemos agregar elementos, también podemos modificar los elementos existentes en un diccionario.
La manera de hacerlo es acceder a la clave del diccionario y modificar su valor.
"""

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
person['first_name'] = 'Eyob'
person['age'] = 252




print("\n<----------- COMPROBACIÓN DE LOS ELEMENTOS DE UN DICCIONARIO ----------->\n")

"""
Igual que en el resto de tipos, usamos el operador in para verificar si una clave existe en un diccionario

    ->  dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
        print('key2' in dct) # True
        print('key5' in dct) # False
"""


person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

print('skills' in person)
print('ejemplo' in person)








print("\n<----------- ELIMINAR PARES CLAVE-VALOR ----------->\n")

"""
Para los diccionarios tenemos tres diferentes maneras de eliminar elementos de un diciconario: 

    -> pop(key) : elimina el elemento con el nombre de clave especificado:
    -> popitem() : elimina el último elemento
    -> del : elimina un elemento con el nombre de clave especificado

        dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
        dct.pop('key1') # removes key1 item
        dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
        dct.popitem() # removes the last item
        del dct['key2'] # removes key2 item
"""

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
person.pop('first_name')        # Removes the firstname item
person.popitem()                # Removes the address item
del person['is_married']        # Removes the is_married item


"""
Además, podemos vaciar un diccionario con el método clear() o eliminarlo por completo con "del".
"""

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct








print("\n<----------- CAMBIO DE DICCOINARIO A LISTA ----------->\n")

"""
El método items() cambia el diccionario a una lista de tuplas.
"""

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])






print("\n<----------- COPIAR UN DICCIONARIO ----------->\n")

"""
Podemos copiar un diccionario utilizando el método copy() . Al utilizar copy podemos evitar la mutación del diccionario original.
"""

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct_copy)





print("\n<----------- CLAVES DE UN DICCIONARIO ----------->\n")


"""
En Python es posible obtener las claves que están almacenadas en un diccionario utilizando la funcion keys().
"""


dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])






print("\n<----------- VALORES DE UN DICCIONARIO ----------->\n")

"""
Por el contrario, el método values() nos da todos los valores de un diccionario como una lista
"""

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])