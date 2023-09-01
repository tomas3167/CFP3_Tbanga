Algoritmo InicioDeSesión
	//Declaro usuario y contraseña guardados en la base de datos
	usuarioGuardado = "tomas"
	contraseñaGuardada = 123
	//solicito usuario y contraseña del usuario
	Imprimir "Ingrese el usuario:"
	Leer usuarioIngresado 
	Imprimir "Ingrese la contraseña:"
	leer contraseñaIngresada
	//evalúo la condición
	si usuarioIngresado = usuarioGuardado y contraseñaIngresada = contraseñaGuardada Entonces
		Imprimir "Bienvenido " usuarioIngresado
	SiNo
		Imprimir "Datos incorrectos"
	FinSi
FinAlgoritmo
