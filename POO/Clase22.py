# 1. Abstraccion: Representar en codigo objetos del mundo real
# 2. Herencia: Mecanismo por el cual una clase padre hereda propiedades y metodos a una clase hija
# 3. Encapsulamiento: Restriccion del acceso directo a los datos del objeto y su manipulacion a traves de metodos (get - set)

# 4. POLIMORFISMO: Se refiere a la capacidad de los objetos de diferentes clases para ser tratados como objetos de una clase comun. Es decir, diferentes clases pueden definir metodos que se llaman igual, pero que tienen comportamientos diferentes. En Python el polimorfismo se logra principalmente a traves de la herencia

import math
class Animal:
    def hacer_sonido(self):
        return "Este metodo debe ser implementado por las clases hijas"

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"
class Vaca(Animal):
    def hacer_sonido(self):
        return "Muuu"
perro = Perro()
gato = Gato()
vaca = Vaca()
# print(perro.hacer_sonido())
# print(gato.hacer_sonido())
# print(vaca.hacer_sonido())
def imprimir_sonido(animal): # -- Otra forma de hacerlo
    print(animal.hacer_sonido())
# imprimir_sonido(perro)
# imprimir_sonido(gato)
# imprimir_sonido(vaca)

 # Ejercicio: figuras geometricas
# A partir de una clase padre "Figura" definir un metodo "calcular_area" que debe ser implementado por todas las clases hijas (Rectangulo, Circulo, Triangulo). Cada subclase que implementa el metodo "calcular_area" debe devolver el resultado de la formula aplicada para cada caso
# Formulas: Rect: Base x Altura -- Cir: PI x (radio ** 2) -- Trian: (B x A) / 2
class Figura:
    def calcular_area(self):
        pass

class Rectangulo(Figura):
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return self.base*self.altura
class Circulo(Figura):
    def __init__(self,radio):
        self.radio = radio
    def calcular_area(self):
        return math.pi*(self.radio**2)
class Triangulo(Figura):
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return (self.base*self.altura)/2

def imprimir_area(figura):
    print(f"El area de la figura es: {figura.calcular_area()}")
rectangulo = Rectangulo(20,40)
circulo = Circulo(8)
triangulo = Triangulo(2,4)
# figuras = [rectangulo, circulo, triangulo]
# for figura in figuras:
#     imprimir_area(figura)

  # --- Otra forma ---
# print(rectangulo.calcular_area())
# print(circulo.calcular_area())
# print(triangulo.calcular_area())

