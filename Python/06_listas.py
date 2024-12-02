#LECCIÓN 7 : LISTAS EN PYTHON

"""
Hay cuatro tipos de datos de colección en Python:

    -> Lista: es una colección ordenada y modificable. Permite miembros duplicados.
    -> Tupla: es una colección ordenada e inmutable. Permite miembros duplicados.
    -> Conjunto: es una colección que no está ordenada, indexada ni es modificable, 
                 pero podemos agregar nuevos elementos al conjunto. No se permiten miembros duplicados.
    -> Diccionario: es una colección desordenada, modificable e indexada. 
                 No contiene miembros duplicados.


Una lista es una colección de distintos tipos de datos que está ordenada y es modificable (mutable).
Una lista puede estar vacía o puede tener elementos de distintos tipos de datos.
"""


"""
En esta sección vamos a aprender como utilizar las listas en Python, y para comenzar, vamos a ver 
como podemos crearlas, ya que tenemos dos maneras diferentes, la primera utilizando la función "list()" que 
ya está integrada en Python, y usando los [].
"""

#Lista con la función
lst = list()

empty_list = list() # Esto es una lista vacía, sin elementos
print(len(empty_list)) # 0

#Listas con corchetes
lst = []

empty_list = [] #Lista vacía con corchetes
print(len(empty_list)) # 0

#Vamos a ver un par de ejemplos de listas creadas con corchetes []
frutas = ['platano', 'naranja', 'mango', 'limon']                     # list of fruits
vegetales = ['tomate', 'patata', 'zanahoria','cebolla']      # list of vegetables
animal_products = ['leche', 'carne', 'mantequilla', 'yogurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
paises = ['Finlandia', 'Estonia', 'Dinamarca', 'Suecia', 'Noruega']

print("\n<-------- Ejemplos de listas -------->\n")

# Print the lists and its length
print('Frutasa:', frutas)
print('Numero de frutas:', len(frutas))
print('Vegetales:', vegetales)
print('Numero de vegetales:', len(vegetales))
print('Animal products:',animal_products)
print('Numero de animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Numero de web technologies:', len(web_techs))
print('Paises:', paises)
print('Numero de paises:', len(paises))


"""
De momeno hemos visto un ejemplo donde todas las listas tienen elementos del mismo tipo de datos,
sin embargo, podemos crear listas con elementos de diferentes tipos
"""

lst = ['Rodrigo', 22, True, {'Pais':'Spain', 'city':'Arnedo'}]


"""
La manera de acceder a cada elemento de una lista es mediante su índice. 
El índice de una lista comienza desde 0, y termina en el número de elementos que tenga la lista menos 1.
Sin embargo, en Python, no solo podemos utilizar la indexación positiva, sino que también podemos utilizar
la indexación negativa para recorrer una tabla, donde el valor -1 hace referencia al último elemento de l lista,
y para acceder al primero, solo tendriamos que acceder al -nºelementos_lista
"""
print("\n<-------- Indexación positiva -------->\n")

fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0] # we are accessing the first item using its index
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

print("\n<-------- Indexación negativa -------->\n")

fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)      # banana
print(last_fruit)       # lemon
print(second_last)      # mango



"""
Si os acordáis, en uno de los primeros temas/lecciones vimos que los strings se podían desempaquetar en variables, pues las listas no son menos,
y también podemos desempaquetarlas de diferentes maneras.
Vimos que para poder desempaquetar todo un string, teníamos que crear tantas variables como char tenía el string, sin embargo, os mentí,
ya que tenemos una manera para poder almacenar todos los valores que nosotros queramos, y podemos hacerlo de varias maneras.
Con los siguientes ejemplos lo vais a entender mejor : 
"""

print("\n<-------- Desempaquetado con restos al final -------->\n")

lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']

print("\n<-------- Desempaquetado con restos por medio -------->\n")

first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10

print("\n<-------- Desempaquetado con restos por medio -------->\n")

countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *hola,es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(hola)
print(es)

"""
Después de ver los diferentes ejemplos, podemos ver que si creamos tantas variables como elmentos tiene la lista, cada elemento
se amacenaría en una variable.

Por el contrario, con el símbolo "*" al principio de una variable, le estamos indicando al programa que desempaquete en ella todos los
elementos desde el índice en el que estuviera, hasta que llegue al final, a no ser que nos encontremos "x" variables declaradas después, que almacenarán
"x" valores.
"""


