num1 = 7
num2 = 5

#suma = num1 + num2
#resta = num1 - num2
#multi = num1 * num2
#divi = num1 / num2
#potencia = num1 ** num2
#divi_entera = num1 // num2
#divi_resto = num1 % num2

#print (f"El resultado de las operaciones de los números {num1} y {num2}: suma: {suma}, resta: {resta}      potencia: {potencia}")
#Comando: Alt + z para que el texto baje

# reglas de PROCEDENCIA para las operaciones
# 1ero: parentesis
# 2do : potencia y raices
# 3ero: multiplicacion y division
# 4to : suma y resta

#print("Esto es una cadena\tcon tabulación")
#print("Esto es una cadena\ncon salto de línea")
# La \ se hace con Alt Gr + la tecla de ?
#print("""Con las 3 comillas se puede hacer esto
#1- suma
#2- resta
#3- multiplicación
#4- división
#  """)


# Indexacion de las cadenas(str)
#animal = "Perro"
#print(animal)
#print(animal[0])
#print(animal[4])
#print(animal[2])

# Esto es para que se muestre el caracter que esta en la posicion indicada, como en los arreglos


# len() hace que muestre la cantidad de caracteres que tiene

#print (len(f"{animal}"))
#print (len(animal))


# Slicing [inicio : final : pasos] como en el para
#fruta = "Durasno"
#print (fruta[4])
#fruta[4] = "z"
#print (fruta)

# Esto no se puede hacer porque las cadenas son inmutables
# para eso usamos el slicing
#fruta = fruta[0:4] + "z" + fruta[5:]
# Si no ponemos nada por defecto los pasos estan en 1 y el final es hasta el último caracter
#print(fruta)


# Dadas cuatro variables con diferentes textos (de forma individual), genera una nueva variable con el siguiente contenido:

#cadena_1 = "moderno"
#cadena_2 = "Python"
#cadena_3 = "es un lenguaje"
#cadena_4 = "de programación"
#cadena_5 = cadena_2 + " " + cadena_3 + " " + cadena_4 + " " + cadena_1
#print (cadena_5)

# Ejercicio: dar vuelta una cadena con slicing
frase = "Hola Roberto, cómo estas?"
print (len(frase)) # para saber la cantidad de caracteres
print(frase[25:0:-1])
print(frase[25:-26:-1])