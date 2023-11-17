# Turtle es una carpeta de python para generar graficos
from turtle import *   # --- el * indica todo
from random import randint

 #Configuracion inicial de la pantalla de Turtle
speed(0) # -- Indicar la velocidad a la que se muestren los graficos en la pantalla
penup() # --- significa que el programa levante el cursor para moverse sin dibujar
goto(-180, 140)  # --- para mover la tortuga a las coordenas indicadas

 #Dibujar la pista de carrera y colocar las tortugas en el eje X
for step in range(15):
    write(step, align="center", font=("Arial",14))
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(30)

 #Crear los corredores (tortugas)
red = Turtle()
red.color("red")
red.shape("arrow")

blue = Turtle()
blue.color("blue")
blue.shape("circle")

green = Turtle()
green.color("green")
green.shape("turtle")

yellow = Turtle()
yellow.color("yellow")
yellow.shape("square")

 #Posicionar las tortugas en el punto de partida
red.penup()
red.goto(-200,100)
red.pendown()
blue.penup()
blue.goto(-200,60)
blue.pendown()
green.penup()
green.goto(-200,20)
green.pendown()
yellow.penup()
yellow.goto(-200,-20)
yellow.pendown()

 #Configurar que las tortugas se muevan de forma aleatoria
for turn in range(140):
    red.forward(randint(1,5))
    blue.forward(randint(1,5))
    green.forward(randint(1,5))
    yellow.forward(randint(1,5))
    


done()