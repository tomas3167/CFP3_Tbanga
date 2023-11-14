#MULTIVARIABLES
# nombre = "Daivis"
# edad = 20
# sexo = "Binario"

#Es lo mismo hacer esto:
# nombre, edad, sexo = "Daivis", 20, "Binario"

# print(nombre)
# print(edad)
# print(sexo)


# --- METODOS PARA CADENAS ---

 #COUNT: devuelve la cantidad de veces que se repite un elemento
# cadena = "Bienvenidos a Humberto primo, estudio junto a mi primo, que se llama Daivis, es un buen primo"
# print(cadena.count("i"))
# print(cadena.count("I"))
# print(cadena.count("primo"))

 #FIND: devuelve la posicion del elemento
# cadena = "Esta es la clase de programacion"
# print(cadena.find("a"))

 #RFIND: devuelve la posicion del ultimo elemento
# cadena_2 = "Esta es la clase de programacion"
# print(cadena_2.rfind("a"))

 #SPLIT: divide la cadena en subcadenas usando un separador especifico
# saludo = "Hola a todos como estan? Como estan?"
# print(saludo.split())

 #JOIN: es para poner un separador entre los elementos
# msg = "-"
# mensaje = "Hola a todos"
# print((msg).join(mensaje))

 #STRIP: devuelve la cadena borrando todos los caracteres delante y detras de la cadena especificados
# saludo_despedida = "------------HOLA-------------"
# print(saludo_despedida.strip("-"))

 #REPLACE: devuelve la cadena reemplazando los caracteres indicados (1ero se pone el elemento que se quiere reemplazar y 2do el otro elemento)
# mensaje = "En 30 minutos nos vamos"
# print(mensaje.replace("30 minutos", "10 segundos"))


# --- OTROS METODOS PARA LISTAS ---

 #EXTEND: para sumar una lista a otra (concatenar)
# cursos = ["Electricidad", "Gas", "Cerrajeria"]
# nuevos_cursos = ["Programacion", "3D", "Mecanica"]
# cursos.extend(nuevos_cursos)
# print(cursos)

 #INSERT: es como APPEND pero puedo elegir la posicion
# cursos = ["Electricidad", "Gas", "Cerrajeria"]
# cursos.insert(2,"Programacion")
# cursos.insert(4,58)
# print(cursos)

 #REVERSE: para dar vuelta una lista
# lista = [1,2,3,4]
# lista.reverse()
# print(lista)

 #SORT: para ordenar una lista de mayor a menor o al reves
# lista = [9,19,2,345,-9,1,0,290,400,2]
# print(lista)
#Ascendente
# lista.sort()
# print(lista)
#Descendente
# lista.sort(reverse=True)
# print(lista)

 #MIN y MAX: minimo y maximo
# lista = [9,19,2,345,-9,1,0,290,400,2]
# print(min(lista))
# print(max(lista))

 #DESEMPAQUETADO: para guardar en una variable cada division
numeros = (1,2,3,4,5,6,7)
uno = numeros[0]
dos = numeros[1]
tres = numeros[2]
cuatro = numeros[3]

print(uno)
print(dos)
print(tres)
print(cuatro)

uno, dos, tres, cuatro, *resto = numeros # --- *resto es el resto de numeros que no los guarde (5,6,7)
uno, dos, tres, cuatro, *_ = numeros # --- *_ omite el resto de elementos
