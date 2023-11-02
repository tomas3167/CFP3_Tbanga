#EJ_1 Escribir un programa que almacene los meses del año en una lista y luego mostrar por pantalla el resultado.
 # meses= ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
 # print(meses)

#EJ_2 Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
# palabra = input("Ingrese una palabra")
 # contador = 0
 # while contador < 10:
 #     print(palabra)
 #     contador = contador + 1
# print(palabra * 10) -- es otra forma

#EJ_3 Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
 # numero = int(input("Ingrese un número"))
 # if numero%2 == 0:
 #     print(f"{numero} es par")
 # else:
 #     print(f"{numero} es impar")

#EJ_4 Para pagar un determinado impuesto se debe ser mayor de 18 años y tener un ingreso mensual igual o mayor a $200.000. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario debe pagar el impuesto o no.
 # edad = int(input("Ingrese su edad"))
 # ingresos = int(input("Ingrese sus ingresos mensuales"))
 # if edad > 18 and ingresos >= 200000:
 #     print("Debe pagar el impuesto")
 # else:
 #     print("No debe pagar el impuesto")

#EJ_5 Escribir un programa para una empresa de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $500 y si es mayor de 18 años, $1000.
 # edad = int(input("Ingrese su edad"))
 # if edad < 4:
 #     print("Puede entrar gratis")
 # elif edad <= 18:
 #     print("Debe pagar $500")
 # else:
 #     print("Debe pagar $1000")

#EJ_6 Escribir un programa que solicite una contraseña y esta se deba volver a confirmar, el programa terminara cuando ambas contrasenas coincidan.
 # contraseña="1"
 # contraseña2="2"
 # while contraseña != contraseña2:
 #     contraseña = input("Ingrese la contraseña")
 #     contraseña2 = input("Ingrese devuelta la contraseña")
 # print("Contraseña correcta")

#FOR for (i) in (variable)
 # meses= ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
 # for i in meses:
 #     print(f"Soy un mes del año y mí nombre es {i}")

# lista =[0,1,2,3,4,5,6,7,8,9,10]
 # for num in lista:
 #     print(f"soy un elemento de la lista y valgo {num}")
 #     num *= 5
 #     print(f"soy el mismo elemento, pero ahora valgo {num}")
 #     print("")

# nombre = "Tomas"
 # for i in nombre:
 #     print (i)

#RANGE es como el for en pseint -- "para (valor inicial = i) hasta (valor final) en (pasos)"
# Mostrar los numeros pares de 1 al 20
 # for i in range(0,21,1):
 #     if i%2 == 0:
 #         print(f"par {i}")
 #     else:
 #         print(f"impar {i}")