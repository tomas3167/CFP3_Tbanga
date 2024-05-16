# class Alumno:
#     def __init__(self,nombre,apellido,edad):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
# alumno_1 = Alumno("Tomas","Banga",35)
# print(f"{alumno_1.nombre},{alumno_1.apellido},{alumno_1.edad}\n")
# alumno_1.nombre = "Juan"
# alumno_1.apellido = "Gonzales"
# alumno_1.edad = 25
# print(f"{alumno_1.nombre},{alumno_1.apellido},{alumno_1.edad}\n")
# alumno_2 = Alumno("Laura","Fernandez",22)
# print(f"{alumno_2.nombre},{alumno_2.apellido},{alumno_2.edad}\n")
    # Si bien esto es posible, es decir modificar los valores de un objeto accediendo a sus atributos, no es la manera mas recomendable, a medida que vayamos avanzando veremos que lo ideal es hacerlo mediante metodos (PILAR: Encapsulamiento)
# alumno_1.domicilio = "Humberto Primo 2256"
# print(alumno_1.domicilio)
# alumno_2.domicilio = "Cabildo 3000"
# print(alumno_2.domicilio)

 # Crear una calculadora usando el paradigma POO
# class Calculadora:
#     def __init__(self,num1,num2,tipo_operacion):
#         self.num1 = num1
#         self.num2 = num2
#         self.tipo_operacion = tipo_operacion
#     def operacion(self):
#         if self.tipo_operacion == "+":
#             resultado = self.num1 + self.num2
#             print (resultado)
#         elif self.tipo_operacion == "-":
#             resultado = self.num1 - self.num2
#             print (resultado)
#         elif self.tipo_operacion == "*":
#             resultado = self.num1 * self.num2
#             print (resultado)
#         elif self.tipo_operacion == "/":
#             resultado = self.num1 / self.num2
#             print (resultado)
# suma_1 = Calculadora(10,12,"+")
# suma_1.operacion()
   # OTRA FORMA DE HACERLO
# class Calculadora:
#     def __init__(self,num1,num2):
#         self.num1 = num1
#         self.num2 = num2
#     def suma(self):
#             return self.num1 + self.num2
#     def resta(self):
#             return self.num1 - self.num2
#     def multi(self):
#             return self.num1 * self.num2
#     def div(self):
#             return self.num1 / self.num2
# oper_1 = Calculadora(10,12)
# print(f"Suma: {oper_1.suma()}")
# print(f"Resta: {oper_1.resta()}")
# print(f"Multiplicacion: {oper_1.multi()}")
# print(f"Division: {oper_1.div()}")
 # Crear una clase hija que herede de Calculadora (SuperClase) sus atributos y metodos y agregar en esta clase hija los metodos de: Potencia, Raiz cuadrada, Seno y Coseno
 # Para hacer la raiz cuadrado y los otros metodos, hay que importar una carpeta
# import math
# class CalculadoraCientifica(Calculadora):
#     def __init__(self, num1, num2):
#         super().__init__(num1, num2)
#     def potencia(self):
#           return self.num1 ** self.num2
#     def raiz(self):
#           return math.sqrt(self.num1)
#     def seno(self):
#           return math.sin(self.num1)
#     def coseno(self):
#           return math.cos(self.num1)
# oper_2 = CalculadoraCientifica(4,3)
# print(f"Potencia: {oper_2.potencia()}")
# print(f"Raiz cuadrada: {oper_2.raiz()}")
# print(f"Seno: {oper_2.seno()}")
# print(f"Coseno: {oper_2.coseno()}")

 # EJ:
class Personaje():
    def __init__(self,nombre,fuerza,inteligencia,defensa,vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    def atributos(self):
        print (f"Nombre: {self.nombre}")
        print (f"Fuerza: {self.fuerza}")
        print (f"inteligencia: {self.inteligencia}")
        print (f"defensa: {self.defensa}")
        print (f"vida: {self.vida}\n")
    def subir_nivel(self,fuerza,inteligencia,defensa,vida):
        print(f"El personaje {self.nombre} subio de nivel")
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa
        self.vida += vida
        print("Nuevos atributos:")
        print(f"F: {self.fuerza} ")
        print(f"I: {self.inteligencia} ")
        print(f"D: {self.defensa} ")
        print(f"V: {self.vida} ")
    def vivo(self):
        return self.vida > 0
    def esta_vivo(self):
        if self.vida > 0:
            print(f"El personaje sigue vivo con {self.vida} de vida")
        else:
            print("El personaje esta muerto")
    def daño(self,enemigo):
        return self.fuerza - enemigo.defensa
        #print(f"El daño que causa {self.nombre} es {self.fuerza - enemigo.defensa} al rival {enemigo.nombre}")
    def atacar(self,enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(f"{self.nombre} le causo {daño} de daño a {enemigo.nombre}")
        if enemigo.vivo():
            print(f"La vida de {enemigo.nombre} es de {enemigo.vida} ")
        else:
            print(f"El enemigo {enemigo.nombre} esta {enemigo.esta_vivo()}")
pj_1 = Personaje("Tomas",200,100,80,150)
pj_1.atributos()
pj_1.subir_nivel(20,50,40,15)
pj_1.esta_vivo()
pj_2 = Personaje("Milagros",300,150,40,100)
print("\n")
pj_2.atributos()
pj_1.daño(pj_2)
pj_1.atacar(pj_2)