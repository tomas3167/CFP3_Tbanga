Proceso ArregloPromedioAlumnos
	Definir cantidadNotas Como Entero
	Definir sumaNotas, promedio, notasArreglo Como Real // Real o flotante sería decimales
	
	Imprimir "Ingrese la cantidad de notas"
	leer cantidadNotas
	
	Dimension notasArreglo[cantidadNotas]
	
	Para i = 0 Hasta cantidadNotas - 1 Con Paso 1 Hacer
		Imprimir "Ingrese la nota"
		Leer notasArreglo[i]
		sumaNotas = sumaNotas + notasArreglo[i]
		promedio = sumaNotas / cantidadNotas
	Fin Para
	
	Imprimir "El promedio es " promedio
	
	
FinProceso
