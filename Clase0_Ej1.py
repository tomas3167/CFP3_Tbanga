# Declarar 3 variables con valores ingresados por el usuario (numeros) y mostrar en un PRINT el promedio de los números

# int sirve para que el valor ingresado sea numérico, si no pongo eso va a ser texto o cadena
num1 = int(input ("Ingrese el primer número"))
num2 = int(input ("Ingrese el segundo número"))
num3 = int(input ("Ingrese el tercer número"))

promedio = (num1 + num2 + num3) / 3

print (f"{promedio}")

# Comandos: con alt + ctrl y la flecha para abajo o arriba hace que cuando escribo algo se escribe en todos los lados
# Comandos: con shift + alt y alguna flecha copio y pego la línea
# Comandos: Alt + z para que el texto baje
# Comandos: Ctrl y + o Ctrl y - para hacer zoom

nombre = "tomas"
existe = False
edad = 19
numDecimal = 3.5

print (type(nombre))
print (type(existe))
print (type(edad))
print (type(numDecimal))
# TYPE sirve para ver el tipo de dato de una variable y la estructura es: print (type(nombre de la variable))

# TODAS las clases
# str = cadena
# bool = boleano, True o False siempre con mayúsculas
# int = número entero
# float = númedo decimal

# false es igual a 0
# true es igual a 1

# != es distinto

# BREAK: sirve para romper la condicion y finalizar el bucle. Siempre se pone adentro de una estructura con una condicion, (ej: if, while, etc)

# PASS: Se utiliza comunmente en bloques de codigo que aun no se han implementado o en funciones que aun no tienen contenido

# CONTINUE: Sirve para omitir una iteracion y continuar con la siguente, si se cumple una condicion determinada.