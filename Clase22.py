# --- METODOS PARA SET ---

 #COPY: copia un set
# set_1 = {1,2,3,4}
# set_2 = set_1.copy()
# print(set_2)

 #ISDISJOINT: para ver si un set es distinto de otro set, (basta con que haya un item en comun)
# set1 = {2,3,4}
# set2 = {2,5,6}
# print(set1.isdisjoint(set2))

 #ISSUBSET: para ver si todos los items de un set esta en otro set
# set1 = {6,7}
# set2 = {5,6,7,8}
# print(set1.issubset(set2))

 #ISSUPERSET: igual que el anterior pero comprueba si los elementos del 2do set estan en el 1ero
# set1 = {6,7}
# set2 = {5,6,7,8}
# print(set1.issuperset(set2))

 #UNION: une un set con otro, (si un item se repite no se suma)
# set1 = {1,2,3,4}
# set2 = {5,6,7,8}
# print(set1.union(set2))

 #DIFFERENCE: devuelve los items no comunes del set 1 respecto al 2do set
# set1 = {1,2,3,4}
# set2 = {3,4,5,6,7}
# print(set1.difference(set2))

 #DIFFERENCE_UPDATE: igual que el DIFFERENCE pero actualiza el 1er set con los items no comunes
# set1 = {1,2,3,4}
# set2 = {3,4,5,6,7}
# set1.difference_update(set2)
# print(set1)

 #INTERSECTION: devuelve los items comunes del set 1 respecto al 2do set
# set1 = {1,2,3,4}
# set2 = {3,4,5,6,7}
# print(set1.intersection(set2))

 #INTERSECTION_UPDATE: lo mismo que el anterior pero actualiza el set con los items
# set1 = {1,2,3,4}
# set2 = {3,4,5,6,7}
# (set1.intersection_update(set2))
# print(set1)

#EJERCICIO: Crea un conjunto (set) "numeros" con elementos de tipo entero. Luego recorrerlo con un ciclo FOR para imprimir cada elemento elevado al cuadrado. Guardar los pares e impares en listas.

import random
numeros = set(random.randint(1,30) for _ in range(10)) 
pares = []
impares = []

print(numeros)

for i in numeros:
    print(i**2)
    if i%2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print(pares)
print(impares)