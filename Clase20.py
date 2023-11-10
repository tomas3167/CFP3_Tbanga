# diccionario = {
#     "nombre": "Tomas",
#     "apellido": "Banga",
#     "edad": 19,
#     "correo": "tomasbanga12@gmail.com"
# }
# print(diccionario)

 #Mutabilidad del diccionario:
# diccionario["apellido"] = "Banga2"
# print(diccionario)

 #En los diccionarios no funciona el ADD pero se puede agregar elementos creando una nueva clave asi:
# diccionario["direccion"] = "Carlos Calvo 2079"
# print(diccionario)

 #UPDATE: para agregar muchos elementos a la vez:
# diccionario.update({"telefono": 1234, "Localidad": "CABA"})
# print(diccionario)

 #LEN: para ver la cantidad de items, es decir, la cantidad de pares "clave-valor" que hay en el diccionario:
# print(len(diccionario))

 #Para agregar mas de un valor en una clave a traves de una lista:
# diccionario = {
#     "nombre": "Tomas",
#     "apellido": "Banga",
#     "edad": 19,
#     "correo": "tomasbanga12@gmail.com",
#     "hobbies": ["Futbol", "Tennis", "Programar"]
# }
# print(len(diccionario["hobbies"][0]))
# print(type(diccionario["hobbies"][0]))
# print(diccionario["hobbies"][0])

 #DEL: elimina una clave de mi diccionario
# del diccionario["edad"]
# print(diccionario)

 #IN: para ver si un elemento esta o no en el diccionario
# print("nombre" in diccionario)
# print("nombres" in diccionario)
# print("nombres" not in diccionario)

 #CLEAR: para vaciar el diccionario
# diccionario.clear()
# print(diccionario)
 #O tambien de la siguiente forma:
# diccionario={}

 #POP: para eliminar un elemento especifico de mi diccionario
# diccionario.pop("apellido")
# item_eliminado = diccionario.pop("apellido") --- Tambien se puede hacer asi
# print(item_eliminado)
# print(diccionario)

#Ejercicio SET:

# grupo = {"Miguel", "Blanca", "Mario", "Andrés"}
# print(grupo)
# grupo.update(["Ana", "Ramón", "Marta", "Eric", "David"])
# print(grupo)
 # 1ra opcion -- Para eliminar las 3 personas se puede usar discard:
# grupo.discard("Mario")
# grupo.discard("Miguel")
# grupo.discard("Esteban")
 # 2da opcion -- Para eliminar las 3 personas a la vez se usa for:
# for nombre in ["Mario","Miguel", "Esteban"]:
#     grupo.discard(nombre)
# print(grupo)

#Ejercicio DICCIONARIO:
 # animales = {"elefante": ""}
 # animales.update({"perro": "Bobby", "tigre": "Peepe", "mono": "homero"})
 # print(animales)
 # animales["elefante"] = "Trompis"
 # animales["delfin"] = "Manolo"
 # print(animales)


# diccionario = {
#     "nombre": "Tomas",
#     "apellido": "Banga",
#     "edad": 19,
#     "correo": "tomasbanga12@gmail.com",
#     "hobbies": ["Futbol", "Tennis", "Programar"]
# }

#Recorrer las claves
 # print("--Claves:")
 # for clave in diccionario.keys():
 #     print(clave)
#Recorrer los valores
 # print("--Valores:")
 # for valor in diccionario.values():
 #     print(valor)
#Recorrer los items (claves-valores)
 # print("--Items:")
 # for items in diccionario.items():
 #     print(items)

#COMPREHENSION: es para escribir menos
# Hacer una lista con los numeros pares del 1 al 10
# Solucion 1:
 # lista_1 = [i for i in range(11) if i % 2 == 0]
 # print(lista_1)

# Solucion 2:
 # lista_2 = [i for i in range(0,11,2)]
 # print(lista_2)

# El usuario ingresa los valores
# Opcion 1:
 # mascota = {}
 # mascota ["nombre"] = input("Ingrese el nombre de su mascota")
 # mascota ["color"] = input("Ingrese el color de su mascota")
 # mascota ["raza"] = input("Ingrese la raza de su mascota")
 # mascota ["edad"] = int(input("Ingrese la edad de su mascota"))
 # print(mascota)

# Opcion 2:
club = {
    "nombre": "",
    "barrio": "",
    "colores": "",
    "cantidad_hinchas": 0,
    "estadio": ""
}
# for clave in club:
#     valor = input(f"Ingrese {clave} del club")

#     if clave == "cantidad_hinchas":
#         club[clave] = int(valor)
#     else:
#         club[clave] = valor

 #Otra forma de hacerlo:
for clave in club:
    if clave == "cantidad_hinchas":
        club[clave] = int(input(f"Ingrese {clave} del club"))
    else:
        club[clave] = input(f"Ingrese {clave} del club")

print("Los datos del club son los siguientes: ")
print(club)