# --- FUNCIONES ---

 # 1er paso, def: definir una funcion
# def saludar():
#     print("Hola mundo")
 # 2do paso, hacer el print de la funcion, basta con escribir el nombre y listo
# saludar()

# def saludar_nombre(nombre): # -- lo que va entre parentesis se llama parametro
#     print(f"Hola {nombre}")
# saludar_nombre("Ronald")
# saludar_nombre(input("Ingrese un nombre")) # -- 2da opcion

 # Alcance de una variable -- la variable numero solo esta definida dentro de la funcion local
# def prueba():
#     numero = 10
#     print(numero)
# prueba()
# print(numero) -- tira error

# numero = 10
# def prueba():
#     numero = 15
#     print(numero)
# prueba()
# print(numero)

 # Estructura de la funcion
# def nombre():
#     sentencias
#     return[expresion]

# def saludo_nombre(nombre):
#     saludo = print(f"Hola {nombre}")
#     return saludo
# saludar = saludo_nombre("Diego")
# print(saludar)

# def saludo_nombre(nombre):
#     saludo = print(f"Hola {nombre}")
# saludar = saludo_nombre("Diego")
# print(saludar)


# def num_mayor(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
#      # return max(a,b,c) # -- es otra forma de hacerlo
    
# resultado = num_mayor(8,12,3)
# print(resultado)

# print(num_mayor(8,12,3))

# def area_circulo(radio,pi=3.14):
#     return pi *(radio ** 2) # -- formula: (pi x radio al cuadrado)
# resultado = area_circulo(10)
# print(resultado)
 # ----- Otra forma:
# def area_circulo(pi=3.1417,radio=10): # -- asigno valores por default
#     return pi *(radio ** 2) # -- formula: (pi x radio al cuadrado)
# resultado = area_circulo()
# print(resultado)

 # Ejercicio_1: Escribir una funcion que calcule la suma de 2 numeros, si no se pasa el 2do numero, su valor por default sera 10.
# def suma(a=0,b=10):
#     return a + b
# resultado = suma(5)
# print(resultado)
 # --- otra manera:
# resultado = suma(int(input("Ingrese un numero")),(int(input("Ingrese otro numero"))))
# print(resultado)

 # Ejercicio_2: Escribir una funcion que calcule el promedio de una lista de numeros, si no se proporcina una lista, el valor por default sera una lista vacia.
def numeros(nums=[]):
    if len(nums) == 0:
        return "La lista esta vacia"
    else:
        return sum(nums)/len(nums)
resultado = numeros([2,4,100,87])
print(resultado)

# El return funciona como un BREAK, por lo tanto, todo lo que se escribe despues del return no lo toma