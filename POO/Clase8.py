 # 1- Escribir una funcion llamada "contar_vocales" que tome como argumento una cadena de texto y cuente el numero de veces que aparece cada vocal (a,e,i,o,u) en la cadena
# A = []
# E = []
# I = []
# O = []
# U = []
# def contar_vocales(cadena="Hola compañeros"):
#     for i in range(len(cadena)):
#         if cadena[i] == "a":
#             A.append(cadena[i])
#         if cadena[i] == "e":
#             E.append(cadena[i])
#         if cadena[i] == "i":
#             I.append(cadena[i])
#         if cadena[i] == "o":
#             O.append(cadena[i])
#         if cadena[i] == "u":
#             U.append(cadena[i])
#     return len(A), len(E), len(I), len(O), len(U)
# resultado = contar_vocales()
# print(resultado)
    #OTRA FORMA CON DICCIONARIO
# def contar_vocales(cadena):
#     vocales = {
#         "a": 0,
#         "e": 0,
#         "i": 0,
#         "o": 0,
#         "u": 0,
#     }
#     for letra in cadena:
#         if letra.lower() in vocales:
#             vocales[letra.lower()] += 1
#     return vocales
# cadena = input("Ingrese un texto: ")
# resultado = contar_vocales(cadena)
#  #print(resultado)
# ## --- En vez de hacer el print creamos un archivo de texto con el resultado.
# with open("resultado","w") as archivo: # Se puede poner w de WRITE o r de READ
#     for vocal, cantidad in resultado.items():
#         archivo.write(f"La vocal {vocal} aparece {cantidad} de veces \n")

 # 2- Escribir una funcion que acepte una cantidad variable de argumentos numericos y devuelva el valor maximo y minimo de todos los argumentos
# def numeros(*args):
#     return min(args), max(args)
# resultado = numeros(2,4,5,10)
# print(resultado)

          # PROGRAMACION ORIENTADA A OBJETOS
  # 1- Definicion de clase
#class Persona:
  # 2- Atributos: Caracteristica de una clase, puede ser de cualquier tipo, numero, cadena, lista, etc
 # __init__ : Es un metodo especial en Python que se llama automaticamente cuando se crea una clase, es utilizado para inicializar los atributos de una clase con valores especificos
 # self : Se refiere al propio objeto y se utiliza para acceder a sus atributos y metodos dentro de la clase. Es una convencion usar self como el primer parametro
# class Persona:
#     def __init__(self,nombre,edad):
#         self.nombre = nombre
#         self.edad = edad
  # 3- Metodo: Accion definida dentro de una clase que puede realizar alguna operacion especifica con los atributos del objeto
#    def saludar(self):
#        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años")
  # 4- Objeto: Una instancia de una clase, se crea utilizando la clase como plantilla y representa una entidad del mundo real. Cada objeto tiene sus propios atributos y puede ejecutar sus propios metodos
 #Crear objeto de la clase persona
# persona_1 = Persona("Tomas", 26)
# print("Atributos: ")
# print(persona_1.nombre)
# print(persona_1.edad)
# print("\n")
# print("Metodos: ")
# persona_1.saludar()

# Crear una clase llamada "Libro" que represente un libro. La clase debe tener los siguientes atributos: titulo, autor, paginas, editorial, fecha_publicacion. Y un metodo llamado "informacion" que imprima todos los datos del libro. Crear 2 objetos de la clase libro
class Libro:
    def __init__(self,titulo,autor,paginas,editorial,fecha_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.editorial = editorial
        self.fecha_publicacion = fecha_publicacion
    def informacion(self):
        print(f"El libro {self.titulo} del autor {self.autor} de la editorial {self.editorial} tiene {self.paginas} paginas y se publico en {self.fecha_publicacion} ")

libro_1 = Libro("A","Borges",200,"pepe","10/10/1990")
libro_2 = Libro("B","Tomas",150,"pepito","5/11/2008")
print(libro_1.titulo)
print(libro_1.autor)
libro_1.informacion()
libro_2.informacion()