#LECCIÓN 9 : SETS EN PYTHON

"""
Un conjunto o set es una colección de elementos. La definición matemática de un conjunto se puede aplicar también en Python.
Un conjunto es una colección de elementos distintos no ordenados y no indexados. En Python, un conjunto se usa para almacenar elementos únicos y 
es posible encontrar la unión , intersección , diferencia , diferencia simétrica , subconjunto , superconjunto y conjunto disjunto entre conjuntos.
"""

print("\n<----------- CREACCIÓN DE SETS ----------->\n")

"""
Como para el resto de tipos de datos más complejos como listas o tuplas, podemos utilizar la función incorporada set().

    -> Podemos crear un conjunto vacío o con elementos desde un inicio
"""

st = set()
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits)

print("\n<----------- LONGITUD DE SETS ----------->\n")

"""
Y de la misma manera, podemos comprobar su longitud usando la funcion len()

    ->  st = {'item1', 'item2', 'item3', 'item4'}
        len(st)
"""

fruits = {'banana', 'orange', 'mango', 'lemon'}
print(len(fruits))



print("\n<----------- ACCEDER A LOS ELEMENTOS DE UN SET ----------->\n")

"""
Para poder acceder a los elementos de un set, usamos los bucles. 
Para ello podemos utilizar los rangos utilizados y vistos en la sección de bucles para poder recorrerlos.
"""



print("\n<----------- COMPROBAR LOS ELEMENTOS DE UN SET ----------->\n")

"""
Al igual que en otros tipos de datos, utilizamos el "in" para compobar si cierto elemento se encuentra en el conjunto.
"""

fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits ) # True






print("\n<----------- AGREGAR ELEMENTOS DE UN SET ----------->\n")

"""
En otras secciones hemos visto como podemos agregar elementos a una lista o tupla, y en este caso, utilizamos
la funciín add().
Una vez creado un conjunto no podemos cambiar ningún elemento pero podemos agregar elementos adicionales.

La sintxis es : 

    ->  st = {'item1', 'item2', 'item3', 'item4'}
        st.add('item5')
"""

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')


"""
Para los sets en Python, tenemos una función con la que podemos agregar de una sola vez varios elementos a un conjunto/set.
Podemos agregar varios elementos mediante update() La función update() permite agregar varios elementos a un conjunto.
La función update() toma como argumento una lista.

    ->  st = {'item1', 'item2', 'item3', 'item4'}
        st.update(['item5','item6','item7'])
"""

fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits)
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print(fruits)






print("\n<----------- BORRAR ELEMENTOS DE UN SET ----------->\n")  


"""
Podemos eliminar un elemento de un conjunto utilizando el método remove() . Si no se encuentra el elemento, el método remove() generará errores, 
por lo que es bueno verificar si el elemento existe en el conjunto dado. Sin embargo, el método discard() no genera ningún error.
"""

st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
print(st)

"""
Los métodos pop() eliminan un elemento aleatorio de una lista y devuelven el elemento eliminado.
"""

fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits.pop())  # removes a random item from the set
#Esta función devuelve el elemento que ha elimniado


"""
Si queremos limpiar o vaciar el conjunto utilizamos el método clear .
"""

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set() Indica que tenemos un set vacío.


"""
Si queremos eliminar el conjunto en sí utilizamos el operador "del", como hemos visto anteriormente.
"""

fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits





print("\n<----------- CONVERSIÓN DE UN SET ----------->\n") 


"""
Podemos convertir una lista en un conjunto y un conjunto en una lista. 
Al convertir una lista en un conjunto se eliminan los duplicados y solo se reservan los elementos únicos.
"""

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}






print("\n<----------- UNIR SETS ----------->\n") 

"""
Podemos unir dos conjuntos usando el método union() o update() .
El método union() devuelve un nuevo conjunto, mientras que update inserta un conjunto en un conjunto dado
"""

#Union
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}



#Update
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}







print("\n<----------- INTERSECCIÓN DE DOS SETS ----------->\n") 


"""
La intersección devuelve un conjunto de elementos que se encuentran en ambos conjuntos. 

La sintaxis para completar la intersección es :

    ->  st1 = {'item1', 'item2', 'item3', 'item4'}
        st2 = {'item3', 'item2'}
        st1.intersection(st2) # {'item3', 'item2'}
"""


whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
intersection = whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}
print(intersection)

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
intersection = python.intersection(dragon)     # {'o', 'n'}
print(intersection)



print("\n<----------- SUBCONJUNTOS O SUPERCONJUNTOS DE UN SET ----------->\n") 

"""
En Python podemos comprobar si un conjunto es un subconjunto o superconjunto de otros conjuntos.

¿Qué funciones utilizamos para comprobar si es un subconjunto o superconjunto?

    -> Subconjunto: issubset()
    -> Superconjunto: issuperset()

        st1 = {'item1', 'item2', 'item3', 'item4'}
        st2 = {'item2', 'item3'}
        st2.issubset(st1) # True
        st1.issuperset(st2) # True

"""


whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.issubset(even_numbers)) # False, because it is a super set
print(whole_numbers.issuperset(even_numbers)) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.issubset(dragon))     # False





print("\n<----------- DIFERENCIA ENTRE DOS SETS ----------->\n") 

"""
En ocasiones podemos encontrar interesante comprobar cuales son las diferencias entre dos conjuntos.
Para ello podemos utilizar la función difference().

    ->  st1 = {'item1', 'item2', 'item3', 'item4'}
        st2 = {'item2', 'item3'}
        st2.difference(st1) # set()
        st1.difference(st2) # {'item1', 'item4'} => st1\st2
"""

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.difference(even_numbers)) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.difference(dragon))     # {'p', 'y', 't'}
print(dragon.difference(python))     # {'d', 'r', 'a', 'g'}









print("\n<----------- DIFERENCIA SIMÉTRCA ENTRE DOS SETS ----------->\n") 


"""
La función symmetric_difference() devuelve la diferencia simétrica entre dos conjuntos. Es decir, 
devuelve un conjunto que contiene todos los elementos de ambos conjuntos, excepto los elementos que están presentes en ambos conjuntos,
matemáticamente: (A\B) ∪ (B\A)
"""

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
print(whole_numbers.symmetric_difference(some_numbers)) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.symmetric_difference(dragon))  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}






print("\n<----------- CONJUNTOS DISJUNTOS ----------->\n") 


"""
Si dos conjuntos no tienen un elemento o elementos en común, los llamamos conjuntos disjuntos. 
Podemos comprobar si dos conjuntos son conjuntos o disjuntos utilizando el método isdisjoint() .

La sintaxis para comprobarlo es : 
    ->  st1 = {'item1', 'item2', 'item3', 'item4'}
        st2 = {'item2', 'item3'}
        st2.isdisjoint(st1) # False
"""

even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers)) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.isdisjoint(dragon))  # False, there are common items {'o', 'n'}