print("\n<-------- CORTAR LISTAS -------->\n")

"""
Ya lo vimos en secciones anteriores, pero podemos acceder a un numero concreto de elementos de una lista, pudiendo elegir desde y hasta donde cortamos la lista.
Podemos hacerlo mediante indexación positiva, y también mediante indexación negativa.

"""
#Indexacion positiva
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits
# this will also give the same result as the one above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the first index
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']

print("\n")

#Indexacion negativa    
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # it returns all the fruits
orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']




print("\n<-------- MODIFICAR LISTAS -------->\n")

"""
Como ya sabemos, las listas están compuestas por una serie de elementos, y podemos acceder a ellos mediante un índice.
Otra de las funciones que podemos hacer, lógicamente, es modificar dichos elementos, lo único que tenemos que hacer es acceder 
a la posición de la lista donde queremos modificar un elemento, y asignarle otro valor, además al no tener un tipo concreto en Python, 
podemos modificar por ejemplo un elemento de tipo int a tipo string, etc.
"""
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']


print("\n<-------- COMPROBAR LISTAS -------->\n")

"""
En Python podemos comprobar de una manera muy directa si en una lista esta comprendido un elemento en concreto.
La sintaxis es: 
    
    -> elemento in lista : Devolverá el valor True si lo ha encontrado, o False en caso contrario.
"""

fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False


print("\n<-------- AGREGAR ELEMENTOS -------->\n")


"""
A diferrencia de otros lenguajes de programación, en Python podemos agregar de una manera muy directa un elemento nuevo 
al final de una lista. Para ello usamos el método append() .

-> La sintaxis para agregar elementos es : 
    
    -> lst = list()
       lst.append(item)
"""

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
print(fruits)



print("\n<-------- INSERTAR ELEMENTOS -------->\n")

"""
Acabamos de ver como agregar un elemento al final de una lista, pero, ¿y si queremos agregarlo en un índice en concreto?
A este concepto se le llama insertar un elemento en la lista, y en Python utilizamos el método insert().
Tened en cuenta que los demás elementos se desplazan hacia la derecha.
El método insert() toma dos argumentos: índice y un elemento para insertar.

La sintaxis es :

    -> lst = ['item1', 'item2']
       lst.insert(index, item)
"""

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)



print("\n<-------- ELIMINAR ELEMENTOS -------->\n")


"""
En Python podemos eliminar elemenos de una lista de varias maneras, asi que vamor a ir viéndolas una a una.
"""

"""
Para comenzar, podemos eliminar un elemento en concreto de una lista con el método remove().

La sintaxis es :
    ->  lst = ['item1', 'item2']
        lst.remove(item)

"""

print("\n<-------- remove() -------->\n")

fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon', 'banana'] - this method removes the first occurrence of the item in the list
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango', 'banana']



"""
También podemos utilizar el método pop(), que elimina el índice especificado (o el último elemento si no se especifica el índice).
La sintaxis es : 

    ->  lst = ['item1', 'item2']
        lst.pop()       # last item
        lst.pop(index)
"""

print("\n<-------- pop() -------->\n")

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)
print(fruits)       # ['orange', 'mango']


"""
La palabra clave "del" elimina el índice especificado y también se puede utilizar para eliminar elementos dentro del rango del índice. 
También puede eliminar la lista por completo.
Y la sintaxis que tenemos que utilizar es :

    ->  lst = ['item1', 'item2']
        del lst[index] # solo elimina el elemento del índice
        del lst        # elimina toda la lista
"""

print("\n<-------- del -------->\n")

fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)        # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1]
print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
del fruits[1:3]     # Elimina los items entre los índices dados, pero no icluye el segundo índice.
print(fruits)       # ['orange', 'lime']
del fruits
#print(fruits)       # Esto dará un erorr: NameError: name 'fruits' is not defined

"""
Directamente borra toda la memoria que puede haber dentro de la variable, lo que signfica que si intentamos usarla,
como en el último ejemplo, nos dará un error como si no la hubiesemos inicializado.
"""




print("\n<-------- BORRAR ELEMENTOS -------->\n")

