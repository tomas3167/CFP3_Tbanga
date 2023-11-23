palabra  = input("Ingrese una palabra")
palabra_2 = ("")
for i in range(len(palabra)-1,-1,-1):
    palabra_2 = palabra_2 + palabra[i]

print(palabra == palabra_2)

