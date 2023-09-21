Algoritmo Clase8_EJSumaDeArreglos
	Definir arreglo1, arreglo2, arreglo3 Como Entero
	Dimension arreglo1[4]
	Dimension arreglo2[4]
	Dimension arreglo3[4]
	
	Para i = 0 Hasta 4 - 1 Con Paso 1 Hacer
		arreglo1[i] = azar(100)
		arreglo2[i] = azar(100)
		
		arreglo3[i] = arreglo1[i] + arreglo2[i]
		Imprimir "La suma entre " arreglo1[i] " y " arreglo2[i] " es " arreglo3[i]
	Fin Para
	
FinAlgoritmo
