#Ejercicio: Escribir un programa que genere una lista de numeros pares del 0 al 10 (ambos inclusive), para esto debemos usar un ciclo FOR y el metodo APPEND. Finalmente imprimir la lista de numeros por pantalla. 

# lista_pares = []
# lista_impares = []
 # for i in range(0,11,1):
 #     if i%2 == 0:
 #         lista_pares.append(i)
 #     else:
 #         lista_impares.append(i)
 # print(f"pares: {lista_pares}")
 # print(f"impares: {lista_impares}")

#Ejercicio_2: Dada una lista numeros=[1,2,3,4,5] hacer un programa que recorra la lista y vaya eliminando los elementos de la lista uno a uno y los muestre por pantalla hasta que la lista quede vacía.

# lista_numeros = [1,2,3,4,5]

 # print(lista_numeros)
 # while lista_numeros != []:
 #     lista_numeros.pop(-1)
 #     print(lista_numeros)

# OTRA FORMA: DESCENDENTE
 # for i in range(len(lista_numeros)-1,-1,-1):
 #     numero_eliminado = lista_numeros.pop(i)
 #     print(f"Se eliminó el número {numero_eliminado}")
  #     ### print (f"Se eliminó el elemento {lista_numeros.pop(-1)}") -- Se puede hacer de esta forma tambien
 # print(f"La lista quedo vacía {lista_numeros}")

# OTRA FORMA: ASCENDENTE
 # for _ in range(len(lista_numeros)): -- (el guion bajo "_" signfica que se obvia el elemento)
 #     numero_eliminado = lista_numeros.pop(0)
 #     print(f"Se eliminó el número {numero_eliminado}")
  #     ### print (f"Se eliminó el elemento {lista_numeros.pop(-1)}") -- Se puede hacer de esta forma tambien
 # print(f"La lista quedo vacía {lista_numeros}")

#Ejercicio_3: Crear un programa que almacene dos listas: usuarios y contraseñas y solicite al ingresante los datos de login (usuario y contraseña) solo se admiten 3 intentos de inicio de sesión.

# usuarios = ["Bryan","Tomas","Ronal","Santiago","Roberto"]
# contraseñas = ["pepito","123","45","contraseña","pepito1"]
# intentos = 3

 # while intentos > 0:
 #     usuario_ingresado =usuario_ingresado = input("Ingrese la usuario").capitalize()
 #     contraseña_ingresada = (input("Ingrese la contraseña")).lower()
 #     if usuario_ingresado in usuarios  and contraseña_ingresada == contraseñas[usuarios.index(usuario_ingresado)]:
 #         print(f"Inicio de sesión correcto. Bienvenido {usuario_ingresado}")
 #         break
 #     else:
 #         print("Datos incorrectos, intente de nuevo")
 #         intentos = intentos - 1
 
 # if intentos == 0:
 #     print("Cuenta bloqueada, superó el límite de intentos")
