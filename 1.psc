Algoritmo InicioDeSesi�n
	//Declaro usuario y contrase�a guardados en la base de datos
	usuarioGuardado = "tomas"
	contrase�aGuardada = 123
	//solicito usuario y contrase�a del usuario
	Imprimir "Ingrese el usuario:"
	Leer usuarioIngresado 
	Imprimir "Ingrese la contrase�a:"
	leer contrase�aIngresada
	//eval�o la condici�n
	si usuarioIngresado = usuarioGuardado y contrase�aIngresada = contrase�aGuardada Entonces
		Imprimir "Bienvenido " usuarioIngresado
	SiNo
		Imprimir "Datos incorrectos"
	FinSi
FinAlgoritmo
