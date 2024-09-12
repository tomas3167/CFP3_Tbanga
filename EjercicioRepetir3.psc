Algoritmo EjercicioRepetir3
	definir totalAcumulado Como Entero
	
	Repetir
		Imprimir "Ingrese un número"
		leer num
		Imprimir "¿Desea agregar otro número? si/no"
		leer respuesta
		totalAcumulado = totalAcumulado + num
	Hasta Que respuesta <> "si"
	Imprimir "El valor acumulado es: " totalAcumulado
	
FinAlgoritmo
