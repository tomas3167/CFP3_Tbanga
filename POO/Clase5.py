 # 1- Crear una funcion que sume dos numeros
 # 2- a la funcion anterior modificarla para que los numeros los pueda introducir el usuario

# def suma(num1,num2):
#     num = num1 + num2
#     return num
# num1 = int(input("Ingrese un numero"))
# num2 = int(input("Ingrese un numero"))
# resultado = suma(num1,num2)
# print(f"El resultado entre {num1} y {num2} es {resultado}")

 # 3- Incorporar la logica para que solicite de manera indefinida la suma de dos numeros, hasta que una condicion corte el ciclo.

# num1 = 1
# num2 = 1
# def suma(num1,num2):
#     return num1+num2
# while num1 != 0 and num2 != 0:
#     num1 = int(input("Ingrese un numero"))
#     num2 = int(input("Ingrese un numero"))
#     if num1 == 0 or num2 == 0:
#         break
#     resultado = suma(num1,num2)
#     print(f"el resultado es {resultado}")

    ### OTRA FORMA
 
def suma(num1,num2):
    resultado = num1 + num2
    return resultado

def suma_bucle():
    while True:
        num1 = int(input("Ingrese el primer numero (0 para salir) "))
        num2 = int(input("Ingrese el segundo numero "))
        if num1 == 0 or num2 == 0:
            print("Usted esta saliendo del programa.....")
            break
        resultado_suma = suma(num1,num2)
        print(f"La suma es {resultado_suma}")
suma_bucle()