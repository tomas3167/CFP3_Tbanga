  # HERENCIA MULTIPLE: Una clase puede heredar de muchas clases padres
class ClaseA:
    def metodo_a(self):
        return "Metodo de ClaseA"
class ClaseB:
    def metodo_b(self):
        return "Metodo de ClaseB"

class ClaseDerivada(ClaseA, ClaseB):
    def metodo_derivada(self):
        return "Metodo de ClaseDerivada"

objetoDeri = ClaseDerivada()

 # Llamar a los metodos de las clases padres
# print(objetoDeri.metodo_a()) # -- metodo de la clase a
# print(objetoDeri.metodo_b()) # -- metodo de la clase b
# print(objetoDeri.metodo_derivada()) # -- metodo de la clase derivada

 # Mediante el uso de herencia multiple representar distintos tipos de vehiculos, para combinar las caracteristicas de vehiculos
class Vehiculo():
    def __init__(self,marca,modelo,color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
    def metodo_mostrar(self):
        return f"Marca:{self.marca}, Modelo:{self.modelo}, Color:{self.color}"

class Auto(Vehiculo):
    def __init__(self,marca,modelo,color,motor,puertas):
        super().__init__(marca,modelo,color)
        self.motor = motor
        self.puertas = puertas
    def metodo_mostrar(self):
        return f"{super().metodo_mostrar()}, Motor:{self.motor}, Puertas:{self.puertas}"
    def conducir(self):
        return "Conduciendo el auto"

class Avion(Auto,Vehiculo):
    def __init__(self, marca, modelo, color, motor, capacidad,cant_motor, alas, puertas):
        # -- El super(). no funciona si se hereda mas de una clase padre
        Auto.__init__(self,marca,modelo,color,motor, puertas)
        Vehiculo.__init__(self,marca,modelo,color)
        self.capacidad = capacidad
        self.cant_motor = cant_motor
        self.alas = alas
        self.puertas = puertas
    def metodo_mostrar(self):
        return f"{super().metodo_mostrar()}, Capacidad:{self.capacidad}, Cantidad de motores:{self.cant_motor}, Alas:{self.alas}"
    def volar(self):
        return "Volando el avion"

auto1 = Auto("Fiat Duna","1996","Negro",300,5)
print(auto1.metodo_mostrar())
print(auto1.conducir())
avion = Avion("Boeing","747", "Blanco", 3000, 300, 4, 2, 2)
print(avion.metodo_mostrar())
print(avion.volar())