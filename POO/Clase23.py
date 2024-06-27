 # Ej: Una empresa nos solicita un programa que les permita gestionar los empleados.
# Tipos de empleados: Tiempo completo, Medio tiempo, Freelance
# Debemos poder calcular sus salarios y gestionar una lista de todos sus empleados

# 1- Clases y Herencia
    # - Crear una clase base "Empleado" con los siguientes atributos y metodos:
    # ATRIBUTOS: nombre(privado), id_empleado(privado)
    # Metodos: __init__, calcular_salario, get y set, y un __str__
# 2- Subclases:
    # - EmpleadoTiempoCompleto(Empleado)
        #- Atributo: salario_mensual(privado)
        #- Metodo: calcular_salario()
    # - EmpleadoMedioTiempo(Empleado)
        #- Atributo: salario_por_hora(privado), horas_trabajadas(privado)
        # Metodo: calcular_salario()
    # - EmpleadoFreelance(Empleado)
        #- atributo: tarifa_proyecto(privado)
        #- Metodo: calcular_salario()
# 3- Gestion de empleados
    # - class GestionEmpleados
        # - atributo: lista_empleados
    # - Metodos:
        # - agregar_empleado()
        # - agregar_varios_empleados()
        # - eliminar_empleado_por_id()
        # - mostrar_empleados()
        # - calcular_salario(): Calcular y devolver la suma de todos los salarios de todos los empleados de la lista
        # - __str__ : Una representación en cadena de la lista de nombres de empleados
class Empleado:
    def __init__(self,nombre,id_empleado):
        self.__nombre = nombre
        self.__id_empleado = id_empleado
    def calcular_salario(self):
        pass
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre_nuevo):
        self.__nombre = nombre_nuevo
    def get_id(self):
        return self.__id_empleado
    def set_id(self,id_nuevo):
        self.__id_empleado = id_nuevo
    def __str__(self):
        return f"Nombre del empleado: {self.__id_empleado}, ID: {self.__id_empleado}"

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, id_empleado, salario_mensual):
        super().__init__(nombre, id_empleado)
        self.__salario_mensual = salario_mensual
    def calcular_salario(self):
        return self.__salario_mensual

class EmpleadoMedioCompleto(Empleado):
    def __init__(self, nombre, id_empleado, salario_por_hora, horas_trabajadas):
        super().__init__(nombre, id_empleado)
        self.__salario_por_hora = salario_por_hora
        self.__horas_trabajadas = horas_trabajadas
    def calcular_salario(self):
        return self.__salario_por_hora * self.__horas_trabajadas

class EmpleadoFreelance(Empleado):
    def __init__(self, nombre, id_empleado, tarifa_proyecto):
        super().__init__(nombre, id_empleado)
        self.__tarifa_proyecto = tarifa_proyecto
    def calcular_salario(self):
        return self.__tarifa_proyecto

class GestionEmpleados(Empleado):
    def __init__(self):
        self.lista_empleados = []
    def agregar_empleado(self,nombre):
        self.lista_empleados.append(nombre)
    def agregar_varios_empleados(self,*nombres):
        for empleado in nombres:
            self.agregar_empleado(empleado)
    def eliminar_empleado_id(self,id):
        self.lista_empleados = [i for i in self.lista_empleados if id != i.get_id()] # list comprehension
    def mostrar_empleados(self):
        for i in self.lista_empleados:
            print(i)
    def calcular_salarios_totales(self):
        return sum(i.calcular_salario() for i in self.lista_empleados)
empleado_1 = EmpleadoTiempoCompleto("Pepe", 1, 10000)
empleado_2 = EmpleadoMedioCompleto("tomas", 2, 800, 10)
empleado_3 = EmpleadoFreelance("bryan", 3, 60000)
# print(empleado_1.calcular_salario())
lista_1 = GestionEmpleados()
lista_1.agregar_varios_empleados(empleado_1, empleado_2, empleado_3)
print(lista_1.mostrar_empleados())
lista_1.eliminar_empleado_id(3)
print(lista_1.mostrar_empleados())
print(lista_1.calcular_salarios_totales())