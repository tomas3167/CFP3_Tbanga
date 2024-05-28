import sqlite3

def conectar():
    conn = sqlite3.connect("productos.db")
    return conn

def crear_tabla():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS productos (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                producto TEXT NOT NULL,
                categoria TEXT NOT NULL,
                cantidad INTEGER NOT NULL
                )
                   ''')
    conn.commit()
    conn.close()

def insertar_producto(producto,categoria,cantidad):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
                INSERT INTO productos (producto,categoria,cantidad) VALUES (?, ?, ?)
                    ''',(producto,categoria,cantidad))
    conn.commit()
    conn.close()

def eliminar(ID):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
                DELETE FROM productos
                    ''',(ID))
    conn.commit()
    conn.close()

def modificar(nombre,stock,nombre_nuevo,stock_nuevo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
                UPDATE productos SET nombre = ?, stock = ? WHERE nombre = ? AND stock = ?
                    ''',(nombre,stock,nombre_nuevo,stock_nuevo))
    conn.commit()
    conn.close()

crear_tabla()
insertar_producto("Tomate","Verduras",30)
insertar_producto("Queso","Lacteos",50)
insertar_producto("Leche","Lacteos",20)
insertar_producto("Cebolla","Verduras",15)
insertar_producto("Fideos","Pasta",15)