CREATE TABLE if NOT EXISTS Productos (
	ID_Producto INTEGER PRIMARY KEY AUTOINCREMENT,
	Producto TEXT not NULL,
	Precio REAL not NULL,
	Cantidad INTEGER not NULL,
	ID_Proveedor INTEGER not NULL,
	ID_Categoria INTEGER not NULL,
		FOREIGN key (ID_Proveedor) REFERENCES Proveedores(ID_Proveedor),
		FOREIGN key (ID_Categoria) REFERENCES Categorias(ID_Categoria)
		);     

CREATE TABLE if NOT EXISTS Clientes (
	ID_Cliente INTEGER PRIMARY KEY AUTOINCREMENT,
	Nombre TEXT(20) not NULL,
	Apellido TEXT not NULL,
	DNI TEXT not NULL,
	Direccion TEXT not NULL,
	Telefono TEXT not NULL,
	Email TEXT not NULL 
	);

CREATE TABLE if not EXISTS Ventas (
	ID_Venta INTEGER PRIMARY KEY AUTOINCREMENT,
	Precio REAL not NULL,
	Cantidad INTEGER not NULL,
	ID_Cliente INTEGER not NULL,
	ID_Producto INTEGER not NULL,
	ID_Comprobante INTEGER not NULL,
		FOREIGN key (ID_Cliente) REFERENCES Clientes(ID_Cliente),
		FOREIGN key (ID_Producto) REFERENCES Productos(ID_Producto),
		FOREIGN key (ID_Comprobante) REFERENCES Comprobantes(ID_Comprobante)
		);

CREATE TABLE if not EXISTS MetodoDePago (
	ID_Metodo INTEGER PRIMARY KEY AUTOINCREMENT,
	Metodo TEXT not NULL,
	Fecha_alta datetime,
	Fecha_baja datetime );

CREATE TABLE if NOT EXISTS Proveedores (
	ID_Proveedor INTEGER PRIMARY KEY AUTOINCREMENT,
	Nombre TEXT not NULL,
	Direccion TEXT );

CREATE TABLE if not EXISTS Categorias (
	ID_Categoria INTEGER PRIMARY KEY AUTOINCREMENT,
	Categoria TEXT not NULL
	);

CREATE TABLE if not EXISTS Devoluciones (
	ID_Devolucion INTEGER PRIMARY KEY AUTOINCREMENT,
	Fecha datetime,
	ID_Cliente INTEGER not NULL,
	ID_Proveedor INTEGER not null,
	ID_Producto INTEGER not null,
		FOREIGN key (ID_Cliente) REFERENCES Clientes(ID_Cliente),
		FOREIGN key (ID_Proveedor) REFERENCES Proveedores(ID_Proveedor),
		FOREIGN key (ID_Producto) REFERENCES Productos(ID_Producto)
		);

CREATE TABLE if not EXISTS Comprobantes (
	ID_Comprobante INTEGER PRIMARY KEY AUTOINCREMENT,
	Num_Comprobante TEXT not NULL,
	Descripcion TEXT,
	Num_CAE TEXT not NULL,
	Fecha datetime not NULL,
	PrecioTotal INTEGER not NULL,
	IVA REAL not NULL,
	ID_Cliente INTEGER not NULL,
	ID_TipoComp INTEGER not NULL,
		FOREIGN key (ID_Cliente) REFERENCES Clientes(ID_Cliente),
		FOREIGN key (ID_TipoComp) REFERENCES TipoDeComprobantes(ID_TipoComp)
		);

CREATE TABLE if not EXISTS TipoDeComprobantes (
	ID_TipoComp INTEGER PRIMARY KEY AUTOINCREMENT,
	TipoComp TEXT not NULL,
	Fecha_alta datetime,
	Fecha_baja datetime );

CREATE TABLE if not EXISTS Envios (
	ID_Envio INTEGER PRIMARY KEY AUTOINCREMENT,
	Fecha datetime,
	ID_TipoEnvio INTEGER not NULL,
	ID_Venta INTEGER not NULL,
	ID_Cliente INTEGER not NULL,
	ID_Producto INTEGER not NULL,
	ID_Metodo INTEGER not NULL,
		FOREIGN key (ID_TipoEnvio) REFERENCES TipoDeEnvio(ID_TipoEnvio),
		FOREIGN key (ID_Venta) REFERENCES Ventas(ID_Venta),
		FOREIGN key (ID_Cliente) REFERENCES Clientes(ID_Cliente),
		FOREIGN key (ID_Producto) REFERENCES Productos(ID_Producto),
		FOREIGN key (ID_Metodo) REFERENCES MetodoDePago(ID_Metodo)
		);

CREATE TABLE if not EXISTS TipoDeEnvio (
	ID_TipoEnvio INTEGER PRIMARY KEY AUTOINCREMENT,
	TipoEnvio TEXT not NULL );

INSERT INTO TipoDeEnvio (TipoEnvio) VALUES
	('Express(24hs)'),
	('Estándar'),
	('Elegís la fecha');

INSERT INTO TipoDeComprobantes (TipoComp,Fecha_alta,Fecha_baja) VALUES
	('Tipo A',NULL,NULL),
	('Tipo B',NULL,NULL),
	('Tipo C',NULL,NULL),
	('Tipo M',NULL,NULL),
	('Nota de crédito',NULL,NULL),
	('Nota de débito',NULL,NULL);

INSERT INTO MetodoDePago (Metodo,Fecha_alta,Fecha_baja) VALUES
	('Crédito',NULL,NULL),
	('Débito',NULL,NULL),
	('Efectivo',NULL,NULL),
	('Transferencia',NULL,NULL),
	('Cheque',NULL,NULL),
	('Mercado Pago',NULL,NULL);

INSERT INTO Categorias (Categoria) VALUES
	('Frutas'),
	('Lácteos'),
	('Carne'),
	('Pasta'),
	('Fiambres'),
	('Vegetales');
INSERT INTO Proveedores (Nombre,Direccion) VALUES
	('Mayorista Makro',NULL),
	('Mayorista Yaguar',NULL),
	('Firox',NULL);