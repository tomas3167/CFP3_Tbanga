Proceso ValoresPorTeclado2
	Definir numArreglo Como entero
	
	Imprimir "Ingrese el n�mero de �ndices que quiere"
	leer dimensionArreglo
	
	Dimension numArreglo[dimensionArreglo]
	
	para i = 0 hasta dimensionArreglo - 1 Con Paso 1 Hacer // se le pone el -1 para evitar errores y desbordamiento
		Imprimir "Ingrese un valor para el arreglo"
		Leer numArreglo[i] 
	fin para
	Para i = 0 Hasta dimensionArreglo - 1 Con Paso 1 Hacer
		Imprimir "El �ndice n�mero " i " es " numArreglo[i]
	Fin Para
FinProceso
