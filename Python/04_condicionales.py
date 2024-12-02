#LECCIÓN 5 : CONDICIONALES



"""
Por defecto, las instrucciones en un script de Python se ejecutan secuencialmente de arriba hacia abajo. 
Si la lógica de procesamiento lo requiere, el flujo secuencial de ejecución puede alterarse de dos maneras:

    -> Ejecución condicional: un bloque de una o más instrucciones se ejecutará si una determinada expresión es verdadera.
    -> Ejecución repetitiva: un bloque de una o más instrucciones se ejecutará repetidamente mientras una determinada expresión sea verdadera.
                             En esta sección, cubriremos las instrucciones if, else y elif. Los operadores de comparación y 
                             lógicos que aprendimos en secciones anteriores serán útiles aquí.
"""



#CONDICION IF
"""
En Python y otros lenguajes de programación, la palabra clave if se utiliza para comprobar 
si una condición es verdadera y ejecutar el código del bloque. Recuerda la sangría después de los dos puntos porque
sino Python no detectará que forma parte del if, en este caso no tenemos llaves sino que lo importante es la identación / sangría.

    -> La sintaxis es la siguiente: 

    if condition:
        parte del código del if
"""

a = 3
if a > 0:
    print('A is a positive number') # A is a positive number

print("\n")


"""
Como se puede ver en el ejemplo anterior, 3 es mayor que 0. La condición era verdadera y se ha ejecutado el código de bloque.
Sin embargo, si la condición es falsa, no vemos el resultado. Para ver el resultado de la condición falsa, deberíamos tener otro bloque, que será else .
"""


#CONDICION ELSE
"""
Si la condición es verdadera se ejecutará el primer bloque, si no se ejecutará la condición else.

    -> La sintaxis es la siguiente : 
        if condition:
            this part of code runs for truthy conditions
        else:
            this part of code runs for false conditions
"""


a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')

print("\n")

"""
En nuestra vida , tomamos decisiones a diario. No tomamos decisiones verificando una o dos condiciones, sino múltiples.
Al igual que la vida, la programación también está llena de condiciones. Usamos elif cuando tenemos múltiples condiciones.

    -> La sintaxis es : 

            if condition:
                code
            elif condition:
                code
            else:
                code
"""
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')


print("\n")

"""
También podemos usar estas expresiones de la siguiente manera:
    
    -> code if condition else code
"""
a = 3
print('A is positive') if a > 0 else print('A is negative') 

print("\n")

"""
En Python, las condiciones se pueden anidar, como imagino que ya habréis visto en otros lenguajes de programación como Java.

    -> La sintaxis es : 
        if condition:
            code
            if condition:
                code

En Python es muy pero que muy importante la identación para saber que lineas de codigo forman parte de que estructura de control.
"""

a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')


print("\n")

"""
Y como hemos visto en secciones anterior, podemos utilizar los operadores lógicos para concatenar condicoines dentro de los condicionales

    ->  Su sintaxis es : 
            -if condition or/and condition:
                code

            -if not condition:
                code
"""
user = 'Rodrigo'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')

print("\n")