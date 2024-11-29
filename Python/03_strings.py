#LECCIÓN 4 : LOS STRINGS EN PYTHON

#Strings de ejemplo
my_string = "String"
my_other_string = "Other String"

"""
Si recordáis, hemos visto algunas funciones ya sobre este tipo de datos básico, como puedo ser str para forzar la conversión,
o como puede ser "len" para sacar la longitud de un string.
"""
print(len(my_string))
print(len(my_other_string) , "\n")





"""
También hemos visto que podemos concatenar strings con el operador aritmético "+", o incluso multiplicarlo por un entero con "*"
"""
print(my_string + " " + my_other_string)
print((my_string * 5) + " " + (my_other_string*10), "\n")






"""
Indirectamente, otra de las funciones de los strings ya os la he enseñado, que es lo que se conoce como salto de línea.
Si os fijáis en la consola, separo los diferentes ejemplos utilizando el \n para realizar un salto de línea.

También podemos utilizar las tabulaciones, utilizando el \t
"""
string_salto_de_linea = "Esto es un ejemplo\ncon un salto de linea\n"
print(string_salto_de_linea)

string_tab = "\tEsto es un ejemplo \tde la tabulacion en Python\n"
print(string_tab)

#SI YO QUIERO ESCRIBIR UN \t o \n por pantalla, basta con utilizar doble \\
scape_string = "\\tEsto es un ejemplo de la tabulacion en Python\\n"
print(scape_string)






"""
Ahora vamos a ver como podemos formatear un string
"""

name, surname, age = "Rodrigo" , "Cabello" , 22

print("Mi nombre es %s, mi apellido es %s y mi edad es %d" .format(name,surname,age))
print("Mi nombre es %s, mi apellido es %s y mi edad es %d" %(name,surname,age))

"""
El formateo de un string sirve para en medio de una cadena de texto, especificar que vamos a colocar un parámetro, y de que tipo, más adelante.
Des esta manera nos ahorramos el tener que estar concatenando cada variable de manera manual.

Si os fijas, también podemos ver que con .format no tenemos que hacerlo de esa forma, sino que tenemos que ponerlo de la siguiente manera.
"""
#Ahora si funciona de la misma manera que con %(parámetros)
print("Mi nombre es {}, mi apellido es {} y mi edad es {}" .format(name,surname,age))


"""
Y Rodrigo, ¿qué diferencia hay entre uno u otro?
La diferencia principal y fundamental es que de la forma .format, se escriben los valores tal cual en pantalla, sin identificar de que tipo son,
sin embargo, utilizando la forma %(), tenemos que especificar en cada lugar que queremos colocar un valor, de que tipo va a ser este, y de esta 
manera, podemos asegurarnos en un futuro de que los parámetros que nos pasan al print están bien, ya que si pedimos un valor de tipo int (%d) 
y nos pasan uno de tipo str(%s) nos va a fallar, de la otra manera no fallaría.
"""

#ESTE CÓDIGO FALLA YA QUE LA EDAD QUEREMOS QUE SEA UN INT PERO LE ESTAMOS PASANDO UN STRING
#Sirve como código defensivo
#print("Mi nombre es %s, mi apellido es %s y mi edad es %d" %(name,surname,"35"))


#Otra forma útil y corta es la siguiente
print(f"Mi nombre es {name}, mi apellido es {surname} y mi edad es {age}")

"""
Con este último format, conseguimos lo mismo que con .format, pero nos queda más claro que lugar va a ocupar cada variable.
"""




print("\n")



"""
Ahora vamos a ver el desempaquetado de cadenas de carácteres.
Podemos crear varias variables y asignarle una cadena de caracteres, yu
"""
language = "Python"
a,b,c,d,e,f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)



print("\n")



"""
En Python podemos acceder a un string en función de un índice, y como ya sabemos, en programación, la cuenta comienza desde cero. Por lo tanto, la primera letra 
de una cadena está en el índice cero y la última letra de una cadena está en la longitud de la cadena menos uno
"""
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n


print("\n")


"""
En Python, si queremos empezar por el último índice, también podemos utilizar el -1 y asi sucesivamente
"""
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o



print("\n")


"""
En Python, otra cosa que podemos hacer muy interesante es dividir cadenas en subcadenas.
¿Y cómo hacemos esto?
Tenemos diferentes formas para dividir una cadena de texto, por ejemplo :
    -> indice1 : indice2 --> Empieza la cadena en el caracter "indice1" y termina en "indice2", pero sin incluir este último.
    -> indice :  --> Empieza en el indice indicado hasta el final
    -> : indice --> Empieza en el indice 0 y termina en  indice 
"""
language = 'Python'
first_three = language[1:4]
print(first_three) #yth
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon
first_three = language[:3]
print(first_three)   # Pyt




print("\n")



