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
        return f"Nombre del empleado: {self.__nombre}, ID: {self.__id_empleado}"

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
    def __init__(self, lista_empleados=[]):
        self.lista_empleados = lista_empleados
    def agregar_empleado(self,nombre):
        self.lista_empleados.append(nombre)
    def agregar_varios_empleados(self,*nombres):
        for empleado in nombres:
            self.lista_empleados.append(empleado)
    def eliminar_empleado_id(self,id):
        if any(emp.get_id() == id for emp in self.lista_empleados): # -- any: busca si hay aunque sea alguna concidiencia. Es decir, si hay alguna id dentro de la lista que coicida con el id puesto
            self.lista_empleados = [emp for emp in self.lista_empleados if emp.get_id() != id] # list comprehension
            print(f"Empleado con ID {id} eliminado correctamente")
        else:
            print(f"Empleado con ID {id} no encontrado")
    def mostrar_empleados(self):
        for i in self.lista_empleados:
            print(i)
    def calcular_salarios_totales(self):
        return sum(i.calcular_salario() for i in self.lista_empleados)
    def __str__(self):
        nombres = [emp.get_nombre() for emp in self.lista_empleados]
        return f" - ".join(nombres)

def menu():
    print ("Gestion de Empleados")
    print ("1- Agregar empleado")
    print ("2- Agregar varios empleados")
    print ("3- Eliminar empleado por ID")
    print ("4- Mostrar empleados")
    print ("5- Calcular salarios totales")
    print ("6- Salir")

def obtener_datos_empleados(tipo):
    nombre = input("Ingrese el nombre")
    id = int(input("Ingrese el ID"))

    if tipo == 1:
        salario_mensual = int(input("Ingrese el salario mensual: "))
        return EmpleadoTiempoCompleto(nombre, id, salario_mensual)
    elif tipo == 2:
        salario_por_hora = int(input("Ingrese el salario por hora: "))
        horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))
        return EmpleadoMedioCompleto(nombre, id, salario_por_hora, horas_trabajadas)
    elif tipo == 3:
        tarifa_proyecto = int(input("Ingrese la tarifa del proyecto: "))
        return EmpleadoFreelance(nombre, id, tarifa_proyecto)
    else:
        return "Numero incorrecto"

def main():
    gestion = GestionEmpleados()
    while True:
        menu()
        opcion = int(input("Seleccione una opcion: "))
        if opcion >= 6:
            print("Saliendo del programa")
            break
        elif opcion == 5:
            print(gestion.calcular_salarios_totales())
            pass
        elif opcion == 4:
            gestion.mostrar_empleados()
            pass
        elif opcion == 3:
            id = int(input("ID del empleado que desea eliminar: "))
            gestion.eliminar_empleado_id(id)
            gestion.mostrar_empleados()
            pass
        elif opcion == 1:
            tipo = int(input("Ingrese el tipo: 1- Tiempo completo, 2- Tiempo medio- 3- Freelance"))
            empleado = obtener_datos_empleados(tipo)
            gestion.agregar_varios_empleados(empleado)
        elif opcion == 2:
            num_empleados = int(input("Ingrese el numero de emp"))
            empleados = []
            for i in range(num_empleados):
                tipo = int(input("Ingrese el tipo de empleado"))
                empleado = obtener_datos_empleados(tipo)
                empleados.append(empleado)
            gestion.agregar_varios_empleados(*empleados)

# empleado_1 = EmpleadoTiempoCompleto("Pepe", 1, 10000)
# empleado_2 = EmpleadoMedioCompleto("Tomas", 2, 800, 10)
# empleado_3 = EmpleadoTiempoCompleto("Milagros", 3, 20000)
# empleado_4 = EmpleadoFreelance("Bryan", 4, 60000)
# # print(empleado_1.calcular_salario())
# lista_1 = GestionEmpleados()
# lista_1.agregar_varios_empleados(empleado_1, empleado_2, empleado_3, empleado_4)
# print(lista_1.mostrar_empleados())
# lista_1.eliminar_empleado_id(3)
# lista_1.mostrar_empleados()
# print(lista_1.calcular_salarios_totales())
# print(lista_1)
# print(lista_1.calcular_salarios_totales())
# lista_1.mostrar_empleados()

main()