"""
Ahora mismo, hemos visto como eliminamos los elementos, y estos puede ser muy útil, pero puede que realmente nuestro objetivo sea borrar, no eliminar.
Por ejemplo, en el último ejemplo, si eliminamos la tabla, es como si no tuviesemos una lista en la variable, sin embargo, puede que simplemente 
queramos vaciar la lista, y que esta se quede vacía.

    ->  lst = ['item1', 'item2']
        lst.clear()
"""

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)       # []




print("\n<-------- COPIAR ELEMENTOS -------->\n")


"""
Es posible copiar una lista reasignándola a una nueva variable de la siguiente manera: list2 = list1.
Ahora, list2 es una referencia de list1, cualquier cambio que hagamos en list2 también modificará la original, list1. 
Pero hay muchos casos en los que no queremos modificar la original, sino que queremos tener una copia diferente.
Una forma de evitar el problema anterior es usar copy() .

    ->  lst = ['item1', 'item2']
        lst_copy = lst.copy()
"""

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']




print("\n<-------- UNIR LISTAS -------->\n")


"""
Hay varias formas de unir o concatenar dos o más listas en Python. La primera de ellas es con el operador "+".
De esta manera, si sumamos list1 + list2 , los elementos de list se concatenarán a continuación del elemento final de list1.

    -> list3 = list1 + list2
"""

positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables ) # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

print("\n")

"""
También podemos unir listas mediante el método extend(). El método extend() permite añadir una lista a otra lista.

    ->  list1 = ['item1', 'item2']
        list2 = ['item3', 'item4', 'item5']
        list1.extend(list2)
"""

num1 = [0, 1, 2, 3]
num2= [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1) # Numbers: [0, 1, 2, 3, 4, 5, 6]
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers) # Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits ) # Fruits and vegetables: ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']





print("\n<-------- CONTAR ELEMENTOS DE UNA LISTA -------->\n")

"""
En ciertas ocasiones podemos querer contar cuantas veces se repite un elemento en concreto en una lista, y utilizamos el método count().
El método count() devuelve el número de veces que aparece un elemento en una lista.

La sintaxis es :    

    ->  lst = ['item1', 'item2']
        lst.count(item)
"""

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3



print("\n<-------- ÍNDICE DE UN ELEMENTO -------->\n")


"""
El método index() devuelve el índice de un elemento de la lista.
Este método, en caso de encontrar dos elementos con el mismo valor dentro de una lista, solo devuelve el índice del primer elemento encontrado 
dentro de la misma.

    ->  lst = ['item1', 'item2']
        lst.index(item)
"""

fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))           # 2,


print("\n<-------- INVERTIR UNA LISTA -------->\n")

"""
Si queremos, también podemos invertir todos los elementos de una lista utilizando el método reverse().
El método reverse() invierte el orden de una lista.

    ->  lst = ['item1', 'item2']
        lst.reverse()
"""

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits) # ['lemon', 'mango', 'orange', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages) # [24, 25, 24, 26, 25, 24, 19, 22]


print("\n<-------- ORDENAR UNA LISTA -------->\n")

"""
Por último en esta sección, vamos a ver como podemos ordenar los elementos de una lista.
Para ordenar listas podemos utilizar el método sort() o las funciones integradas de sorted() .
El método sort() reordena los elementos de la lista en orden ascendente y modifica la lista original. 
Si un argumento del método sort() reverse es igual a true, ordenará la lista en orden descendente.

    ->  lst = ['item1', 'item2']
        lst.sort()                # ascending
        lst.sort(reverse=True)    # descending
"""

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)             # sorted in alphabetical order, ['banana', 'lemon', 'mango', 'orange']
fruits.sort(reverse=True)
print(fruits) # ['orange', 'mango', 'lemon', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages) #  [19, 22, 24, 24, 24, 25, 25, 26]

ages.sort(reverse=True)
print(ages) #  [26, 25, 25, 24, 24, 24, 22, 19]

"""
En caso de tener una lista de strings, la ordena según el orden alfabético. 
"""

print("\n<-- Sorted -->\n")
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))   # ['banana', 'lemon', 'mango', 'orange']
# Reverse order
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits,reverse=True)
print(fruits)     # ['orange', 'mango', 'lemon', 'banana']


"""
Si utilizamos el método sorted, no tenemos por qué modificar la lista que queremos ordenar.
"""
