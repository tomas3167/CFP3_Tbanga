 # Representar un objeto del mundo real en codigo python
# class Panaderia:
#     def __init__(self,producto,precio,cantidad,fecha_ven):
#         self.producto = producto
#         self.precio = precio
#         self.cantidad = cantidad
#         self.fecha_ven = fecha_ven
#     def descripcion(self):
#         print(f"{self.producto}: cuesta {self.precio} y su fecha de vencimiento es {self.fecha_ven} ")
#     def comprar(self):
#         print(f"Se compro {self.cantidad} de {self.producto} ")
   # __STR__: Es un metodo especial en Python que se utiliza para devolver una representacion de cadena legible para humanos. -- Es el print(producto_1).          Al utilizar __str__ podemos personalizar completamente la salida del objeto, mostrando solo la informacion relevante que queremos mostrar.
#     def __str__(self):
#         return f"{self.producto}: cuesta {self.precio} y su fecha de vencimiento es {self.fecha_ven} "
# producto_1 = Panaderia("Pan",1500,"1kg","12/10/2024")
# producto_2 = Panaderia("Medialunas",5500,"1 docena",False)
# producto_1.comprar()
# producto_1.descripcion()
# producto_2.comprar()
# producto_2.descripcion()
# print(producto_1)
# print(producto_2)

 # HERENCIA: Es un pilar de la POO que permite que una clase herede atributos y metodos de otra clase. En la herencia, una clase principal o superclase puede definir ciertos comportamientos y caracteristicas que son comunes en un grupo de clases relacionadas. La herencia promueve la reutilizacion de codigo y ayudar a crear una jerarquia de clases que refleja relaciones del mundo real. Se pueden sobreescribir un metodo, etc en la clase hija
# class Mascota(): # Clase principal
#     def comer(self):
#         print("La mascota esta comiendo")
#     def dormir(self):
#         print(f"{self.nombre} La mascota esta durmiendo")
# class Gato(Mascota): # Clase hija
#     def comer(self):
#         print("El gato esta comiendo")
#     def dormir(self):
#         print("El gato esta durmiendo")
# class Perro(Mascota):
#     def __init__(self,nombre):
#         self.nombre = nombre
# perro_1 = Perro("Emma")
# perro_1.comer()
# perro_1.dormir()
# cata = Gato()
# cata.comer
# cata.dormir

class Vehiculo():
    def __init__(self,marca,modelo,color,motor,asientos,velocidad_max):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.asientos = asientos
        self.velocidad_max = velocidad_max
        self.velocidad_actual = 0
    def acelerar(self,incremento):
        self.velocidad_actual += incremento
        if self.velocidad_actual > self.velocidad_max:
            self.velocidad_actual = self.velocidad_max
        print(f"La velocidad actual: {self.velocidad_actual}")
 # SUPER(): El metodo SUPER es una funcion incorporada en Python que se utiliza para llamar al metodo de la SuperClase. En lugar de tener que especificar todos los atributos nuevamente, lo reemplazamos con el uso de SUPER()
class Moto(Vehiculo):
    def __init__(self,marca,modelo,color,motor,asientos,rodado,manubrio):
        super().__init__(marca,modelo,color,motor,asientos,velocidad_max = 200,)
        self.rodado = rodado
        self.manubrio = manubrio
class Bicicleta(Vehiculo):
    def __init__(self,marca,modelo,color,motor,asientos):
        super().__init__(marca,modelo,color,motor,asientos,velocidad_max = 30)

moto_1 = Moto("Honda","CBR","Rojo",1000,2,12,"metal")
moto_1.acelerar(250)
bici_1 = Bicicleta("Venus","BMX","Amarilla",False,1)
bici_1.acelerar(15)