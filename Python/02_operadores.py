#LECCIÓN 3 : LOS OPERADORES EN PYTHON



"""
En esta sección vamos a ver los diferentes operadores básicos de la programación que tenemos 
a nuestro alcance en Python, cabe recalcar que no muestro los operadores de asignación :
    -> =
    -> +=
    -> -=
    -> *=
    -> /=
    -> ...
"""





#<----------- OPERADORES ARITMÉTICOS --------------->
#Son todos aquellos operadores que nos permiten realizar operaciones con valores numéricos



"""
El intérprete funciona como una simple calculadora: puedes introducir una expresión en él y este escribirá los valores. 
La sintaxis es sencilla: los operadores +, -, * y / se pueden usar para realizar operaciones aritméticas;
los paréntesis (()) pueden ser usados para agrupar. Por ejemplo:
"""
#Variables enteras
numero1 = 2
numero2 = 5

#Suma
suma = numero1+numero2
print("La suma es : ",suma)
#Resta
resta = numero1-numero2
print("La resta es : ",resta)
#Multiplicación
multiplicacion = numero2*numero1
print("La multiplicacion es : ",multiplicacion)
#División
division = numero1/numero2
print("La division es : ",division)

#Paréntersis para declarar el orden
parentesis = (numero1 +numero2 ) * 3 + (2*numero1)
print("La operación da: ",parentesis)


"""
Esos son algunos ejemplos de como utilizar los operadores ariméticos básicos en python.
Nada nuevo que no estéis ya acostumbrados de Java.

Los números enteros (ej. 2, 4, 20) tienen tipo int, los que tienen una parte fraccionaria (por ejemplo 5.0, 1.6) tiene el tipo float. 
Vamos a ver más acerca de los tipos numéricos más adelante en el tutorial.
"""





#La división

"""
La división (/) siempre retorna un número decimal de punto flotante. 
Para hacer floor (redondeo) division y obtener un número entero como resultado puede usarse el operador "//".
para calcular el resto puedes usar % (módulo):
"""
numero1 // numero2  # floor division descarta la parte fraccionaria
numero1 % numero2  # Resto de dividir numero1 entre numero2





"""
Para la multiplicación, Python añade el operador "**" para calcular potencias de manera sencilla
"""
elevar_cuadrado = numero1 ** 2
elevar_cubo = numero2 ** 3





"""
Ya veis que el primer operando correspoende al número que quieres elevar.
Y el segundo corresponde a la potencia a la que lo quieres elevar.
Es una similitud a la función Math.pow que podemos encontrar en Java, C++ u otros lenguajes de programación, pero de manera simplificada y directa.
"""
#n
"""
Al igual que en Java, si intentamos utilizar una variable declarada pero no inicializada con ningún valor, dará un fallo
El error que marca será : "ID_Variable is not defined".
"""
#print(n)





#<-- Operadores Aritméticos para cadenas de texto -->
"""
Python puede manipular texto (representado por el tipo str, conocido como «cadenas de caracteres») al igual que números.
Esto incluye caracteres «!», palabras «conejo», nombres «París», oraciones «¡Te tengo a la vista!»,:) etc. «Yay! ». 
Se pueden encerrar en comillas simples ('...') o comillas dobles ("...") con el mismo resultado.
"""
string_uno = "HOLA"
string_dos = 'HOLA'
#Realmente el valor de ambos es el mismo, independientemente de las comillas





"""
Si queremos usar las comillas en un texto, ya sean las simples '' o las dobles "", tenemos que utilizar el carácter \ 
"""
cita = "\nJavier me dijo : \"No entiendo hilos\""
print("\n",cita + "\n")






"""
Que más podemos hacer con los operadores y el texto, pues como en cualquier lenguaje,
podemos concatenar textos en un print utilizando el operador "+"
"""
print("Hola " + "DAM2\n");





"""
Sin embargo, no podemos utilizar el resto de operadores entre cadenas de texto,no podemos hacer : 
    -> CADENA 1 - CADENA2
    -> CADENA 1 / CADENA2
    -> CADENA 1 * CADENA2 
    -> ...

Sin embargo, si podemos hacer alguna cosa muy curiosa, por ejemplo, podemos multiplicar una cadena por un número entero.
"""
print("Hola " * 5 + "\n")
print("<"+ ("-")*10 + " EJEMPLO DE USO " + ("-")*10 + ">\n")





"""
Ya véis que la funcion que tiene es imprimir tantas veces como el factor de multiplicación la cadena de texto.

Luego hay otras cosas que no podemos hacer directamente a pesar de que en otros lenguajes si, 
como puede ser concatenar texto con otros tipos de manera directa
"""
#print("Hola " + 5) # El código falla porque no convierte un int a str
print("Hola " + str(5) + "\n") # Tenemos que forzar la conversion de tipo a str para que funcione
















#<----------- OPERADORES COMPARATIVOS --------------->
#Operadores que utilizamos para una condición.


"""
Cuales son este tipo de operadores, pues los básicos que utilizamos en cualquier lógica de programación
para hacer comparaciones, es decir : 
    -> > Mayor que
    -> < Menor que
    -> >= Mayor o igual que
    -> <= Menor o igual que
    -> == Igual que
    -> != Distinto que 

Este tipo de operadores nos devuelve un valor de tipo bool o boolean, es decir, o True o False.
"""
#Ejemplo de uso de los operadores comparativos
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4, "\n")




"""
También podemos utilizarlo para comparar cadenas de texto, como por ejemplo :
"""
print("Hola" > "Adios")
print("Hola" < "Adios")
print("Hola" >= "Adios")
print("Hola" <= "Adios")
print("Hola" == "Adios")
print("Hola" != "Adios","\n")





"""
Pero, ¿en que se basa esta comparación?
Pues si os fijáis bien y hacemos varias pruebas, llegamos a la conclusión de que no esta comparando longitudes de strings, 
sino que compara ambos strings siguiendo un orden alfabético por ASCII.
"""
print("Hola" > "Adios") # True, la "H" viene después que la "A"
print("Hola" > "Reloj") # False, la "H" viene antes que la "R"
print("Hola" == "Hole" , "\n") # False, si dos letras tienen el mismo orden alfabético, continúa con las siguientes




















#<------- OPERADORES LÓGICOS 
#Operadores que utilizamos para concatenar operadores comparativos y llegar a condiciones más complejas.

"""
Al igual que en cualquier otro lenguaje de programación, podemos concatenarlos para 
conseguir comparaciones más complejas. Y como hacemos esto, con los operadores lógicos.
    -> Operador "and"
    -> Operador "or"
    -> Operador "not
"""
# Condición 1 y Condición 2
print(3 > 4 and 4 == 4)
# Condición 1 o Condición 2
print(3 > 4 or 4 == 4)
# Distinto que  Condición
print(not(3>4))

"""
Si venimos de otros lenguajes de programación, estamos acostumbrados a utilizar estos operadores de la manera :
    -> AND - &&
    -> OR - ||
    -> NOT - !

Sin embargo, en Python los escribimos directamente, pero la funcionalidad es la misma, concatenar comparaciones.
"""
