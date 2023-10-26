#tupla_numeros = (1,2,"tres",4,"cinco")
#print(tupla_numeros)
#lista_numeros = list(tupla_numeros)
#lista_numeros[2] = 3
#lista_numeros[4] = 5
#tupla_numeros = tuple(lista_numeros)
#print (tupla_numeros)

# Tambien se puede hacer asi:
 #tupla_numeros = ()
 #tupla_numeros = (1,2,3,4,5)
 #print (tupla_numeros)

# .upper Transforma todo a mayuscula
# .lower Transforma todo a minuscula
# .capitalize Solo transforma mayuscula la 1ra letra

 #usuario = input("Ingrese su usuario: ").upper()
 #contraseña = input("Ingrese su contraseña: ").lower()

 #if usuario == "MILAGROS" or contraseña == "pepito123":
 #    print("Acceso concedido")
 #else:
 #    print("Acceso denegado")

#edad = 24
 #if edad >= 36:
 #    print("Es un adulto")
 #elif edad == 24:
 #    print("La edad es 24")
 #elif edad == 26:
 #    print("La edad es 24_bis")
 #elif edad == 24:
 #    print("La edad es 24_bis_2")
 #elif edad == 24:
 #    print("La edad es 24_bis_3")
 #else:
 #    print("No sabemos la edad")
#print("Se termino el programa")

# Se solicita un programa que admita una nota y muestre un mensaje:
# menor a 4: reprobado
# menor a 6: aprobado
# menor a 8: sobresaliente
# menor a 9: excelente
# 10: genio

# nota = float(input("Ingrese una nota"))
# if nota <= 4:
#     print ("Reprobado")
# elif nota <= 4.5:
#     print ("Regular")
# elif nota <= 6.7:
#     print ("Aprobado")
# elif nota <= 8.9:
#     print ("Sobresaliente") 
# elif nota <= 9:
#     print ("Excelente")
# else:
#     print ("Genio")

# Un curso se divide en dos grupos A y B.
# Grupo A: [nombre anterior a la M y fan de marvel] o [nombre posterior a la N y fan de capcom]
# Grupo B: El resto

nombre = input("Ingrese su nombre")
preferencia = input("Ingrese su preferencia (Marvel o Capcom)").lower()

if (preferencia == "marvel" and nombre <= "M") or (preferencia == "capcom" and nombre > "N"):
    print (f"{nombre} esta en el grupo A")
else:
    print (f"{nombre} esta en el grupo B")
