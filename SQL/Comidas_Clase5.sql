-- CREAR TABLA
CREATE TABLE if not EXISTS Comidas (
	id_comida INTEGER PRIMARY KEY AUTOINCREMENT,
	comida TEXT not NULL,
	precio INTEGER not NULL,
	peso REAL not NULL,
	fecha_vencimiento datetime not NULL
	)


