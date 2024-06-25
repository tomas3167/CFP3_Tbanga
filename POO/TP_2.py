
#TODO: ENUNCIADOS

# 1-

# Clase Cine
# Crea una clase Cine que represente una sala de cine. La clase debe tener los siguientes atributos públicos y privados:

# _nombre_cine (privado): El nombre del cine (cadena de texto).
# _direccion (privado): La dirección del cine (cadena de texto).
# _peliculas (privado): Una lista que contenga los títulos de las películas disponibles en el cine (cadena de texto).
# capacidad_sala (público): La capacidad máxima de personas que pueden entrar en una sala (entero).
# precio_entrada (público): El precio de la entrada para una película (flotante).
# Implementa los siguientes métodos:

# Métodos getter y setter para _nombre_cine.
# Métodos getter y setter para _direccion.
# Métodos getter y setter para capacidad_sala.
# Métodos getter y setter para precio_entrada.
# Un método getter para obtener la lista de películas get_peliculas().
# Un método agregar_pelicula(pelicula) que añada una película a la lista de películas.
# Un método remover_pelicula(pelicula) que elimine una película de la lista de películas si existe en la lista.
# Un método buscar_pelicula(pelicula) que devuelva True si la película está en la lista y False en caso contrario.
# Un método listar_peliculas() que devuelva una cadena con todos los títulos de las películas disponibles, separados por comas.
# Un método reemplazar_pelicula(pelicula_vieja, pelicula_nueva) que reemplace una película vieja por una nueva si la película vieja existe en la lista.
# Un método str para representar el objeto como una cadena que muestre el nombre del cine, su dirección, la capacidad de la sala y el precio de la entrada.

class Cine:
    def __init__(self,nombre_cine, direccion, capacidad_sala, precio_entrada):
        self.__nombre_cine = nombre_cine
        self.__direccion = direccion
        self.capacidad_sala = capacidad_sala
        self.precio_entrada = precio_entrada
        self.__peliculas = ["Star Wars", "Indiana jones", "Mision imposible"]
    def get_nombre_cine(self):
        return self.__nombre_cine
    def set_nombre_cine(self,nombre):
        self.__nombre_cine = nombre
    def get_direccion(self):
        return self.__direccion
    def set_direccion(self,direccion_nueva):
        self.__direccion = direccion_nueva
    def get_capacidad(self):
        return self.capacidad_sala
    def set_capacidad(self,capacidad_nueva):
        self.capacidad_sala = capacidad_nueva
    def get_precio(self):
        return self.precio_entrada
    def set_precio(self,precio_nuevo):
        self.precio_entrada = precio_nuevo
    def get_peliculas(self):
        return self.__peliculas
    def agregar_pelicula(self,pelicula):
        self.__peliculas.append(pelicula)
    def remover_pelicula(self,pelicula):
        if pelicula in self.__peliculas:
            self.__peliculas.remove(pelicula)
        else:
            return "La pelicula no existe"
    def buscar_pelicula(self,pelicula):
        if pelicula in self.__peliculas:
            return f"La pelicula {pelicula} esta"
        else:
            return "La pelicula no existe"
    def listar_peliculas(self):
        return ", ".join(self.__peliculas)
    def reemplazar_pelicula(self,pelicula_vieja, pelicula_nueva):
        if pelicula_vieja in self.__peliculas:
            self.__peliculas.remove(pelicula_vieja)
            self.__peliculas.append(pelicula_nueva)
        else:
            return "La pelicula no existe"
    def __str__(self):
        return f"Nombre del cine: {self.__nombre_cine}, Direccion: {self.__direccion}, Capacidad de la sala: {self.capacidad_sala}, Precio de la entrada: {self.precio_entrada}"

cine_1 = Cine("Hoyts","Avenida Corrientes 3000",200,5000)
# print(cine_1)
# print(cine_1.get_peliculas())
# cine_1.agregar_pelicula("Goodfellas")
# print(cine_1.get_peliculas())
# print(cine_1.buscar_pelicula("Indiana jones"))
# cine_1.remover_pelicula("Star wars")
# print(cine_1.get_peliculas())
# print(cine_1.listar_peliculas())
# cine_1.reemplazar_pelicula("Mision imposible","Mision imposible 3")
# print(cine_1.get_peliculas())

