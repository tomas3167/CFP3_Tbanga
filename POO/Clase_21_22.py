  # ENCAPSULAMIENTO: El encapsulamiento es uno de los pilares de la Programación Orientada a Objetos (POO). Consiste en ocultar la implementación interna de un objeto y proporcionar una interfaz pública para interactuar con él. De este modo, se controla qué información y comportamiento de un objeto son accesibles desde el exterior, protegiendo así la integridad de los datos y facilitando el mantenimiento del código.

 # 1- Getter: Es un metodo que se utiliza para acceder al valor de un atributo privado desde fuera de la clase. Permite obtener el valor del atributo sin modificarlo, en Python los getters suelen nombrarse con el prefijo get_nombre

 # 2- Setter: Son un metodo que se utiliza para modificar el valor de un atributo privado desde fuera de la clase. Permite controlar y validar los cambios que se realizan en el atributo. En Python, los setters suelen nombrarse con el prefijo set_nombre

 # 3- __ (doble guion bajo): El uso del doble guion bajo indica que ese atributo es privado y no debe ser accedido directamente desde fuera de la clase. Esta convención ayuda a encapsular y proteger los datos y métodos internos de la clase. Python implementa el "name mangling" (mangling de nombres) para estos atributos, lo que significa que renombra el atributo de forma interna para que sea difícil acceder a él desde fuera de la clase.

class Usuario:
    def __init__(self,nombre, edad, email, contraseña):
        self.nombre = nombre
        self.edad = edad
        self.email = email
        self.__contraseña = contraseña

# Metodo get-set para obtener y modificar el nombre de usuario
    def get_nombre(self):
        return self.nombre
    def set_nombre(self,nombre):
        self.nombre = nombre

    # get-set para la edad
    def get_edad(self):
        return self.edad
    def set_edad(self, edad):
        if edad > 0:
            self.edad = edad
        else:
            print("La edad debe ser un número positivo.")

    # get-set para el email
    def get_email(self):
        return self.email
    def set_email(self, email):
        self.email = email
        
    # get-set para la contraseña
    def get_contraseña(self):
        return self.__contraseña
    def set_contraseña(self, nueva_contraseña):
        self.__contraseña = nueva_contraseña
    
# Método para representar el objeto como una cadena
    def __str__(self):
        return f'Usuario: {self.nombre}, Edad: {self.edad}, Email: {self.email}'

# usuario1 = Usuario("Alice", 30, "alice@example.com", "secreta123")
# print(usuario1)

# usuario1.set_nombre("Tomas")
# usuario1.set_edad(42)
# usuario1.set_email("asdhasjfka@example.com")

# print(usuario1.get_nombre())
# print(usuario1.get_edad())
# print(usuario1.get_email())

# usuario1.set_contraseña("123454678")
# print(usuario1.get_contraseña())

    # Ejercicio 1 - Clase Producto
  # Crea una clase Producto que represente un producto en una tienda en línea. La clase debe tener los siguientes atributos privados:
# __nombre: El nombre del producto (cadena de texto).
# __precio: El precio del producto (número decimal).
# __stock: La cantidad de productos disponibles en inventario (número entero).

   # Implementa los siguientes métodos:
# Métodos getter y setter para nombre.
# Métodos getter y setter para precio, con una validación en el setter para asegurar que el precio sea positivo.
# Métodos getter y setter para stock, con una validación en el setter para asegurar que el stock sea un número entero no negativo.
# Finalmente, implementa el método __str__ para que al imprimir un objeto de la clase Producto, se muestre la siguiente información:
# Producto: <nombre>, Precio: <precio>, Stock: <stock>

class Producto:
    def __init__(self,nombre,precio,stock):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre_nuevo):
        self.__nombre = nombre_nuevo
    def get_precio(self):
        return self.__precio
    def set_precio(self,precio_nuevo):
        if precio_nuevo > 0:
            self.__precio = precio_nuevo
        else:
            return "El precio es negativo"
    def get_stock(self):
        return self.__stock
    def set_stock(self,stock_nuevo):
        if stock_nuevo > 0:
            self.__stock = stock_nuevo
        else:
            return "El stock es negativo"
    def __str__(self):
        return f"Producto: {self.__nombre}, Precio: {self.__precio}, Stock: {self.__stock}" 
# producto1 = Producto("Cebollas",2000,5)
# print(producto1)
# producto1.set_nombre("Tomate")
# print(producto1.get_nombre())
# producto1.set_precio(5000)
# print(producto1.get_precio())

    # Ejercicio 2: Clase Empleado
  # Crea una clase Empleado que represente a un empleado en una empresa. La clase debe tener los siguientes atributos privados:
