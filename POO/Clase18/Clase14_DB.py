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

def modificar(producto_nuevo, stock_nuevo, producto, stock):
    query = 'UPDATE productos SET producto = ?, stock = ? WHERE producto = ? and stock = ?'
    parameters = (producto_nuevo,stock_nuevo,producto,stock)
    conectar(query,parameters)
    # obtener_productos()

crear_tabla()
# insertar_producto("Tomate","Verduras",30,"a")
# insertar_producto("Queso","Lacteos",50,"a")
# eliminar("Cebolla")
# modificar("Leche",20,1)
# obtener()
