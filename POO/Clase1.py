#Num = int(input("Ingrese un número"))
 #if Num > 0:
 #    print(f"{Num} es positivo")
 #elif Num < 0:
 #    print(f"{Num} es negativo")
 #else:
 #    print(f"{Num} es igual a cero")

lista_par = []
lista_impar = []
suma_par = 0
suma_impar = []
Num = 1

while Num != 0:
    Num = int(input("Ingrese un número"))
    print(" 0 para finalizar")
    if Num == 0:
        break
    if Num%2 == 0:
        lista_par.append(Num)
    else:
        lista_impar.append(Num)

print(f"Lista de pares {lista_par}")
print(f"Lista de impares {lista_impar}")

#suma_par = sum(lista_par)
#suma_impar = sum(lista_impar)
print(lista_par)
i = 1
for i in range(len(lista_par)):
    suma_par = suma_par + lista_par[i]

print(suma_par)
print(suma_impar)
