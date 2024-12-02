#LECCIÓN 6 : BUCLES


"""
La vida está llena de rutinas. En programación también realizamos muchas tareas repetitivas. 
Para manejar tareas repetitivas, los lenguajes de programación utilizan bucles, y Python, no es menos, también proporciona los siguientes tipos de dos bucles:

    -> Bucle "WHILE"
    -> Bucle "FOR"


"""



#<---------BUCLE WHILE---------->

"""
Como en otros lengujes de programación usamos la palabra reservada while para crear un bucle while. 
Se utiliza para ejecutar un bloque de instrucciones repetidamente hasta que se cumpla una condición dada. 
Cuando la condición se vuelve falsa, las líneas de código posteriores al bucle continuarán ejecutándose.

Los bucles while se ejecutan de manera similar a como lo pueden hacer en otros lenguajes cmoo Java, C++, C#, etc.
¿Y cuál es la sintaxis?:
    
    -> while condition:
            code 

Al igual que en los condicionales, no utilizamos paréntesis para la condición como en otros lenguajes, ni tampoco
colocamos llaves para englobar el código correspondiente al bucle, sino que tras poner dos puntos, lo importante
para indicar que una línea de código pertenece a un bucle es de forma similar a los condicionales, utilizando
la identación o sangría.
""" 

print("\n")
print("<----------- BUCLE WHILE ------------>")
print("\n")
#Un ejemplo sencillo de como imprimir una cuenta


count = 0
while count < 5:
    print(count)
    count = count + 1

    
#prints desde 0 hasta 4


"""
En el bucle while anterior, la condición se vuelve falsa cuando el conteo es 5.
En ese momento, el bucle se detiene. Si nos interesa ejecutar un bloque de código una vez que la condición ya no es verdadera, podemos usar else .
Si, habéis oído bien, en Python podemos colocar un else para indicar una región de código que quermeos que se ejecute cuando no
se cumpla la condición del bucle. Realmente es lo mismo que no poner nada, ya que en el código seguirá ejecutándose de arriba a abajo.

La sintaxis es : 

    ->  while condition:
            code
        else:
            code

"""

print("\n")
print("<-- While : Else -->")

count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)






"""
En Python, al igual que en otros lenguajes, también tenemos una manera para poder salir de un bucle, aunque no se cumpla la condición principal.
Normalmente, en muchas situaciones queremos ejecutar una región de código mientras se cumpla una condición, sin embargo, 
a pesar de que esta no llegue a resultar falsa, podemos querer que si otra condición se cumple, dejemos de ejecutar este código.
La sintaxis es : 

    -> while condition:
        code
        if another_condition:
            code
            break
"""


print("\n")
print("<-- While : Break -->")

count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break



"""
Y de la misma manera con break, también tenemos en Python la manera de poder saltarnos exclusivamente la iteracción actual del bucle ("Continuar")
Para ello podemos utilizar la siguiente sintaxis : 

    -> while condition:
        code
        if another_condition:
            continue
        code
        ...

La palabra reservada "continue" impide que continuemos en caso de tener más código para ejecutar en el bucle, y nos vuelve a la condición.
"""
print("\n")
print("<-- While : Continue -->")

count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1


print("\n")
print("\n")

"""
Bueno, realmente y como ya habéis podido observar, en cuanto al bucle While no tenemos nada nuevo en Python, únicamente que le podemos 
añadir un else para cuando no se cumpla la condición, puede ser útil para cuando salimos de un bucle utilizando un break y no 
porque la condición del bucle sea falsa.
"""




print("\n")
print("<----------- BUCLE FOR ------------>")
print("\n")


"""
Ahora vamos a ver los bucles "FOR" de Python. La palabra clave for se utiliza para crear un bucle for, similar a otros lenguajes de programación,
pero con algunas diferencias de sintaxis.

El bucle se utiliza para iterar sobre una secuencia (que puede ser una lista, una tupla, un diccionario, un conjunto o una cadena).
Algunos de estos tipos de datos los veremos más adelante.

La sintaxis del bucle for en Python es la siguiente : 
    #LISTAS
    -> for iterator in lst:
            code
    #STRINGS
    -> for iterator in string:
            code
    #TUPLAS
    -> for iterator in tpl :
            code 
    #DICCIONARIOS
    -> for iterator in dct : 
            code
    #SETS
    -> for iterator in sets : 
            code

En los diccionarios, elemento qu veremos en temas futuros, se obtiene la clave del diccionario al recorrer el bucle.    

"""

print("\n")
print("<-- FOR: Listas -->")
print("\n")

#En este ejemplo utilizamos una lista de Python (las veremos más adelante)
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # la variable number es temporal y se utilizar para hacer referencia a cada uno de los items de la lista "numbers"
    print(number)       # los número van a ser printeados línea a línea de 0 a 5


print("\n")
print("<-- FOR: String -->")
print("\n")

language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])


print("\n")
print("<-- FOR: Tuplas -->")
print("\n")

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)


print("\n")
print("<-- FOR: Diccionario -->")
print("\n")

person = {
    'first_name':'Rodrigo',
    'last_name':'Cabello',
    'age':22,
    'country':'Spain',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out

"""
Relamente este tipo de bucles también los encontramos en otros lenguajes de programación, y se llaman bucles for each.

Si leemos de manera natural el bucle sería algo así : 
Por ejemplo para una lista de la compra:
    
    -> Para cada producto en la lista de la compra... hacemos ...

Y de esta manera, es como si estuviesemos accediendo a la posición "i" en cualquier bucle for de otro lenguaje, pero de manera más sencilla y natural.

"""



"""
El bucle FOR, no es menos que el while, por lo que podemos utilizar las expresiones "Continue" y "Break" de la misma
manera que en el bucle While.

La sintaxis es :
    
    -> for iterator in sequence:
            code  
            if condition:
                break
                
    -> for iterator in sequence:
            code  
            if condition:
                continue
"""

print("\n")
print("<-- Break -->")
print("\n")

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break

print("\n")
print("<-- Continue -->")
print("\n")

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')





"""

En Python tenemos una función muy interesante y que podemos aplicar para los bucles for.
La función range() se utiliza para crear una lista de números. El rango (inicio, fin, incremento) acepta tres parámetros: inicio, fin e incremento. 
De manera predeterminada, comienza desde 0 y el incremento es 1. La secuencia de rango necesita al menos 1 argumento (fin). 
La sintacis para la creación de secuencias con rango es :

    -> for iterator in range(start, end, step):

"""

#Ejemplo de como utilizar la funcion range para crear listas y sets.
lst = list(range(11)) 
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # Si tiene dos argumentos, indican el principio y fin, el incremento se queda en 1 por defecto.
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

#Ejemplo de creación de listas y sets con los 3 parámetrs
lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}


for number in range(11):
    print(number)   # prints 0 to 10, not including 11



"""
Al igual que en otros lenguajes de programación, podemos anidar tantos bucle como deseemos o como necesitemos.

La sintaxis típica para un bucle bidimensional es : 
    ->  for x in y:
            for t in x:
                print(t)


"""

person = {
    'first_name': 'Rodrigo',
    'surname': 'Cabello',
    'age': 22,
    'country': 'Spain',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)



"""
Al igual que en el bucle while, también podemos utilizar la estructura de control "else" en caso de que queramos
ejecutar código exclusivamente cuando no se salga de un bucle por un break.
"""