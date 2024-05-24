# Crear la base de datos
import sqlite3

 # Conectar a la base de datos de SQlite
def conectar():
    conn = sqlite3.connect("usuarios.db")
    return conn

 # Crear la tabla de usuarios si no existe
def crear_tabla():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuarios (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT NOT NULL,
                contraseña TEXT NOT NULL
                )
                   ''')
    conn.commit()
    conn.close() # -- Para cerrar la conexion a la base de datos asi no ocupa mucha memoria

 # Insertar usuarios en la base de datos
def insertar_usuarios(usuario,contraseña):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
                INSERT INTO usuarios (usuario,contraseña) VALUES (?, ?)
                    ''',(usuario,contraseña))
    conn.commit()
    conn.close()

 # Validar usuario
def validar_usuario(usuario, contraseña):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
                SELECT * FROM usuarios WHERE usuario = ? AND contraseña = ?
                   ''',(usuario,contraseña))
    usuario_encontrado = cursor.fetchone() # -- Para guardar el usuario
    conn.close()
    return usuario_encontrado is not None

 # Crear la tabla (Ejecuta la funcion crear_tabla)
crear_tabla()
insertar_usuarios("lopez","1111")
