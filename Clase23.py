 #MANEJO DE VARIABLES

 #Muchas maneras de hacer lo siguiente:
# nombre = input("Ingrese su nombre")
# saludo1 = "Hola mucho gusto mi nombre es " + nombre
# saludo2 = "Hola mucho gusto mi nombre es %s " %nombre
# saludo3 = "Hola mucho gusto mi nombre es {} " .format(nombre)
# saludo4 = f"Hola mucho gusto mi nombre es {nombre} "

# print(saludo1)
# print(saludo2)
# print(saludo3)
# print(saludo4)
# print(f"Hola mucho gusto mi nombre es {nombre.capitalize()}")

 #REDONDEO DE NUMEROS DECIMALES
#1 - Clasico
numero_decimal = 49.23592865472
print("Numero decimal: %.3f" %numero_decimal) # --- % es el simbolo de formato, el 3 es la cantidad de decimales que quiero que se muestre, la f indica que el numero es flotante y despues hay que poner la variable o el elemento

#2 - Format()
numero_decimal2 = 124.234536
print(float(''))