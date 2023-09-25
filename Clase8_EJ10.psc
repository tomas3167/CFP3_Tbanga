Algoritmo Clase8_EJ10
	Definir arreglo, arreglo2, dimensionArreglo Como Entero
	
	Imprimir "Ingrese la dimension de su arreglo"
	leer dimensionArreglo
	
	Dimension arreglo[dimensionArreglo]
	Para i = 0 Hasta dimensionArreglo - 1 Con Paso 1 Hacer
		Imprimir "Ingrese un número para el arreglo " i
		Leer arreglo[i]
	Fin Para
	
	Para i = 0 Hasta dimensionArreglo - 1 Con Paso 1 Hacer
		arreglo2 = arreglo[i] ^ 2 // la ^ significa portencia y se hace con alt + 2 y 4 con el bloq num, alt + 2 + 4 todo a la vez.
		Imprimir arreglo[i] " elevado al cuadrado es " arreglo2
	Fin Para
	
FinAlgoritmo