# ===============================================================

# 2-
# Clase Restaurante
# Crea una clase Restaurante que represente un restaurante. La clase debe tener los siguientes atributos públicos y privados:

# _nombre_restaurante (privado): El nombre del restaurante (cadena de texto).
# _direccion (privado): La dirección del restaurante (cadena de texto).
# _menu (privado): Una lista que contenga los nombres de los platos disponibles en el menú (cadena de texto).
# aforo_maximo (público): El número máximo de clientes que pueden estar en el restaurante (entero).
# horario_apertura (público): El horario de apertura del restaurante (cadena de texto).
# Implementa los siguientes métodos:

# Métodos getter y setter para _nombre_restaurante.
# Métodos getter y setter para _direccion.
# Métodos getter y setter para aforo_maximo.
# Métodos getter y setter para horario_apertura.
# Un método getter para obtener la lista de platos get_menu().
# Un método agregar_plato(plato) que añada un plato a la lista del menú.
# Un método remover_plato(plato) que elimine un plato de la lista del menú si existe en la lista.
# Un método buscar_plato(plato) que devuelva True si el plato está en la lista y False en caso contrario.
# Un método listar_menu() que devuelva una cadena con todos los nombres de los platos disponibles, separados por comas.
# Un método reemplazar_plato(plato_viejo, plato_nuevo) que reemplace un plato viejo por uno nuevo si el plato viejo existe en la lista.
# Un método str para representar el objeto como una cadena que muestre el nombre del restaurante, su dirección, el aforo máximo y el horario de apertura.

class Restaurante:
    def __init__(self,nombre_restaurante,direccion,aforo_maximo,horario_apertura):
        self.__nombre_restaurante = nombre_restaurante
        self.__direccion = direccion
        self.aforo_maximo = aforo_maximo
        self.horario_apertura = horario_apertura
        self.__menu = ["Ravioles"]
    def get_nombre_restaurante(self):
        return self.__nombre_restaurante
    def set_nombre_restaurante(self,nombre_nuevo):
        self.__nombre_restaurante = nombre_nuevo
    def get_direccion(self):
        return self.__direccion
    def set_direccion(self,direccion_nueva):
        self.__direccion = direccion_nueva
    def get_aforo_max(self):
        return self.aforo_maximo
    def set_aforo_max(self,aforo_nuevo):
        self.aforo_maximo = aforo_nuevo
    def get_horario(self):
        return self.horario_apertura
    def set_horario(self,horario_nuevo):
        self.horario_apertura = horario_nuevo
    def get_menu(self):
        return self.__menu
    def agregar_plato(self,plato):
        self.__menu.append(plato)
    def remover_plato(self,plato):
        if plato in self.__menu:
            self.__menu.remove(plato)
        else:
            return f"El plato {plato} no esta en el menu"
    def buscar_plato(self,plato):
        if plato in self.__menu:
            return(f"El plato {plato} esta en el menu")
        else:
            return("El plato no esta en el menu")
    def listar_platos(self):
        return ", ".join(self.__menu)
    def reemplazar_plato(self,plato_viejo, plato_nuevo):
        if plato_viejo in self.__menu:
            self.__menu.remove(plato_viejo)
            self.__menu.append(plato_nuevo)
        else:
            print("El plato no esta en el menu")
    def __str__(self):
        return f"Nombre del restaurante: {self.__nombre_restaurante}, Direccion: {self.__direccion}, Aforo maximo: {self.aforo_maximo}, Horario de apertura: {self.horario_apertura}"
restaurante = Restaurante("Pepe","Av Independencia 3000",100,"12:00")
print(restaurante)
restaurante.agregar_plato("Milanesa napolitana")
restaurante.agregar_plato("Pizza")
restaurante.agregar_plato("Risoto")
print(restaurante.get_menu())
restaurante.remover_plato("Risoto")
print(restaurante.get_menu())
print(restaurante.buscar_plato("Pizza"))
print(restaurante.listar_platos())