# Ctrl + } para comentar todo
 # PASO POR VALOR
# num = 10
# def doblar_numero(num):
#     num *= 2
#     return num
# resultado = doblar_numero(10)
# print(resultado) #20
# print(num) #10
 # Aca la variable no se reemplaza al pasar por la funcion

 # PASO POR REFERENCIA
# def doblar_lista(lista):
#     for i in range(len(lista)):
#         lista[i] *= 2
#     return lista
# lista = [10,20,30]
# copia_lista = lista[:]
# resultado = doblar_lista(copia_lista)
# print(resultado)
# print(lista)
 # La lista, a diferencia de las variables, se reemplazan los datos cuando pasan por una funcion, por eso hacemos una copia de la lista original

# *ARGS: Son parametros especiales que permiten pasar a la funcion multiples datos en forma de tupla
# def suma_numeros(num1,num2,num3,num4):
#     return num1 + num2 + num3 + num4
# resultado = suma_numeros(2,6,9,4)
# print(resultado)
#  # Para no poner cada numero, usamos el args, no es necesario que se llame args, solo tiene que tener el * adelante
# def suma_args(*args):
#     resultado = 0
#     for i in args:
#         resultado += i    # --- (resultado += i) es lo mismo que (resultado = resultado + i)
#     return resultado
# resultado = suma_args(2,6,9,4,5,20,40,2,5,13,7,52)
# print(resultado)

#Crear una funcion que calcule el perimetro
# def perimetro(*numeros):
#     resultado = 0
#     for i in numeros:
#         resultado += i
#     return resultado
# resultado_perim = perimetro(10,15,20,30)
# print(resultado_perim)

#Crear una funcion que acepte como argumento un numero indefinido de STRING y devuelva una cadena que contenga todos los argumentos concatenados en una sola cadena, separada por un separador opcional, si no se proporciona un separador, la funcion debe utilizar un espacio en blanco como separador
def strings(*args,separador=' - '):
    return separador.join(args)
resultado = strings("hola","s","d")
print(resultado)
 # el join es para concatenar algo despues de cada dato