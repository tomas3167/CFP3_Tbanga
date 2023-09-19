Algoritmo Clase8_EJ8
	Definir numMayor,arreglo Como Entero
	
	Dimension arreglo[10]
	Para i = 0 Hasta 10 - 1 Con Paso 1 Hacer
		arreglo[i] = azar(100)
	Fin Para
	
	numMayor = arreglo[0]
	
	Para i = 0 Hasta 10 - 1 Con Paso 1 Hacer
		
		Si arreglo[i] > numMayor Entonces
			numMayor = arreglo[i]
		Fin Si
		
	Fin Para
	Imprimir "El número mas alto es " numMayor
	
FinAlgoritmo
