palabras = ["estrella","alien","milanesa","viaje"]
lista = []

for i in range(len(palabras)):
    
    if palabras[i][0] > palabras[0]:
        lista.append(palabras[i])
    else:
        lista.insert(0,palabras[i])
print(lista)
