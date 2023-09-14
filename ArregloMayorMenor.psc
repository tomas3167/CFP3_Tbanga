Algoritmo ArregloMayorMenor
	
	Definir dimensionArreglo, valoresArreglo Como Entero
	
	Imprimir "Ingrese la cantidad de valores"
	Leer dimensionArreglo
	
	Dimension valoresArreglo[dimensionArreglo]
	Para i = 0 Hasta dimensionArreglo - 1 Con Paso 1 Hacer
		Imprimir "Ingrese los valores"
		leer valoresArreglo[i]
	Fin Para
    
	max = valoresArreglo[0]
	min = valoresArreglo[0]
	
	Para i = 1 Hasta dimensionArreglo - 1 Con Paso 1 Hacer
		Si valoresArreglo[i] > max Entonces
			max = valoresArreglo[i]
		SiNo
			Si valoresArreglo[i] < min Entonces
				min = valoresArreglo[i]
			SiNo
			
			Fin Si
		Fin Si
	Fin Para
	
	Imprimir "El número mayor es " max
	Imprimir "El número menor es " min
	
FinAlgoritmo
