#LECCIÓN 8 : LAS TUPLAS EN PYTHON


print("\n<----------- TUPLAS EN PYTHON ----------->\n")

"""
Una tupla es una colección de diferentes tipos de datos que está ordenada y no se puede cambiar (inmutable). 
Las tuplas se escriben entre corchetes, (). Una vez que se crea una tupla, no podemos cambiar sus valores. 
No podemos usar métodos de agregar, insertar o eliminar en una tupla porque no es modificable (mutable).
A diferencia de una lista, una tupla tiene pocos métodos. Métodos relacionados con las tuplas:

    -> tuple(): para crear una tupla vacía
    -> count(): para contar el número de un elemento especificado en una tupla
    -> index(): para encontrar el índice de un elemento específico en una tupla
    -> Operador: para unir dos o más tuplas y crear una nueva tupla.


La sintaxis qe utilizamos en Python para crear una tupla es : 
    
    ->  empty_tuple = ()
        # o con el contructor de la tupla
        empty_tuple = tuple()
"""

#tpl = ('item1', 'item2','item3')
fruits = ('banana', 'orange', 'mango', 'lemon')
print(fruits)


print("\n<----------- LONGITUD DE TUPLAS ----------->\n")

"""
Con las tuplas, igual que con e resto de elementos, también podemos consultar su longitud con el método len
"""

tpl = ('item1', 'item2', 'item3')
print(len(tpl))


print("\n<----------- ACCEDER A LOS ELEMENTOS DE UNA TUPLA ----------->\n")


"""
De manera similar al tipo de datos de listas,podemos utilizar indexación positiva o negativa para acceder a los elementos de una tupla.

    ->  tpl = ('item1', 'item2', 'item3')
        first_item = tpl[0]
        second_item = tpl[1]

    ->  tpl = ('item1', 'item2', 'item3','item4')
        first_item = tpl[-4]
        second_item = tpl[-3]
"""

fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index =len(fruits) - 1
last_fruit = fruits[last_index]
print(second_fruit)


fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]
print(last_fruit)


print("\n<----------- CORTAR TUPLAS ----------->\n")

"""
Podemos dividir una subtupla especificando un rango de índices donde comenzar y donde terminar en la tupla;
el valor de retorno será una nueva tupla con los elementos especificados.

La sintaxis para lograrlo es : 

    ->  tpl = ('item1', 'item2', 'item3','item4')
        all_items = tpl[0:4]         # todos los items
        all_items = tpl[0:]         # todos los items
        middle_two_items = tpl[1:3]  # no incluye el index 3

    ->  tpl = ('item1', 'item2', 'item3','item4')
        all_items = tpl[-4:]         # todos los items
        middle_two_items = tpl[-3:-1]  # no incluye el index 3 (-1)
"""

#Usando índices positivos
fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]   
all_fruits= fruits[0:]      
orange_mango = fruits[1:3]  
orange_to_the_rest = fruits[1:]
print(orange_to_the_rest)

#Usando índices negativos
fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]   
orange_mango = fruits[-3:-1] 
orange_to_the_rest = fruits[-3:]
print(orange_to_the_rest)


print("\n<----------- CAMIAR TUPLAS A LISTAS ----------->\n")

"""
Esto es muy útil, ya que las tuplas son inmutables, por lo que si queremos modificar los elementos de una tupla, tendremos que transformarla 
a una lista.
Podemos cambiar tanto tuplas a listas como listas a tuplas.

La sintaxis es muy sencilla : 

    ->  tpl = ('item1', 'item2', 'item3','item4')
        lst = list(tpl)
"""

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')


"""
De esta manera hemos conseguido modificar una tupla, considerada inmutable.
"""

#fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment




print("\n<----------- COMPROBAR ELEMENTOS ----------->\n")

"""
Al igual que en las listas, podemos comprobar si cierto elemento se encuentra en una tupla usando "in".

    ->  tpl = ('item1', 'item2', 'item3','item4')
        'item2' in tpl # True
"""


fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False



print("\n<----------- UNIR TUPLAS ----------->\n")

"""
Podemos unir dos o más tuplas usando el operador "+"

        ->  tpl1 = ('item1', 'item2', 'item3')
            tpl2 = ('item4', 'item5','item6')
            tpl3 = tpl1 + tpl2
"""


fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)



print("\n<----------- ELIMIAR ELEMENTOS DE UNA TUPLA ----------->\n")

"""
A diferencia de las listas, como hemos visto, las tuplas son inmutables, por ello es imposible borrar elementos de una tupla.
Sin embargo, si que podemos elminar la tupla en sí utilizando la palabra reservada "del".
Recordad que esto es como si eliminásemos toda la memoria reservada para la tupla, asi que si la intentamos utilizar
nos dará un error de que la variable no está definida.
"""

fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits