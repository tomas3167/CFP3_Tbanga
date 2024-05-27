# Funcion para validar usuario
from Clase13_DB import validar_usuario
def validar_usuario_login(usuario, contraseña): # Importante que la funcion no se llame igual
    return validar_usuario(usuario,contraseña)

    # Diccionario con los usuarios para simular una base de datos
    # usuarios_validos = {
    #     "tomas": "1234",
    #     "rlozano": "pepito",
    #     "pepe": "1111",
    #     "messi": "10"
    # }
    # # Logica para validar el usuario
    # if usuario in usuarios_validos and usuarios_validos[usuario] == contraseña:
    #     return True
    # else:
    #     return False