"""
Que más cosas podemos hacer en Python con los string, pues por ejemplo podemos invertir cadenas fácilmente.
    -> Solo tenemos que utiliza "variable::-1"
    -> El valor que le indicamos indica cada cuantos valores coge un caracter
"""


reversed = 'Hello, World!'
print(reversed[::-1]) # !dlroW ,olleH
print(reversed[::-2]) # !lo ,olH


print("\n")



"""
También es posible omitir caracteres al dividir una cadena pasando el argumento de paso al método de división.
    -> Y como se utiliza esto, language[indice1 : limite : rango]
    -> Aquí lo que conseguimos es empezar en el indice uno, y vamos quedando con los caracterés sumando el rango a indice, hasta que no nos pasemos del limite.
"""


language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto

print("\n\n")



print("<----------- EJEMPLO DE FUNCIONES CON STRINGS ---------------->")
print("\n\n")

#MÉTODOS DE STRINGS
"""
Existen muchos métodos de cadenas que nos permiten formatear cadenas. Ve algunos de los métodos de cadenas en el siguiente ejemplo:

    -> capitalize(): Convierte el primer carácter de la cadena en mayúscula.

    -> count(): Devuelve el número de ocurrencias de un subcadena en una cadena.
                count(substring, start=.., end=..).
                El parámetro start es el índice inicial para contar, y end es el último índice hasta donde se contará.

    -> endswith(): Verifica si una cadena termina con un final especificado.

    -> expandtabs(): Reemplaza el carácter de tabulación con espacios. El tamaño predeterminado de la tabulación es 8. 
                     Acepta un argumento para especificar el tamaño de la tabulación.

    -> find(): Devuelve el índice de la primera ocurrencia de una subcadena. Si no se encuentra, devuelve -1.

    -> rfind(): Devuelve el índice de la última ocurrencia de una subcadena. Si no se encuentra, devuelve -1.

    -> format(): formatea los strings para un mejor output
    
    -> index(): Devuelve el índice más bajo de una subcadena. Los argumentos adicionales indican los índices de inicio y fin 
                (por defecto 0 y la longitud de la cadena menos 1). Si no se encuentra la subcadena, se genera un ValueError.

    -> rindex(): Devuelve el índice más alto de una subcadena. Los argumentos adicionales indican los índices de inicio y fin
                 (por defecto 0 y la longitud de la cadena menos 1).

    -> isalnum(): Verifica si todos los caracteres de la cadena son alfanuméricos (letras y números).

    -> isalpha(): Verifica si todos los elementos de la cadena son caracteres alfabéticos (de la a a la z y de la A a la Z).

    -> isdecimal(): Verifica si todos los caracteres de una cadena son decimales (del 0 al 9).

    -> isdigit(): Verifica si todos los caracteres de una cadena son números (del 0 al 9 y algunos otros caracteres Unicode para números).

    -> isnumeric(): Verifica si todos los caracteres de una cadena son números o caracteres relacionados
                    con números (al igual que isdigit(), pero acepta más símbolos, como ½).

    -> isidentifier(): Verifica si una cadena es un identificador válido, es decir, si es un nombre de variable válido en Python. 

    -> islower(): Verifica si todos los caracteres alfabéticos en la cadena son minúsculas.

    -> isupper(): Verifica si todos los caracteres alfabéticos en la cadena son mayúsculas.

    -> join(): Devuelve una cadena concatenada. Este método se usa para unir los elementos de un iterable (como una lista o tupla) en una sola cadena,
               utilizando el string sobre el cual se llama como separador.

    -> strip(): Elimina todos los caracteres dados al principio y al final de la cadena. Si no se especifican caracteres, 
                elimina los espacios en blanco por defecto.

    -> replace(): Reemplaza una subcadena por una cadena dada.

    -> split(): divide la cadena, utilizando la cadena dada o el espacio como separador

    -> title(): Devuelve una cadena con título en mayúsculas y minúsculas

    -> swapcase(): Convierte todos los caracteres en mayúsculas en minúsculas y todos los caracteres en minúsculas en mayúsculas

    -> startswith(): Comprueba si la cadena comienza con la cadena especificada

Veamos ejemplos de todas las funciones:
"""

print("<-- capitalize -->")
#capitalize
string_example = 'thirty days of python'
print(string_example.capitalize()) # 'Thirty days of python'
print("\n\n")

print("<-- count -->")
#count
string_example = 'thirty days of python'
print(string_example.count('y')) # 3
print(string_example.count('y', 7, 14)) # 1, 
print(string_example.count('th')) # 2`
print("\n\n")

print("<-- endswith -->")
#endswith
string_example = 'thirty days of python'
print(string_example.endswith('on'))   # True
print(string_example.endswith('tion')) # False
print("\n\n")

