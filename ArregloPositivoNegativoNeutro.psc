Algoritmo ArregloPosNeg
	Definir dimensionArreglo, valoresArreglo, pos, neg, neu Como Entero
	Imprimir "Ingrese la cantidad de valores"
	Leer dimensionArreglo
	
	Dimension valoresArreglo[dimensionArreglo]
	Para i = 0 Hasta dimensionArreglo - 1 Con Paso 1 Hacer
		Imprimir "Ingrese los valores"
		leer valoresArreglo[i]
	Fin Para
	
	Para i = 0 Hasta dimensionArreglo - 1 Con Paso 1 Hacer
		Si valoresArreglo[i] > 0 Entonces
			pos = pos + 1
		SiNo
			Si valoresArreglo[i] < 0 Entonces
				neg = neg + 1
			SiNo
				Si valoresArreglo[i] == 0 Entonces
					neu = neu + 1
				SiNo
				Fin Si
			Fin Si
		Fin Si
	Fin Para
	
	Imprimir "La cantidad de números positivos son " pos
	Imprimir "La cantidad de números negativos son " neg
	Imprimir "La cantidad de números neutros son " neu
	
FinAlgoritmo
