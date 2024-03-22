CREATE TABLE Tienda (
	ID_Tienda INTEGER PRIMARY KEY AUTOINCREMENT,
	Nombre TEXT not NULL,
	Direccion TEXT not NULL );

CREATE TABLE Cliente (
	ID_Cliente INTEGER PRIMARY KEY AUTOINCREMENT,
	Nombre TEXT (20) not NULL,
	Apellido TEXT not NULL,
	Email TEXT not NULL,
	Telefono TEXT not NULL );

CREATE TABLE Producto (
	ID_Producto INTEGER PRIMARY KEY AUTOINCREMENT,
	Nombre TEXT not NULL,
	Descripcion TEXT not NULL,
	Precio REAL not NULL,
	Cantidad INTEGER not NULL,
	Categoria TEXT not NULL,
	ID_Tienda INTEGER not NULL,
	FOREIGN KEY (ID_Tienda) REFERENCES Tienda(ID_Tienda)
	);

CREATE TABLE Venta (
	ID_Venta INTEGER PRIMARY KEY AUTOINCREMENT,
	Fecha datetime,
	Total_Venta REAL not NULL,
	ID_Cliente INTEGER not NULL,
	ID_Tienda INTEGER not NULL,
	ID_Producto INTEGER not NULL,
	FOREIGN KEY (ID_Cliente) REFERENCES Cliente(ID_Cliente),
	FOREIGN KEY (ID_Tienda) REFERENCES Tienda(ID_Tienda),
	FOREIGN KEY (ID_Producto) REFERENCES Producto(ID_Producto)
	);

insert into Tienda (ID_Tienda, Nombre, Direccion) values (1, 'SeaChange International', '8649 Luster Parkway');
insert into Tienda (ID_Tienda, Nombre, Direccion) values (2, 'Strattec Security Corporation', '03612 Glendale Place');
insert into Tienda (ID_Tienda, Nombre, Direccion) values (3, 'Marlin Business', '7299 Fallview Trail');
insert into Tienda (ID_Tienda, Nombre, Direccion) values (4, 'Dollar Tree', '955 Esker Plaza');

insert into Cliente (Nombre, Apellido, Email, Telefono) values ('Uriah', 'Tupp', 'utupp0@omniture.com', '107-585-9437');
insert into Cliente (Nombre, Apellido, Email, Telefono) values ('Joanna', 'Tebbitt', 'jtebbitt1@nih.gov', '876-935-4993');
insert into Cliente (Nombre, Apellido, Email, Telefono) values ('Shaw', 'Slewcock', 'sslewcock2@abc.net.au', '540-308-0903');
insert into Cliente (Nombre, Apellido, Email, Telefono) values ('Chandal', 'Dearth', 'cdearth3@parallels.com', '465-126-9035');
insert into Cliente (Nombre, Apellido, Email, Telefono) values ('Dorry', 'Thornewill', 'dthornewill4@creativecommons.org', '449-938-9012');
insert into Cliente (Nombre, Apellido, Email, Telefono) values ('Bentlee', 'Clifforth', 'bclifforth5@reddit.com', '693-353-5791');
insert into Cliente (Nombre, Apellido, Email, Telefono) values ('Vania', 'Purshouse', 'vpurshouse6@columbia.edu', '969-734-3871');
insert into Cliente (Nombre, Apellido, Email, Telefono) values ('Antonella', 'Milkins', 'amilkins7@cbsnews.com', '264-760-4719');
insert into Cliente (Nombre, Apellido, Email, Telefono) values ('Joy', 'Spinelli', 'jspinelli8@usatoday.com', '708-746-0020');
insert into Cliente (Nombre, Apellido, Email, Telefono) values ('Culver', 'Johnston', 'cjohnston9@google.nl', '337-471-9073');
insert into Cliente (Nombre, Apellido, Email, Telefono) values ('Patty', 'Sorrill', 'psorrilla@g.co', '279-603-7301');
insert into Cliente (Nombre, Apellido, Email, Telefono) values ('Annetta', 'Saint', 'asaintb@nih.gov', '225-352-6456');
insert into Cliente (Nombre, Apellido, Email, Telefono) values ('Lammond', 'Sayton', 'lsayton2t@cdc.gov', '566-623-2068');
insert into Cliente (Nombre, Apellido, Email, Telefono) values ('Pincas', 'Mathews', 'pmathews2u@google.ca', '480-709-1595');