print("<-- expandtabs -->")
#expandtabs
string_example = 'thirty\tdays\tof\tpython'
print(string_example.expandtabs())   # 'thirty  days    of      python'
print(string_example.expandtabs(10)) # 'thirty    days      of        python'
print("\n\n")

print("<-- find -->")
#find
string_example = 'thirty days of python'
print(string_example.find('y'))  # 5
print(string_example.find('th')) # 0
print("\n\n")

print("<-- rfind -->")
#rfind
string_example = 'thirty days of python'
print(string_example.rfind('y'))  # 16
print(string_example.rfind('th')) # 17
print("\n\n")

print("<-- format -->")
#format
first_name = 'Rodrigo'
last_name = 'Alberto'
age = 250
job = 'teacher'
country = 'Spain'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, age, job, country)
print(sentence)
print("\n")

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result) # The area of a circle with radius 10 is 314

print("\n\n")
print("<-- index -->")
#index
string_example = 'thirty days of python'
sub_string = 'da'
print(string_example.index(sub_string))  # 7
#print(string_example.index(sub_string, 9)) # error
print("\n\n")

print("<-- rindex -->")
#rindex
string_example = 'thirty days of python'
sub_string = 'da'
print(string_example.rindex(sub_string))  # 7
#print(string_example.rindex(sub_string, 9)) # error
print(string_example.rindex('on', 8)) # 19
print("\n\n")

print("<-- isalnum -->")
#isalnum
string_example = 'ThirtyDaysPython'
print(string_example.isalnum()) # True

string_example = '30DaysPython'
print(string_example.isalnum()) # True

string_example = 'thirty days of python'
print(string_example.isalnum()) # False, space is not an alphanumeric character

string_example = 'thirty days of python 2019'
print(string_example.isalnum()) # False
print("\n\n")


print("<-- isalpha -->")
#isalpha
string_example = 'thirty days of python'
print(string_example.isalpha()) # False, space is once again excluded
string_example = 'ThirtyDaysPython'
print(string_example.isalpha()) # True
num = '123'
print(num.isalpha())      # False   
print("\n\n")

print("<-- isdecimal -->")
#isdecimal
string_example = 'thirty days of python'
print(string_example.isdecimal())  # False
string_example = '123'
print(string_example.isdecimal())  # True
string_example = '\u00B2'
print(string_example.isdigit())   # False
string_example = '12 3'
print(string_example.isdecimal())  # False, space not allowed
print("\n\n")

print("<-- isdigit -->")
#isdigit
string_example = 'Thirty'
print(string_example.isdigit()) # False
string_example = '30'
print(string_example.isdigit())   # True
string_example = '\u00B2'
print(string_example.isdigit())   # True
print("\n\n")

print("<-- isnumeric -->")
#isnumeric
num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False
print("\n\n")

print("<-- isidentifier -->")
#isidentifier
string_example = '30DaysOfPython'
print(string_example.isidentifier()) # False, because it starts with a number
string_example = 'thirty_days_of_python'
print(string_example.isidentifier()) # True
print("\n\n")

print("<-- islower -->")
#islower
string_example = 'thirty days of python'
print(string_example.islower()) # True
string_example = 'Thirty days of python'
print(string_example.islower()) # False
print("\n\n")

print("<-- isupper -->")
#isupper
string_example = 'thirty days of python'
print(string_example.isupper()) #  False
string_example = 'THIRTY DAYS OF PYTHON'
print(string_example.isupper()) # True
print("\n\n")

print("<-- join -->")
#join
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'
print("\n")
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'
print("\n\n")

print("<-- strip -->")
#strip
string_example = 'thirty days of pythoonnn'
print(string_example.strip('noth')) # 'irty days of py'
print("\n\n")

print("<-- replace -->")
#replace
string_example = 'thirty days of python'
print(string_example.replace('python', 'coding')) # 'thirty days of coding'
print("\n\n")

print("<-- split -->")
#split
string_example = 'thirty days of python'
print(string_example.split()) # ['thirty', 'days', 'of', 'python']
string_example = 'thirty, days, of, python'
print(string_example.split(', ')) # ['thirty', 'days', 'of', 'python']
print("\n\n")

print("<-- title -->")
#title
string_example = 'thirty days of python'
print(string_example.title()) # Thirty Days Of Python
print("\n\n")

print("<-- swapcase -->")
#swapcase
string_example = 'thirty days of python'
print(string_example.swapcase())   # THIRTY DAYS OF PYTHON
string_example = 'Thirty Days Of Python'
print(string_example.swapcase())  # tHIRTY dAYS oF pYTHON
print("\n\n")

print("<-- startswith -->")
#startswith
string_example = 'thirty days of python'
print(string_example.startswith('thirty')) # True

string_example = '30 days of python'
print(string_example.startswith('thirty')) # False
print("\n\n")