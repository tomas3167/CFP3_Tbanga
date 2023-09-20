Algoritmo EJ9_2daOpción
	Definir arreglo, num, Existe Como Entero
	
	Dimension arreglo[10]
	arreglo[0] = 4
	arreglo[1] = 56
	arreglo[2] = 7
	arreglo[3] = 3
	arreglo[4] = 9
	arreglo[5] = 23
	arreglo[6] = 14
	arreglo[7] = 8
	arreglo[8] = 15
	arreglo[9] = 5
	
	Imprimir "Ingrese un número"
	leer num
	
	i = 0
	
	Mientras i <= 9 Hacer
		Si num = arreglo[i] Entonces
			Existe = Existe + 1
		Fin Si
		
		i = i + 1
	Fin Mientras
	
	Si Existe > 0 Entonces
		Imprimir "El número existe"
	SiNo
		Imprimir "El número no existe"
	Fin Si
	
FinAlgoritmo