# __nombre: El nombre del empleado (cadena de texto).
# __salario: El salario del empleado (número decimal).
# __departamento: El departamento al que pertenece el empleado (cadena de texto).
# Implementa los siguientes métodos:

# Métodos getter y setter para nombre.
# Métodos getter y setter para salario, con una validación en el setter para asegurar que el salario sea positivo.
# Métodos getter y setter para departamento.
# Además, implementa un método aumentar_salario(porcentaje) que incremente el salario del empleado por un cierto porcentaje. Asegúrate de validar que el porcentaje sea un número positivo.

# Finalmente, implementa el método __str__ para que al imprimir un objeto de la clase Empleado, se muestre la siguiente información:
# Empleado: <nombre>, Salario: <salario>, Departamento: <departamento>

class Empleado:
    def __init__(self,nombre,salario,departamento):
        self.__nombre = nombre
        self.__salario = salario
        self.__departamento = departamento
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre_nuevo):
        self.__nombre = nombre_nuevo
    def get_salario(self):
        return self.__salario
    def set_salario(self,salario_nuevo):
        if salario_nuevo > 0:
            self.__salario = salario_nuevo
        else:
            return "El salario es negativo"
    def get_departamento(self):
        return self.__departamento
    def set_departamento(self,departamento_nuevo):
        self.__departamento = departamento_nuevo
    def aumentar_salario(self,porcentaje):
        if porcentaje > 0:
            self.__salario += self.__salario * (porcentaje / 100)

        else:
            return "El porcentaje es negativo"
    def __str__(self):
        return f"Empleado: {self.__nombre}, Salario: {self.__salario}, Departamento: {self.__departamento}"
    
# empleado1 = Empleado("Juan",200,"Produccion")
# print(empleado1)

# empleado1.aumentar_salario(20)
# print(empleado1.get_salario())
# print(empleado1)

    # Ejercicio 3: Clase Curso
  # Crea una clase Curso que represente un curso en una plataforma educativa. La clase debe tener los siguientes atributos privados:

# __nombre_curso: El nombre del curso (cadena de texto).
# __instructor: El nombre del instructor del curso (cadena de texto).
# __estudiantes: Una lista que contenga los nombres de los estudiantes inscritos en el curso.
# Implementa los siguientes métodos:

# Métodos getter y setter para nombre_curso.
# Métodos getter y setter para instructor.
# Un método getter para obtener la lista de estudiantes get_estudiantes().
# Un método agregar_estudiante(estudiante) que añada un estudiante a la lista de estudiantes.
# Un método remover_estudiante(estudiante) que elimine un estudiante de la lista de estudiantes si existe en la lista.
# Un método listar_estudiantes() que devuelva una cadena con todos los nombres de los estudiantes inscritos, separados por comas.
# Un método __str__ para representar el objeto como una cadena que muestre el nombre del curso y el nombre del instructor.

class Curso:
    def __init__(self,nombre_curso,instructor,estudiantes=[]):
        self.__nombre_curso = nombre_curso
        self.__instructor = instructor
        self.__estudiantes = estudiantes
    def get_nombre_curso(self):
        return self.__nombre_curso
    def set_nombre_curso(self,nuevo_nombre):
        self.__nombre_curso = nuevo_nombre
    def get_instructor(self):
        return self.__instructor
    def set_instructor(self,nuevo_instructor):
        self.__instructor = nuevo_instructor
    def get_estudiantes(self):
        return self.__estudiantes
    def agregar_estudiantes(self,nuevo_estudiante):
        self.__estudiantes.append(nuevo_estudiante)
    def remover_estudiantes(self,estudiante):
        if estudiante in self.__estudiantes:
            self.__estudiantes.remove(estudiante)
        else:
            print(f"El estudiante '{estudiante}' no esta la lista")
    def listar_estudiantes(self):
        return " , ".join(self.__estudiantes) # -- JOIN es para poner un separador
    def __str__(self):
        return f"Curso: {self.__nombre_curso}, Instructor: {self.__instructor}"

curso1 = Curso("a","s",["Juan","Pepe"])
print(curso1.get_estudiantes())
curso1.agregar_estudiantes("tomas")
print(curso1.get_estudiantes())
print(curso1.listar_estudiantes())
print(curso1)
curso1.remover_estudiantes("pepito")
print(curso1.get_estudiantes())
