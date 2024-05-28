from tkinter import *
from tkinter import ttk
from Clase14_DB import eliminar
from Clase14_DB import insertar_producto

ventana = Tk()
ventana.title("Stock")
ventana.geometry("800x600")
ventana.config(bg="beige")

mainframe = LabelFrame(ventana,text="Tienda", font=("Arial",12,"bold"))
mainframe.grid(row=0, column=0, padx=20, pady=20)
mainframe.config(width=1000, height=350)
# mainframe.config(bg="beige")

producto = Label(mainframe, text="Producto: ", font=("Arial",12,"bold"))
producto.grid(column=0, row=1, sticky=W, pady=5, padx=5)
productoEntry = Entry(mainframe, width=50)
productoEntry.grid(row=1, column=1, pady=5, padx=5)

categoria = cantidad = Label(mainframe, text="Categoria: ", font=("Arial",12,"bold"))
categoria.grid(column=0, row=2, sticky=W, pady=5, padx=5)
categoriaEntry = Entry(mainframe, width=50)
categoriaEntry.grid(row=2, column=1, pady=5, padx=5)

cantidad = Label(mainframe, text="Cantidad: ", font=("Arial",12,"bold"))
cantidad.grid(column=0, row=3, sticky=W, pady=5, padx=5)
cantidadEntry = Entry(mainframe, width=50)
cantidadEntry.grid(row=3, column=1, pady=5, padx=5)

añadirBoton = Button(mainframe, text="Añadir", font=("Arial",12,"bold"), command=insertar_producto())
añadirBoton.grid(row=4, column=0, padx=10, sticky=W, pady=5)

eliminarBoton = Button(mainframe, text="Eliminar", font=("Arial",12,"bold"), command=eliminar())
eliminarBoton.grid(row=4, column=1, padx=5, sticky=W, pady=5)

modificarBoton = Button(mainframe, text="Modificar", font=("Arial",12,"bold"))
modificarBoton.grid(row=4, column=1, padx=0, pady=5)

grilla = ttk.Treeview(height=10, columns=3)
grilla.grid(row=5, column=0, pady=5, padx=5)
grilla.heading("#0", text="Producto") 
# grilla.heading("#1",text="Categoria")
grilla.heading("#1",text="Cantidad")


ventana.mainloop()
