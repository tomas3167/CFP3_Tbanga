from tkinter import *
from tkinter import ttk
from Clase14_DB import *
from Clase14_DB import obtener_productos


ventana = Tk()
ventana.title("Stock")
ventana.geometry("800x600")
ventana.config(bg="beige")

mainframe = LabelFrame(ventana,text="Tienda", font=("Arial",12,"bold"))
mainframe.grid(row=0, column=0, padx=200, pady=20)
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

añadirBoton = Button(mainframe, text="Añadir", font=("Arial",12,"bold"))
añadirBoton.grid(row=5, column=0, padx=10, sticky=W, pady=5)

eliminarBoton = Button(mainframe, text="Eliminar", font=("Arial",12,"bold"))
eliminarBoton.grid(row=5, column=1, padx=5, sticky=W, pady=5)

modificarBoton = Button(mainframe, text="Modificar", font=("Arial",12,"bold"))
modificarBoton.grid(row=5, column=1, padx=0, pady=5)

grilla = ttk.Treeview(height=10, columns=("Categoria","Stock","Descripcion"),command=obtener_productos())
grilla.grid(row=6, column=0, pady=5, padx=5)
grilla.heading("#0", text="Producto", anchor=CENTER)
grilla.heading("Categoria", text="Categoria", anchor=CENTER)
grilla.heading("Stock", text="Stock", anchor=CENTER)
grilla.heading("Descripcion", text="Descripcion", anchor=CENTER)

grilla.column("#0", width=100) 
grilla.column("Categoria", width=100)
grilla.column("Stock", width=100)
grilla.column("Descripcion", width=100)


ventana.mainloop()
