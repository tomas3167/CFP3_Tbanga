#Libreria TKINTER --> Entorno grafico --- Ya viene instalada con python
from tkinter import *
from tkinter import messagebox
from Clase13_Logica import validar_usuario

# Funcion que se llama al hacer click en el boton "Iniciar Sesion"
def iniciar_sesion():
    usuario = nombreEntry.get() # -- get es para obtener el texto ingresado en el campo
    contraseña = contraseñaEntry.get()

    if validar_usuario(usuario,contraseña):
        messagebox.showinfo("Exito","Inicio de sesion exitoso") # -- el primero "Exito" es el titulo y el segundo "Inicio etc" es el mensaje
    else:
        messagebox.showerror("Error","Usuario o contraseña incorrectos")
        # El showerror, info y warning solo cambia el color y la ventana que sale

 # 1- VENTANA PRINCIPAL
root = Tk()                     # -- la ventana principal
root.title("Login de usuario")  # -- titulo de la ventana
root.geometry("300x250")        # -- tamaño de la ventana
root.config(bg="skyblue")       # -- color del fondo

 # 2- FRAME (Segundo contenedor)
mainframe = Frame(root)
mainframe.grid(row=0, column=0, padx=20, pady=20) # -- La ubicacion del FRAME -- row = fila column = columna -- padx = espaciado en el eje X -- pady = esp. eje Y
mainframe.config(width=250, height=220) # -- tamaño

 # 3- TITULO
titulo = Label(mainframe, text="Login de usuario", font=("Arial",22))
titulo.grid(row=0, column=0, columnspan=2, pady=10) # -- columnspan es para que el titulo ocupe 2 filas si lo necesita

 # 4- LABEL Y ENTRY --> Usuario - Contraseña
 # - Usuario
nombreLabel = Label(mainframe, text="Usuario: ", font=("Arial",10))
nombreLabel.grid(column=0, row=1, sticky=W, pady=5) # -- sticky para que lo posicione a la izq, der o centro.
nombreEntry = Entry(mainframe, width=30)
nombreEntry.grid(column=1, row=1)
 # - Contraseña
contraseñaLabel = Label(mainframe,text="Contraseña: ", font=("Arial",10))
contraseñaLabel.grid(column=0, row=2, sticky=W, pady=5)
contraseñaEntry = Entry(mainframe, width=30, show="*")
contraseñaEntry.grid(column=1, row=2)

 # 5- BOTON
iniciarSesionBtn = Button(mainframe, text="Iniciar Sesion", command=iniciar_sesion) # -- Command es para llamar a la funcion
iniciarSesionBtn.grid(column=0, row=3, columnspan=2, pady=20)

root.mainloop()  # -- Para que no se cierre