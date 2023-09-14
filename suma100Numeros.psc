Algoritmo suma100Numeros
	Definir suma, contador Como Entero // esto significa que suma y contador solo van a almacenar datos de tipo entero
	suma = 0
	contador = 1 // inicializo las variables
	Mientras contador <= 100 Hacer
		suma = suma + contador
		contador = contador + 1
		Imprimir suma " - " contador
	Fin Mientras
	Imprimir "La suma total es " suma
FinAlgoritmo
