#LECCIÓN 2 : LAS VARIABLES EN PYTHON

"""

Ahora toca aprender lo más sencillo de todo lenguaje de programación :

-> ¿Qué tipos básicos tenemos en Python?
    La respuesta es simple, los mismos tipos que en la mayoría de lenguajes de programación

-> Y ahora, ¿Cómo declaramos e inicializamos estás variables?
    Pues, en Python, tenemos algo soprendente, y es que las variables son totalmente dinámicas,
    que quiero decir con esto, no tenemos que decirle de que tipo es la variable, simplemente 
    al asignarle un valor, la variable cogerá automáticamente el tipo que sea necesario de manera dinámica.

"""

NumeroEntero = 3
NumeroDecimal = 3.3

"""

Como véis en los ejemplos de aquí arriba, la variable NumeroEntero, es un tipo "int" o "integer".
Y de la misma manera, la variable NumeroDecimal, es de tipo "double" o "float".

En Python, para crear una variable, solo necesitamos darle un identificador, y el tipo de la misma
se irá dinámicamente adaptando según el valor que la variable adquiera en cada momento.

Es importante decir, que como en todo lenguaje de programación, existe una notación de variables por defecto.
Lo más normal en otros lenguajes, es la notación cammel, es decir, el comienzo de cada palabra escribirlo en mayúscula,
o en su defecto, hacer lo mismo pero la primera letra de todas con minúscula (numeroEntero, numeroDecimal).

Sin embargo, en python, la notación que se considera una buena práctica de programación es la siguiente : 
    -> Todas las variables se escriben en minúscula.
    -> Si la variable contiene varios nombres, se separan por una barra baja "_"
    -> Algún ejemplo de identificadores serían : numero_entero , numero_decimal, etc.

"""

numero_entero = 3
numero_decimal = 3.3

"""

Ahora si tenemos dos variables con una buena práctica de programación, siguiendo una notación.
Y al igual que hemos creado dos variables numéricas, podemos crear variables con cadenas de texto o valores booleanos.

"""

boolean_variable = True # Esto es una variables de tipo bool
string_variable = "Esto una variable de tipo String"
lista_variable = [0,1,3] # Esto es una variables de tipo Lista o Array

"""

Si en medio de la ejecución de nuestro código, tenemos curiosidad sobre que tipo de dato lleva una variable,
podemos utilizar una de las funciones que vienen importadas por defecto en Python, llamada "type".
Si juntamos esta función, con la función print que ya hemos visto, tendremos por consola el tipo de una variable.

"""

print(type(numero_entero))
print(type(numero_decimal))
print(type(string_variable))
print(type(lista_variable))
print(type(boolean_variable))


"""

Ya véis que con esta función podemos ver en cada momento de que tipo es cierta variable.

"""


"""

Ahora vamos a ver algo muy obvio, como hacemos print y encadenamos variables?
->La respuesta es muy sencilla, print recibe parámetros separados por comas, donde podemos meter tantas variables como queramos.

"""

#Concatenación de variables en un print
print("\nEsta es la variables decimal : ", numero_decimal, ". Y esta es la variable booleana : ",boolean_variable,"\n")



"""

¿Qué más cosas podemos hacer con variables?
Pues algo muy sencillo, es el cambio de tipo, veamos un ejemplo:

"""


variable_entera = 3

print(type(variable_entera))

variable_string = str(variable_entera)

print(type(variable_string),"\n")

"""

Esto es muy sencillo, es lo que conocemos como conversión de tipo, y estoy seguro de que lo habéis visto en otros lenguajes como java.
Si véis los prints por consola, cada variable es del tipo correspondiente al valor, una de tipo entero y otra de tipo str o string.
Sin embargo, para poder hacer un print, no es necesario hacer una conversión de tipo de las variables a str ya que el propio print 
es capaz de automáticamente convertir todos los tipos a cadena de carácteres.

"""

"""

A continuación, voy a aprovechar y os dejo un link a lo documentación oficial de Python, donde podéis ver todas las funciones que nos ofrece por defecto
Python y que podemos utilizar, como hemos visto, tenemos entre mucas otras la función "print" y la función "str" para el cambio de tipo.

-> Link a la documentación Built-in Functions : https://docs.python.org/3/library/functions.html

"""



#FUNCIONES DEL SISTEMA
"""

Otra función del sistema que están precargadas es la función "len".
La función nos dice la longitud de la variable, recibe un parámetro en tipo str

"""

print(len(str(variable_entera)))
print(len(string_variable),"\n")



#VARIABLES EN UNA SOLA LÍNEA
"""

Como en otros lenguajes de programación, podemos declarar variables en una sola línea.

"""

name,surname,alias,age = "Rodrigo" , "Moure" , "Rodri" , 35

"""

Hemos creado cuatro variables, y a cada una le hemos asigando un valor separados por comas, cada una será del tipo correspondiente.
Sin embargo, esto puede ser un peligro si nos ponemos a definir variables en una sola línea y nos confundimos sobre a cual le asignamos cada valor.
Con esto quiero decir que se puede hacer, pero que no es una buena práctica en Python.

"""


#INPUT EN PYTHON

variable_entera = input("Escribe una variable del tipo que desees : ")

print("La variable introducida por el usuario es del tipo : ", type(variable_entera))

"""

Realmente, a no ser que estemos generando un script o alguna aplicación que utilice directamente la terminal, no es muy útil, 
el valor de los tipos es de tipo str.

Si os fijáis, acaba de pasar algo ilógico en cualquier otro lenguaje de programación.
Igual no os habéis dado cuenta, pero hemos utilizado una variable entera creada con anterioridad para leer el input de usuario,
y si os fijáis en lo que ha devuelto el tipo de esa variable después de leer, nos ha dicho que es de tipo str, cuando antes era un int.
Con esto quiero deciros que Python no trabaja con un tipo de datos indefinido, por lo que el tipo de datos de una variable no solo se asigna
dinámicamente la primera vez que le damos un valor, sino todas las veces que le demos un valor con un tipo diferente.
Esto puede ser muy útil para reutilzar variables, o muy peligroso y problemático, asi que os recomiendo no utilizarlo o lo más mínimo posible.

"""

variable_entera_dos = 3
print(type(variable_entera_dos))
variable_entera_dos = "Ahora es un string"
print(type(variable_entera_dos))

"""

Como os decía, esto puede ser peligroso en proyectos en equipo donde alguién se vuelva loco y cambie una variable de tipo, y el resto de 
programdores sigan pensando que era del tipo que ellos la habrían creado.

"""

tipo_string:str = "Esta es una variable de tipo string" #Mera información


"""

Como pogramadores, podemos fijar el tipo de dato que tiene una variable en su creación, pero esto no es más que mera información,
ya que se le puede seguir cambiando el tipo las veces que queramos

"""

tipo_string = 3 #Ahora es un tipo entero.