insert into Producto (Nombre, Descripcion, Precio, Cantidad, Categoria, ID_Tienda) values ('Mussels - Frozen', 'Pathological fracture in other disease, unspecified shoulder', 48.38, 42, 'Verduras', 3);
insert into Producto (Nombre, Descripcion, Precio, Cantidad, Categoria, ID_Tienda) values ('Dikon', 'Disp fx of greater trochanter of r femr, 7thJ', 77.64, 13, 'Verduras', 1);
insert into Producto (Nombre, Descripcion, Precio, Cantidad, Categoria, ID_Tienda) values ('Pear - Asian', 'Laceration w fb of l rng fngr w damage to nail, subs', 96.77, 46, 'Carnes', 3);
insert into Producto (Nombre, Descripcion, Precio, Cantidad, Categoria, ID_Tienda) values ('Split Peas - Green, Dry', 'Unsp injury of oth blood vessels of thorax, right side, subs', 73.92, 26, 'Carnes', 3);
insert into Producto (Nombre, Descripcion, Precio, Cantidad, Categoria, ID_Tienda) values ('Pepper - Gypsy Pepper', 'Pedl cyc pasngr inj in clsn w nonmtr vehicle nontraf, sqla', 14.23, 12, 'Lacteos', 1);
insert into Producto (Nombre, Descripcion, Precio, Cantidad, Categoria, ID_Tienda) values ('Coffee - Hazelnut Cream', 'Genitourinary myiasis', 21.63, 47, 'Verduras', 3);
insert into Producto (Nombre, Descripcion, Precio, Cantidad, Categoria, ID_Tienda) values ('Energy Drink - Redbull 355ml', 'Unsp inj flexor musc/fasc/tend l mid finger at forarm lv', 37.86, 22, 'Carnes', 4);
insert into Producto (Nombre, Descripcion, Precio, Cantidad, Categoria, ID_Tienda) values ('Squash - Pattypan, Yellow', 'Laceration without foreign body of unsp part of thorax', 80.07, 12, 'Verduras', 4);
insert into Producto (Nombre, Descripcion, Precio, Cantidad, Categoria, ID_Tienda) values ('Wine - Trimbach Pinot Blanc', 'Lacerat flexor musc/fasc/tend l mid fngr at wrs/hnd lv, init', 14.25, 27, 'Carnes', 2);
insert into Producto (Nombre, Descripcion, Precio, Cantidad, Categoria, ID_Tienda) values ('Red Currant Jelly', 'Periumbilic rebound abdominal tenderness', 40.25, 2, 'Verduras', 4);
insert into Producto (Nombre, Descripcion, Precio, Cantidad, Categoria, ID_Tienda) values ('Plastic Wrap', 'Displ intertroch fx r femr, 7thE', 23.13, 3, 'Lacteos', 1);
insert into Producto (Nombre, Descripcion, Precio, Cantidad, Categoria, ID_Tienda) values ('Bread - Roll, Canadian Dinner', 'Oth injury of popliteal artery, right leg, subs encntr', 90.48, 1, 'Verduras', 3);
insert into Producto (Nombre, Descripcion, Precio, Cantidad, Categoria, ID_Tienda) values ('Tea - Darjeeling, Azzura', 'Cardiomyopathy', 63.4, 40, 'Lacteos', 3);

insert into Venta (Fecha, Total_Venta, ID_Cliente, ID_Tienda, ID_Producto) values ('1/15/2023', 673.41, 14, 2, 7);
insert into Venta (Fecha, Total_Venta, ID_Cliente, ID_Tienda, ID_Producto) values ('3/17/2024', 964.12, 7, 4, 9);
insert into Venta (Fecha, Total_Venta, ID_Cliente, ID_Tienda, ID_Producto) values ('10/31/2023', 937.67, 7, 1, 12);
insert into Venta (Fecha, Total_Venta, ID_Cliente, ID_Tienda, ID_Producto) values ('10/8/2022', 976.63, 9, 2, 7);
insert into Venta (Fecha, Total_Venta, ID_Cliente, ID_Tienda, ID_Producto) values ('8/10/2023', 605.33, 10, 4, 1);
insert into Venta (Fecha, Total_Venta, ID_Cliente, ID_Tienda, ID_Producto) values ('12/21/2023', 766.11, 6, 3, 13);
insert into Venta (Fecha, Total_Venta, ID_Cliente, ID_Tienda, ID_Producto) values ('8/2/2023', 320.39, 10, 2, 6);
insert into Venta (Fecha, Total_Venta, ID_Cliente, ID_Tienda, ID_Producto) values ('4/30/2023', 242.37, 4, 2, 11);
insert into Venta (Fecha, Total_Venta, ID_Cliente, ID_Tienda, ID_Producto) values ('5/27/2022', 931.79, 14, 1, 10);
insert into Venta (Fecha, Total_Venta, ID_Cliente, ID_Tienda, ID_Producto) values ('5/2/2022', 619.52, 1, 3, 8);
insert into Venta (Fecha, Total_Venta, ID_Cliente, ID_Tienda, ID_Producto) values ('3/2/2023', 466.62, 3, 4, 12);
insert into Venta (Fecha, Total_Venta, ID_Cliente, ID_Tienda, ID_Producto) values ('8/5/2022', 230.45, 6, 2, 10);
insert into Venta (Fecha, Total_Venta, ID_Cliente, ID_Tienda, ID_Producto) values ('10/10/2023', 480.59, 9, 3, 9);
insert into Venta (Fecha, Total_Venta, ID_Cliente, ID_Tienda, ID_Producto) values ('1/20/2023', 112.46, 3, 3, 12);
insert into Venta (Fecha, Total_Venta, ID_Cliente, ID_Tienda, ID_Producto) values ('6/4/2023', 795.95, 9, 4, 1);
insert into Venta (Fecha, Total_Venta, ID_Cliente, ID_Tienda, ID_Producto) values ('12/24/2023', 379.55, 2, 3, 11);
insert into Venta (Fecha, Total_Venta, ID_Cliente, ID_Tienda, ID_Producto) values ('2/26/2023', 25.89, 1, 2, 12);
insert into Venta (Fecha, Total_Venta, ID_Cliente, ID_Tienda, ID_Producto) values ('10/26/2022', 559.27, 1, 1, 2);
insert into Venta (Fecha, Total_Venta, ID_Cliente, ID_Tienda, ID_Producto) values ('10/27/2022', 242.38, 12, 1, 1);

