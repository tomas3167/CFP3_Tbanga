baja = []
media = []
alta = []
temperaturas=[]
for i in range(5):
    temperaturas = int(input("Ingrese la temperatura"))
for i in range(temperaturas):
    if temperaturas[i] < 10:
        baja.append(temperaturas[i])
    elif temperaturas[i] <= 25:
        media.append(temperaturas[i])
    else:
        alta.append(temperaturas[i])
print(baja)
print(media)
print(alta)