# Estructura WHILE (Mientras)
# while (condicion):
#     Instrucciones

# Ejemplo 1
#num = 5
 #while num > 0:
 #        print(f"{num}")
 #        num = num - 1
#print("Fin del bucle")

# Login usando WHILE y CONTADOR de intentos de sesion
#Para salir del bucle el usuario debe ingresar correctamente las credenciales o llegar al maximo de intentos posibles

# intentos = 0
 # while intentos < 3:
 #     usuario = input("Ingrese su usuario: ").upper()
 #     contraseña = input("Ingrese su contraseña: ").lower()
 
 #     if usuario == "MILAGROS" and contraseña == "pepito123":
 #         print (f"Acceso condedido {usuario}")
 #         break  # BREAK: sirve para romper la condicion y finalizar el bucle. Siempre se pone adentro de una estructura con una condicion, (ej: if, while, etc)
 #     else:
 #         print (f"Usuario o contraseña incorrectas, intente de nuevo. Intentos restantes:{2 - intentos}")
 #       # intentos = intentos + 1  ---  Es lo mismo que intentos = intentos + 1
 #         intentos += 1
 
 # if intentos >= 3:
#     print ("Superó el límite de intentos, su cuenta fue bloqueada")

# Estructura WHILE-ELSE
# while (condicion)
#     instrucciones
# else
#     instrucciones

# intento = 1
 # while intento <= 3:
 #     msg = input("Escribe SI: ").upper()
 #     if msg == "SI":
 #         print(f"Ok, lo conseguiste en el intento {intento}")
 #         break
 #     intento +=1
 # else:
#     print("Usaste todos tus intentos disponibles")

# Escribir un programa que le pregunte al usuario números hasta que ingrese el 0, cuando lo haga mostrar por pantalla la suma de todos los números ingresados

# suma = 0
 # num = 1
 # while num != 0:
 #     num = int(input ("Ingrese un número, 0 para terminar"))
 #     suma = suma + num
 # else:
#     print (f"La suma total es: {suma}")

# Realizar un programa que me devuelva la suma de los primeros 100 numeros enteros

# suma = 0
 # num = 0
 # while suma < 5050 or num < 100:
 #     num = num + 1
 #     suma = suma + num
 #     print (f"{num} -- {suma}")
 # else:
#     print (f"La suma es {suma}")

# BREAK: sirve para romper la condicion y finalizar el bucle. Siempre se pone adentro de una estructura con una condicion, (ej: if, while, etc)

# PASS: Se utiliza comunmente en bloques de codigo que aun no se han implementado o en funciones que aun no tienen contenido

# CONTINUE: Sirve para omitir una iteracion y continuar con la siguente, si se cumple una condicion determinada.