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
    def vida(self):
        if self.vida < 0:
            return "muerto"
        else:
            return f"La vida del personaje {self.nombre} es {self.vida}"
    def esta_vivo(self):
        return self.vida > 0
        # if self.vida > 0:
        #     print(f"El personaje {self.nombre} sigue vivo con {self.vida} de vida")
        # else:
        #     print(f"El personaje {self.nombre} esta muerto")
    def daño(self,enemigo):
        return self.fuerza - enemigo.defensa
    def atacar(self,enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(f"{self.nombre} le causo {daño} de daño a {enemigo.nombre}")
        if enemigo.vida > 0:
            print(f"La vida de {enemigo.nombre} es de {enemigo.vida} ")
        else:
            print(f"El enemigo {enemigo.nombre} esta muerto")

# pj_1 = Personaje("Tomas",200,100,80,150)
# pj_1.atributos()
# pj_1.subir_nivel(20,50,40,15)
# pj_1.esta_vivo()
# pj_2 = Personaje("Milagros",300,150,40,200)
# print("\n")
# pj_2.atributos()
# pj_1.atacar(pj_2)
# pj_2.esta_vivo()
# print(f"El daño que causa el personaje {pj_1.nombre} a {pj_2.nombre} es de  {pj_1.daño(pj_2)}")
class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida,arma=""):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.arma = arma
    def elegir_arma(self):
        opcion = int(input("1 = Daga (20 daño)\n2 = Espada (50 daño)\n"))
        if opcion == 1:
            self.arma = 20
            self.fuerza += self.arma
            return (f"Fuerza actual: {self.fuerza}")
        else:
            self.arma = 50
            self.fuerza += self.arma
            return (f"Fuerza actual: {self.fuerza}")
    def mostrar_arma(self):
        if self.arma == 20:
            return(f"Arma actual: Daga {self.arma} de daño")
        else:
            return(f"Arma actual: Espada {self.arma} de daño")
class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, hechizo=""):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.hechizo = hechizo
    def elegir_hechizo(self):
        opcion = int(input("1 = Rayo (40 daño)\n2 = Fuego (90 daño)\n3 = Curacion (200 vida)"))
        if opcion == 1:
            self.hechizo = 40
            self.fuerza += self.hechizo
            return (f"Fuerza actual: {self.fuerza}")
        elif opcion == 2:
            self.hechizo = 90
            self.fuerza += self.hechizo
            return (f"Fuerza actual: {self.fuerza}")
        else:
            self.hechizo = 200
            self.vida += self.hechizo
            return (f"Vida actual: {self.vida}")
    def mostrar_hechizo(self):
        if self.hechizo == 40:
            return (f"Hechizo actual: Rayo ({self.hechizo} de daño)")
        elif self.hechizo == 90:
            return (f"Hechizo actual: Fuego ({self.hechizo} de daño)")
        else:
            return (f"Hechizo actual: Curacion ({self.hechizo} de vida)")

        
tomas = Guerrero("Tomas",125,120,120,900)
tomas.atributos()
# print(pj_3.elegir_arma())
# print(pj_3.mostrar_arma())
# pj_3.atributos()
# print("-----------\n")
milagros = Mago("Milagros",150,200,115,500)
milagros.atributos()
# print(pj_4.elegir_hechizo())
# print(pj_4.mostrar_hechizo())
# print(pj_4.daño(pj_3))
# pj_4.atributos()
# pj_3.atacar(pj_4)

def combate(jugador_1,jugador_2):
    turno = 1
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print(f"\n Turno: {turno}")
        print(f"Accion de {jugador_1.nombre}")
        jugador_1.atacar(jugador_2)
        print(f"Accion de {jugador_2.nombre}")
        jugador_2.atacar(jugador_1)
        turno += 1
    if jugador_1.esta_vivo():
        print(f"\n {jugador_1.nombre} ha ganado")
    elif jugador_2.esta_vivo():
        print(f"\n {jugador_2.nombre} ha ganado")
    else:
        print("\n Fue una dura pelea que termino en empate")
combate(tomas,milagros)