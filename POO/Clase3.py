# FUNCIONES:
#def saludar():
#    print("Hola a todos")
#saludar()

#def saludar_nombre(nombre): #Parametro
#    print(f"Hola {nombre} como estas?")

#saludar_nombre("Roberto") #Argumento

#Crear una funcion que imprima por pantalla el nombre, apellido y edad del alumno
#def alumno(nombre,apellido,edad):
#    print(f"El alumno se llama {nombre} {apellido} y tiene {edad}")
#alumno("Jose","Gomez","22")

# SCOPE DE VARIABLES:
#edad = 20
#def var_local():
#    edad = 18
#    print(edad)
#var_local()
#print(edad)

# RETURN:
#def saludo_nombres(nombre1,nombre2):
#    saludando = (f"Somos los alumnos {nombre1} y {nombre2}")
#    return saludando
#resultado = saludo_nombres("Milagros","Jessica")
#print(resultado)

#def numero():
#    return 6,True,"Pepito",2.4
#    print("La funcion se ejecuto")
#resultado = numero()
#print(resultado)

#def numero():
#    return 6
#resultado = numero() + 10
#print(resultado)
#print(type(numero()))

#Crear una funcion que me duvuelva el mayor de 3 numeros dados sin usar max
#def numeros(num1,num2,num3):
#    mayor = (num1)
#    if mayor < num2:
#        return num2
#    elif mayor < num3:
#        return num3
#    else:
#        return num1
#print(numeros(2,5,3))
# # Tambien se puede hacer asi:
#def num_max(num1,num2,num3):
#    return max(num1,num2,num3)
#print(num_max(10,15,27))
#valor_max = num_max(10,15,27)
#print(valor_max)

#Crear una funcion que calcule el area de un circulo
# PI por radio al cuadrado -- PI * (Radio**2)
#Parametros por DEFAULT
#def area_circulo(radio,pi=3.14):
#    return pi * (radio**2)
#resultado_area = area_circulo(11)
#print(resultado_area)

#Crear una funcion que sume dos numeros, si no se proporciona el segundo numero, el valor por default es 20
#def nums(num1,num2=20):
#    return num1 + num2
#resultado = nums(6)
#print(resultado)

#Crear una funcion que calcule el promedio de una lista de numeros. Si no se proporciona una lista, el valor por defecto sera una lista vacia. Se usa SUM
def promedio(lista=[]):
    if len(lista) == 0:
        return("La lista esta vacia")
    else:
        return sum(lista) / len(lista)
resultado = promedio(lista=[2,5,7,2,9,1])
print(resultado)
resultado2 = promedio()
print(resultado2)