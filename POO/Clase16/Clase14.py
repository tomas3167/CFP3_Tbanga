from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Clase14_DB import *
from Clase14_DB import insertar_producto
from Clase14_DB import eliminar


# Validar que los datos no esten vacios
def validar():
    return len(productoEntry.get()) != 0 and len(categoriaEntry.get()) != 0 and len(stockEntry.get()) != 0 and len(descripcionEntry.get()) != 0

def validar_id():
    return len(idEntry.get()) != 0

def insertar():
    if validar():
        producto = productoEntry.get()
        categoria = categoriaEntry.get()
        stock = stockEntry.get()
        descripcion = descripcionEntry.get()
        insertar_producto(producto,categoria,stock,descripcion)

        productoEntry.delete(0,END)
        categoriaEntry.delete(0,END)
        stockEntry.delete(0,END)
        descripcionEntry.delete(0,END)
    else:
        messagebox.showerror("Error","Los datos estan vacios")
    obtener_productos()

def eliminar_producto():
    if validar_id():
        ID = idEntry.get()
        eliminar(ID)
    else:
        messagebox.showerror("Error","Los datos estan vacios")

def obtener_productos():
    from Clase14_DB import obtener_productos
    grabados = grilla.get_children()  # -- get_children para obtener todas las filas actuales de mi tabla
    for elemento in grabados:
        grilla.delete(elemento)
    # Consulto los datos
    # Llamar a la funcion obtener_productos para obtener todos los productos de la base de datos
    productos = obtener_productos()
    for row in productos:
        grilla.insert('',0,text=row[1],values=row[3])


ventana = Tk()
ventana.title("Stock")
ventana.geometry("700x600")
ventana.config(bg="beige")

mainframe = LabelFrame(ventana,text="Tienda", font=("Arial",12,"bold"))
mainframe.grid(row=0, column=0, padx=40, pady=20)
mainframe.config(width=1000, height=350)
# mainframe.config(bg="beige")

producto = Label(mainframe, text="Producto: ", font=("Arial",12,"bold"))
producto.grid(column=0, row=1, sticky=W, pady=5, padx=5)
productoEntry = Entry(mainframe, width=50)
productoEntry.grid(row=1, column=1, pady=5, padx=5)

categoria = Label(mainframe, text="Categoria: ", font=("Arial",12,"bold"))
categoria.grid(column=0, row=2, sticky=W, pady=5, padx=5)
categoriaEntry = Entry(mainframe, width=50)
categoriaEntry.grid(row=2, column=1, pady=5, padx=5)

stock = Label(mainframe, text="Stock: ", font=("Arial",12,"bold"))
stock.grid(column=0, row=3, sticky=W, pady=5, padx=5)
stockEntry = Entry(mainframe, width=50)
stockEntry.grid(row=3, column=1, pady=5, padx=5)

descripcion = Label(mainframe, text="Descripcion: ", font=("Arial",12,"bold"))
descripcion.grid(column=0, row=4, sticky=W, pady=5, padx=5)
descripcionEntry = Entry(mainframe, width=50)
descripcionEntry.grid(row=4, column=1, pady=5, padx=5)

id = Label(mainframe, text="ID", font=("Arial",12,"bold"))
id.grid(row=5, column=2, padx=0, sticky=W, pady=5)
idEntry = Entry(mainframe, width=20)
idEntry.grid(row=5, column=2, padx=30, pady=5)

añadirBoton = Button(mainframe, text="Añadir", font=("Arial",12,"bold"),command=insertar)
añadirBoton.grid(row=5, column=0, padx=10, sticky=W, pady=5)

modificarBoton = Button(mainframe, text="Modificar", font=("Arial",12,"bold"))
modificarBoton.grid(row=5, column=1, padx=0, sticky=W, pady=5)

eliminarBoton = Button(mainframe, text="Eliminar", font=("Arial",12,"bold"),command=eliminar_producto)
eliminarBoton.grid(row=5, column=1, padx=5, pady=5)

grilla = ttk.Treeview(height=20, columns=("Categoria","Stock","Descripcion"))
grilla.grid(row=6, column=0, pady=5, padx=5)
grilla.heading("#0", text="Producto", anchor=CENTER)
grilla.heading("Categoria", text="Categoria", anchor=CENTER)
grilla.heading("Stock", text="Stock", anchor=CENTER)
grilla.heading("Descripcion", text="Descripcion", anchor=CENTER)

grilla.column("#0", width=150) 
grilla.column("Categoria", width=150)
grilla.column("Stock", width=150)
grilla.column("Descripcion", width=150)

obtener_productos()

ventana.mainloop()
