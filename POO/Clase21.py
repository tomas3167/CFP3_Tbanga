  # ENCAPSULAMIENTO: El encapsulamiento es uno de los pilares de la Programación Orientada a Objetos (POO). Consiste en ocultar la implementación interna de un objeto y proporcionar una interfaz pública para interactuar con él. De este modo, se controla qué información y comportamiento de un objeto son accesibles desde el exterior, protegiendo así la integridad de los datos y facilitando el mantenimiento del código.

 # 1- Getter: Es un metodo que se utiliza para acceder al valor de un atributo privado desde fuera de la clase. Permite obtener el valor del atributo sin modificarlo, en Python los getters suelen nombrarse con el prefijo get_nombre

 # 2- Setter: Son un metodo que se utiliza para modificar el valor de un atributo privado desde fuera de la clase. Permite controlar y validar los cambios que se realizan en el atributo. En Python, los setters suelen nombrarse con el prefijo set_nombre

 # 3- __ (doble guion bajo): El uso del doble guion bajo indica que ese atributo es privado y no debe ser accedido directamente desde fuera de la clase. Esta convención ayuda a encapsular y proteger los datos y métodos internos de la clase. Python implementa el "name mangling" (mangling de nombres) para estos atributos, lo que significa que renombra el atributo de forma interna para que sea difícil acceder a él desde fuera de la clase.

class Usuario:
    def __init__(self,nombre, edad, email, contraseña):
        self.nombre = nombre #
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
        if "@" in email:
            self.email = email
        else:
            print("Email no válido.")
    
    # get-set para la contraseña
    def get_contraseña(self):
        return self.__contraseña
    def set_contraseña(self, nueva_contraseña):
        if len(nueva_contraseña) >= 6:  # Ejemplo de validación
            self.__contraseña = nueva_contraseña
        else:
            print("La contraseña debe tener al menos 6 caracteres.")
    
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
# usuario1.set_contraseña("abc")  # -- La contraseña debe tener al menos 6 caracteres.
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
