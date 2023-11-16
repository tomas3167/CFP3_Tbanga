import pygame
import sys

 #Inicializar pygame
pygame.init()

 #Establecemos los parametros de la ventana (ancho y alto)
width , height = 1000, 600

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mi primer juego")

 #Para cambiar el color de la ventana
bg_color = (164,50,0)

 #Coordenadas del centro de la ventana
center_x, center_y = width // 2, height // 2

 #Para que el juego funcione de forma infinita, creamos un bucle infinito
while True: # -- Si pongo True siempre va a ser infinito
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Logica del juego
    window.fill(bg_color) # -- Para ponerle color a la ventana

    #Dibujar un estrella en el centro de la ventana
    #                         Esto es el color   - aca empieza la linea  - aca termina -     El 2 es el grosor
    pygame.draw.line(window, (255, 255, 255) , (center_x, center_y -50) , (center_x, center_y +50) , 2)
    pygame.draw.line(window, (255, 255, 255) , (center_x -50, center_y ) , (center_x +50, center_y ) , 2)
    pygame.draw.line(window, (255, 255, 255) , (center_x -40, center_y -40) , (center_x +40, center_y +40) , 2)
    pygame.draw.line(window, (255, 255, 255) , (center_x -40, center_y +40) , (center_x +40, center_y -40) , 2)
    pygame.draw.line(window, (255, 255, 255) , (center_x -50, center_y +20) , (center_x +50, center_y -20) , 2)
    pygame.draw.line(window, (255, 255, 255) , (center_x -50, center_y -20) , (center_x +50, center_y +20) , 2)

    pygame.display.flip()

    #Control de velocidad del bucle
    pygame.time.Clock().tick(60)
