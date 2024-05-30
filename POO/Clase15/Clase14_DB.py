import sqlite3

def conectar(query, parameters=()):
    conn = sqlite3.connect("productos.db")
    cursor = conn.cursor()
    resultado = cursor.execute(query, parameters)
    conn.commit()
    return conn

def obtener_productos():
    query = 'SELECT * FROM productos ORDER BY producto DESC'
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

def eliminar(ID):
    query = 'DELETE FROM productos WHERE ID = (?)'
    parameters = (ID)
    conectar(query,parameters)

def modificar(producto,stock,ID):
    query = 'UPDATE productos SET producto = ?, stock = ? WHERE ID = ?'
    parameters = (producto,stock,ID)
    conectar(query,parameters)

# crear_tabla()
# insertar_producto("Tomate","Verduras",30,"a")
# insertar_producto("Queso","Lacteos",50,"a")
# eliminar("4")
# modificar("Leche",20,1)
# obtener_productos()
