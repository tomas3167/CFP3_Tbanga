Algoritmo ArregloAzar
	Definir valoresArreglo, dimensionArreglo Como Entero
	Imprimir "Ingrese la cantidad de números"
	leer dimensionArreglo
	
	Dimension valoresArreglo[dimensionArreglo]
	Para i = 0 Hasta dimensionArreglo - 1 Con Paso 1 Hacer
		valoresArreglo[i] = azar(999)
		Imprimir Sin Saltar valoresArreglo[i] " "
	Fin Para
	
FinAlgoritmo
