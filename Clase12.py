# Listas: Se describe como una lista de items separados por coma "," y contenido entre corchete "[]". Es una lista heterogenea es decir puede contener: números, variables, string o incluso otras listas. Las listas son mutables.

#nombre = "Tomás"
#datos = [1, -4, 124.2, "Marvel", "Nuñez", True, nombre]
#print(datos)
#print (type(datos))

#lenguajes = ["Python", "Java", "C++", "JavaScript", 3, -4, [1,2,3]]
#print(lenguajes)
#print(lenguajes[1])
#print(lenguajes[6][1]) # Accediendo al subíndice de la lista
#print(lenguajes[-1][1]) # -1 siempre es el último elemento

#pares = [2,4,6,8]
#impares = [1,3,5,7,9]
#print(pares + impares)

# A diferencia de los STRING, las listas son MUTABLES
 #juegos = ["Lol", "Fifa", "Valorant"]
 #print(juegos)
 #print(juegos[0])
 #juegos[0] = "Mario Bross"
 #print(juegos)

# Asignacion por SLICING
 #numeros = [1,3,4,"cuatro","cinco","seis"]
 #print(numeros)
 #numeros[3:6:1] = [4,5,6] # El último elemento no esta incluido por eso hay que agregarle uno mas
 #print(numeros)

# letras = ["a","b","c","D","E","F"]
# print(letras)
# letras[0:3:1] = ["A","B","C"]
# print(letras)

# BORRAR por SLICING
 #letras = ["a","b","c","d","e","f"]
 #print(letras)
 #letras[0:3:1] = []
 #print(letras)

# Funcion APPEND -->> para agregar un elemento al final de una lista
 #juegos = ["Mario Bross","COD","NBA2K"]
 #print(juegos)
 #juegos.append("Battlefield")
 #print(juegos)

# Funcion POP -->> para eliminar un elemento
 #juegos = ["Mario Bross","COD","NBA2K"]
 #print(juegos)
 #juegos.pop() #Si no pongo nada por defecto elimina el último elemento
 #print(juegos)

# Funcion INDEX -->> para buscar un elemento que le indiquemos y nos devuelve en que posicion se      encuentra
 #numeros = [1,6,-3,22,-5,6,19,-7,9]
 #print (numeros.index(22))

# Ejercicio listas
lista1 = [1,12,123]
lista2 = ["Bye","Ciao","Agur","Adieu"]
# 1
lista1.append (1234)
lista1.append ("Hola")
# 2
# lista2.append ("Adios")
# lista2.append (1234)
lista2[4:] = ["Adios",1234] #Se puede hacer de las 2 formas
print (f"Lista 1 actualizada {lista1}" )
print (f"Lista 2 actualizada {lista2}")
# 3
lista3 = lista1
lista3.pop(-1)
print (f"lista 3 {lista3}")
# 4
lista4 = lista2
lista4.pop(0)
lista4.pop(-1)
print (f"lista 4 {lista4}")
# 5
lista5 = lista4 + lista3
print(f"lista 5 {lista5}")