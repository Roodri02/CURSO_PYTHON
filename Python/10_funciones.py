# LECCIÓN 10 : FUNCIONES EN PYTHON

"""
Hasta ahora hemos visto muchas funciones integradas de Python. En esta sección, nos centraremos en las funciones personalizadas.
¿Qué es una función? Antes de empezar a crear funciones, aprendamos qué es una función y por qué las necesitamos.
"""


"""
Una función es un bloque de código reutilizable o instrucciones de programación diseñadas para realizar una determinada tarea.
Para definir o declarar una función, Python proporciona la palabra clave "def" . 
La siguiente es la sintaxis para definir una función. El bloque de código de la función se ejecuta solo si se llama o invoca la función.
"""




print("\n")
print("<----------------- FUNCIONES SIN PARÁMETROS ------------------->")
print("\n")

"""
Cuando creamos una función, la llamamos declaración de función. Cuando comenzamos a usarla, la llamamos llamada o invocación de función.
La función se puede declarar con o sin parámetros.
En Python tenemos la siguiente sintaxis para declarar e invocar funciones : 
        ->  # Declaring a function
            def function_name():
                codes

            # Calling a function
            function_name()

En Python, al igual que en otros lenguajes, podemos crear funciones tanto con parámetros como sin parámetros.
"""

#Ejemplo de funciones sin parámetros

def generate_full_name ():
    first_name = 'Rodrigo'
    last_name = 'Cabello'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)


generate_full_name () # calling a function

print("\n")

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)


add_two_numbers()


print("\n")
print("<----------------- FUNCIONES CON  PARÁMETROS ------------------->")
print("\n")


"""
En una función podemos pasar diferentes tipos de datos (número, cadena, booleano, lista, tupla, diccionario o conjunto) como parámetro.
Dentro del paso de parámetros, tenemos diferentes tipos : 
    
    -> Parámetro único: si nuestra función toma un parámetro, debemos llamar a nuestra función con un argumento.

            # Declaring a function
            def function_name(parameter):
                codes
                codes
            # Calling function
            print(function_name(argument))

    -> Dos parámetros: una función puede tener o no uno o más parámetros. Una función también puede tener dos o más parámetros. 
                       Si nuestra función acepta parámetros, debemos llamarla con argumentos.
                
    -> 
"""


#Ejemplo de un solo parámetro 
def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Rodrigo'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)

print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050


print("\n")

#Ejemplo de dos parámetros

def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name('Rodrigo','Cabello'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;

print('Age: ', calculate_age(2024, 2002))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to a string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))





print("\n")
print("<----------------- PASAR ARGUMENTOS CON CLAVE Y VALOR ------------------->")
print("\n")


"""
En Python, tenemos una cosa muy curiosa, si pasamos los argumentos con clave y valor, el orden de los argumentos no importa.
La sintaxis es :

    ->  # Declaring a function
        def function_name(para1, para2):
            codes

        # Calling function
        print(function_name(para1 = 'John', para2 = 'Doe')) # the order of arguments does not matter here

"""

def print_fullname( lastname,firstname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print(print_fullname(firstname = 'Rodrigo', lastname = 'Cabello'))

def add_two_numbers (num1, num2):
    total = num1 + num2
    print(total)
print(add_two_numbers(num2 = 3, num1 = 2)) # Order does not matter







print("\n")
print("<----------------- DEVOLUCIÓN DE VALORES EN FUNCIONES ------------------->")
print("\n")


"""
Las funciones también pueden devolver valores. Si una función no tiene una declaración de retorno, el valor de la función es Ninguno.
Reescribamos las funciones anteriores utilizando el retorno. A partir de ahora, obtenemos un valor de una función cuando la llamamos y la imprimimos.
"""

def generate_full_name ():
    first_name = 'Rodrigo'
    last_name = 'Cabello'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())
print("\n") 
def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())

print("\n") 


"""
Si no devolvemos un valor con una función, entonces nuestra función devuelve None de manera predeterminada. 
Para devolver un valor con una función, usamos la palabra clave return seguida de la variable que estamos devolviendo. 
Podemos devolver cualquier tipo de datos desde una función.
"""

#Cadenas de texto

def print_name(firstname):
    return firstname
print_name('Rodrigo') # Asabeneh

def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name
print_full_name(firstname='Rodrigo', lastname='Cabello')


#Numeros

def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;
print('Age: ', calculate_age(2024, 2002))

#Lista

def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))









print("\n")
print("<----------------- PARÁMETROS PREDETERMINADOS ------------------->")
print("\n")

"""
A veces, pasamos valores predeterminados a los parámetros cuando invocamos la función. 
Si no pasamos argumentos al llamar a la función, se utilizarán sus valores predeterminados.

La sintaxis para declararlo es : 

    ->  def function_name(param = value):
            codes

        # Calling function
        function_name()
        function_name(arg)
"""


def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Rodrigo'))

def generate_full_name (first_name = 'Peter', last_name = 'Cabello'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('Rodrigo','Cabello'))

def calculate_age (birth_year,current_year = 2021):
    age = current_year - birth_year
    return age;
print('Age: ', calculate_age(1821))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - average gravity on Earth's surface
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # gravity on the surface of the Moon









print("\n")
print("<----------------- ARGUMENTOS ARBITRARIOS ------------------->")
print("\n")


"""
Si no sabemos la cantidad de argumentos que pasamos a nuestra función, podemos crear una función que pueda tomar una cantidad arbitraria 
de argumentos agregando "*" antes del nombre del parámetro.
La sintaxis es la siguiente : 

    ->  # Declaring a function
        def function_name(*args):
            codes

        # Calling function
        function_name(param1, param2, param3,..)
"""


def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total


print(sum_all_nums(2, 3, 5)) # 10
print("\n")

def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Rodrigo','Javier','DavidP','DavidB','Félix'))


print("\n")
#You can pass functions around as parameters
def square_number (n):
    return n * n

def do_something(f, x):
    return f(x)

print(do_something(square_number, 3)) # 27