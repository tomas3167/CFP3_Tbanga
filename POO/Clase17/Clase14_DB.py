import sqlite3

def conectar(query, parameters=()):
    with sqlite3.connect("productos.db") as conn:
        cursor = conn.cursor()
        resultado = cursor.execute(query, parameters)
        conn.commit() 
    return resultado

def obtener_productos():
    query = 'SELECT * FROM productos ORDER BY ID DESC'
    db_rows = conectar(query)
    return db_rows
    # conectar(query)

def crear_tabla():
    query = '''
                CREATE TABLE IF NOT EXISTS productos (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                producto TEXT NOT NULL,
                categoria TEXT NOT NULL,
                stock INTEGER NOT NULL,
                descripcion TEXT NOT NULL
                )
                   '''
    conectar(query)

def insertar_producto(producto,categoria,stock,descripcion):
    query = 'INSERT INTO productos VALUES (NULL,?,?,?,?)'
    parameters = (producto, categoria, stock, descripcion)
    conectar(query,parameters)

def eliminar(producto):
    query = 'DELETE FROM productos WHERE producto = ?'
    conectar(query,(producto,))

def modificar(producto):
    query = 'UPDATE productos SET producto = ?'
    parameters = (producto)
    conectar(query,parameters)

crear_tabla()
# insertar_producto("Tomate","Verduras",30,"a")
# insertar_producto("Queso","Lacteos",50,"a")
# eliminar("Cebolla")
# modificar("Leche",20,1)
# obtener()























#---- Esto es para que algunos errores concretos sean excepciones para que la funcion siga
# -- Es para que se seleccione con el clic del mouse
# -- Esto hace que solo se seleccione la parte del texto sino no funciona