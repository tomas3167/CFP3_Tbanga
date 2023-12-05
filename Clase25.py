 # Ejercicio: Define una funcion llamada invertir_lista que tome una lista como parametro y devuelva la lista invertida


# def invertir_lista(lista):
#     return lista[::-1]
# resultado = invertir_lista([1,2,3,4,5,6])
# print(resultado)


# def pares_impares(lista):
#     pares=[]
#     impares=[]
#     for i in lista:
#         if i%2==0:
#             pares.append(i)
#         else:
#             impares.append(i)
#     return pares, impares
# numeros = [2,3,7,1,8,12,5]
# pares, impares = pares_impares(numeros)
# print(f"los numeros pares son: {pares}")
# print(f"los numeros impares son: {impares}")

 # --- Otra forma ---
def pares_impares(lista):
    pares=[i for i in lista if i % 2 == 0]
    impares=[i for i in lista if i % 2 != 0]
    return pares, impares
numeros = [2,3,7,1,8,12,5]
pares, impares = pares_impares(numeros)
print(f"los numeros pares son: {pares}")
print(f"los numeros impares son: {impares}")