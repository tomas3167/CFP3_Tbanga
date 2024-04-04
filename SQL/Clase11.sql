CREATE TABLE if not EXISTS Sucursales (
	ID_Sucursal INTEGER PRIMARY KEY AUTOINCREMENT not null,
	Nombre TEXT not NULL,
	Direccion TEXT not NULL,
	Telefono TEXT not NULL
	);

CREATE TABLE if not EXISTS Vendedores (
	ID_Vendedor INTEGER PRIMARY KEY AUTOINCREMENT not NULL,
	Nombre TEXT not NULL,
	Apellido TEXT not NULL,
	Edad INTEGER not NULL,
	Direccion TEXT not NULL,
	ID_Sucursal INTEGER,
		FOREIGN KEY (ID_Sucursal) REFERENCES Sucursales(ID_Sucursal)
	);

CREATE TABLE if not EXISTS Clientes (
	ID_Cliente INTEGER PRIMARY KEY AUTOINCREMENT not NULL,
	Nombre TEXT not NULL,
	Apellido TEXT not NULL,
	Edad INTEGER not NULL,
	Direccion TEXT not NULL,
	Telefono TEXT not NULL,
	Correo TEXT not NULL
	);

CREATE TABLE if not EXISTS Automoviles (
	ID_Automovil INTEGER PRIMARY KEY AUTOINCREMENT not NULL,
	Marca TEXT not NULL,
	Modelo TEXT not NULL,
	Año INTEGER,
	Color TEXT not NULL,
	Tipo_combustible TEXT not NULL,
	ID_Sucursal INTEGER,
	Transmision TEXT not NULL,
		FOREIGN KEY (ID_Sucursal) REFERENCES Sucursales(ID_Sucursal)
	);

insert into Sucursales (Nombre, Direccion, Telefono) values ('9 Debs Avenue', 'Palermo', '293-779-1604');
insert into Sucursales (Nombre, Direccion, Telefono) values ('26890 Waubesa Street', 'Saavedra', '160-484-3461');
insert into Sucursales (Nombre, Direccion, Telefono) values ('7 Westend Alley', 'Avellaneda', '268-342-2524');
insert into Sucursales (Nombre, Direccion, Telefono) values ('806 Merchant Lane', 'Belgrano', '192-353-7020');
insert into Sucursales (Nombre, Direccion, Telefono) values ('211 New Castle Plaza', 'Once', '566-722-3189');
insert into Sucursales (Nombre, Direccion, Telefono) values ('Himax Technologies, Inc.', 'Congreso', '349-620-7483');
insert into Sucursales (Nombre, Direccion, Telefono) values ('FTD Companies, Inc.', 'Recoleta', '205-298-0844');
insert into Sucursales (Nombre, Direccion, Telefono) values ('Prudential Short, Inc.', 'Parque Patricios', '711-503-8613');
insert into Sucursales (Nombre, Direccion, Telefono) values ('Tremor Video, Inc.', 'Flores', '110-107-3853');
insert into Sucursales (Nombre, Direccion, Telefono) values ('Ulta Beauty, Inc.', 'Tigre', '501-115-1247');

insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Vidovik', 'Toretta', 51, '64 Del Sol Trail', 9);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Opaline', 'Rosiello', 52, '323 Sachs Street', 3);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Marthena', 'Piggens', 31, '60027 Fremont Crossing', 10);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Jarred', 'Snowdon', 66, '51902 Glendale Terrace', 3);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Barthel', 'Dominguez', 56, '8 Shopko Court', 4);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Sybille', 'McNab', 50, '65 Mockingbird Lane', 8);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Rochelle', 'Fargie', 67, '12 Loeprich Center', 8);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Falito', 'Blanpein', 25, '8529 Atwood Crossing', 10);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Merline', 'Weatherell', 30, '995 Sherman Drive', 4);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Cherri', 'Brazel', 45, '07 Dahle Drive', 1);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Melissa', 'McSporrin', 47, '0 Meadow Ridge Plaza', 10);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Charin', 'Bissill', 20, '1308 Mayfield Street', 5);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Elora', 'Anselmi', 68, '0 Sutteridge Center', 10);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Rochette', 'Bewshire', 54, '9 Aberg Trail', 8);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Janek', 'Sonschein', 23, '9591 Comanche Center', 4);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Ulrika', 'Headrick', 58, '9 Jana Terrace', 6);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Corilla', 'Baugham', 69, '73 Blue Bill Park Alley', 9);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Inger', 'Shout', 24, '68455 Goodland Parkway', 4);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Bourke', 'Clowsley', 66, '674 Mcguire Junction', 9);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Bobine', 'Tenby', 50, '5875 Farwell Trail', 9);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Tulley', 'Boorn', 67, '1 Kim Avenue', 6);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Pavia', 'Prahl', 24, '86545 Straubel Terrace', 1);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Alexandrina', 'Vize', 31, '5119 Blackbird Street', 2);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Angel', 'Belshaw', 30, '89 Buell Lane', 3);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Deck', 'Tiddeman', 66, '8 Burning Wood Terrace', 5);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Binny', 'Folan', 66, '94924 Bluestem Road', 7);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Conchita', 'Deme', 31, '9 Messerschmidt Plaza', 6);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Marlane', 'Haggis', 52, '56 Arapahoe Pass', 5);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Vance', 'Ringe', 61, '329 Rusk Lane', 3);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Kelvin', 'Flipek', 46, '3172 High Crossing Center', 5);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Bidget', 'Valentetti', 61, '54529 Spohn Plaza', 3);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Felipa', 'Lightwood', 37, '09003 Quincy Terrace', 3);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Vail', 'Hanvey', 26, '0046 Pepper Wood Junction', 9);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Ruthie', 'Wanklyn', 20, '56 Quincy Avenue', 8);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Ad', 'Quiney', 54, '6285 Swallow Terrace', 4);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Essy', 'Allworthy', 60, '19 Gina Way', 9);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Filmer', 'Poad', 33, '78 Drewry Hill', 8);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Emeline', 'Hornbuckle', 53, '2 Prentice Pass', 6);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Linc', 'Schust', 35, '4973 Helena Junction', 6);
insert into Vendedores (Nombre, Apellido, Edad, Direccion, ID_Sucursal) values ('Tim', 'Mumbey', 46, '81 Linden Way', 1);

insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Shayne', 'Shrigley', 55, '2 Loftsgordon Avenue', '455-856-5160', 'sshrigley0@ca.gov');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Berne', 'Calleja', 49, '740 Grim Crossing', '300-418-6193', 'bcalleja1@nationalgeographic.com');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Martelle', 'Yelding', 56, '5313 Arizona Point', '925-630-0605', 'myelding2@free.fr');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Emlyn', 'Halwill', 57, '524 New Castle Hill', '749-678-8433', 'ehalwill3@geocities.jp');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Bathsheba', 'Kenton', 22, '860 Logan Alley', '419-912-8154', 'bkenton4@com.com');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Hewe', 'Londesborough', 35, '70 3rd Trail', '327-423-8051', 'hlondesborough5@nsw.gov.au');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Waldemar', 'Hansemann', 26, '56169 Fremont Pass', '717-794-7025', 'whansemann6@nymag.com');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Ana', 'Ogelsby', 44, '3527 Fairfield Road', '941-279-6008', 'aogelsby7@wikimedia.org');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Felicity', 'Bruckmann', 25, '6981 Pearson Point', '598-165-4031', 'fbruckmann8@craigslist.org');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Nert', 'Listone', 28, '4178 Atwood Lane', '575-760-3425', 'nlistone9@hatena.ne.jp');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Giacobo', 'Burnup', 39, '13 Debra Trail', '408-244-9488', 'gburnupa@theglobeandmail.com');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Lurlene', 'McGahey', 22, '108 Division Trail', '694-537-6866', 'lmcgaheyb@multiply.com');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Abramo', 'Escofier', 20, '1024 Forest Run Hill', '501-718-0483', 'aescofierc@aboutads.info');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Lynnette', 'Sills', 36, '99402 Homewood Parkway', '728-972-7813', 'lsillsd@prlog.org');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Melloney', 'Plewes', 27, '4 Reinke Street', '879-819-2442', 'mplewese@alexa.com');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Jaclin', 'Kuban', 44, '4230 Hoffman Hill', '319-604-4353', 'jkubanf@examiner.com');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Niall', 'Dary', 60, '585 Mayfield Lane', '369-692-2111', 'ndaryg@diigo.com');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Rebbecca', 'Radmer', 43, '071 Melby Drive', '256-308-4043', 'rradmerh@sbwire.com');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Bruce', 'Elphinstone', 40, '631 Riverside Lane', '171-848-6575', 'belphinstonei@i2i.jp');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Terrel', 'Baser', 25, '469 Truax Parkway', '133-596-8832', 'tbaserj@ted.com');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Leoline', 'Halm', 20, '43436 Menomonie Center', '427-409-8041', 'lhalm2c@weather.com');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Cos', 'Rozzell', 29, '568 Macpherson Park', '532-244-5136', 'crozzell2d@amazon.co.jp');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Ossie', 'MacGuiness', 70, '80399 Goodland Pass', '273-875-0523', 'omacguiness2e@wired.com');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Lorette', 'Cromleholme', 27, '236 Sunbrook Plaza', '961-636-5748', 'lcromleholme2f@loc.gov');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Dulcine', 'Paulot', 36, '776 Utah Point', '490-750-5089', 'dpaulot2g@economist.com');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Evangelina', 'Brinkman', 25, '00 Southridge Junction', '307-584-6543', 'ebrinkman2h@who.int');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Zacharia', 'O''Lagene', 31, '90 Namekagon Street', '896-129-1445', 'zolagene2i@51.la');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Whitney', 'Ferns', 34, '3 Manley Terrace', '391-112-4121', 'wferns2j@goodreads.com');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Dasi', 'Mathou', 28, '765 Oneill Way', '439-931-5834', 'dmathou2k@hatena.ne.jp');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Karisa', 'Argabrite', 48, '3 Lakewood Road', '892-649-3167', 'kargabrite2l@abc.net.au');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Georgie', 'Champney', 28, '64 Fallview Terrace', '604-373-3320', 'gchampney2m@eepurl.com');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Alyson', 'Palfreyman', 29, '1 Columbus Hill', '148-290-8682', 'apalfreyman4q@cbc.ca');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Cherry', 'Kelcher', 55, '6240 Dixon Drive', '785-522-5323', 'ckelcher4r@bloglines.com');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Diego', 'O'' Brian', 67, '07 2nd Pass', '607-541-8169', 'dobrian4s@uiuc.edu');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Karalee', 'Langhorn', 24, '931 Arapahoe Street', '366-835-2167', 'klanghorn4t@cbsnews.com');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Teresina', 'Bruyntjes', 66, '60026 Dovetail Terrace', '226-133-5968', 'tbruyntjes4u@artisteer.com');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Jan', 'Waggett', 56, '64728 Heath Way', '855-205-7163', 'jwaggett4v@rambler.ru');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Anica', 'Dorrance', 68, '45622 5th Parkway', '408-471-1719', 'adorrance4w@google.co.jp');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Cully', 'Whitwood', 58, '62749 Merry Park', '128-695-4694', 'cwhitwood4x@independent.co.uk');
insert into Clientes (Nombre, Apellido, Edad, Direccion, Telefono, Correo) values ('Broddy', 'Tunno', 34, '69 Sachtjen Road', '661-680-6083', 'btunno4y@about.com');

insert into Automoviles (Marca, Modelo, Año, Color, Tipo_combustible, ID_Sucursal, Transmision) values ('Volkswagen', 'Cabriolet', 1990, 'Orange', 'Electrico', 2, 'Automatico');
insert into Automoviles (Marca, Modelo, Año, Color, Tipo_combustible, ID_Sucursal, Transmision) values ('GMC', 'Yukon XL 1500', 2002, 'Purple', 'Nafta', 2, 'Automatico');
insert into Automoviles (Marca, Modelo, Año, Color, Tipo_combustible, ID_Sucursal, Transmision) values ('Honda', 'Accord', 2009, 'Fuscia', 'Nafta', 8, 'Manual');
insert into Automoviles (Marca, Modelo, Año, Color, Tipo_combustible, ID_Sucursal, Transmision) values ('Cadillac', 'Eldorado', 1997, 'Fuscia', 'Electrico', 10, 'Manual');
insert into Automoviles (Marca, Modelo, Año, Color, Tipo_combustible, ID_Sucursal, Transmision) values ('Scion', 'tC', 2009, 'Violet', 'Electrico', 1, 'Automatico');
insert into Automoviles (Marca, Modelo, Año, Color, Tipo_combustible, ID_Sucursal, Transmision) values ('Pontiac', 'Grand Am', 1997, 'Goldenrod', 'Diesel', 7, 'Automatico');
insert into Automoviles (Marca, Modelo, Año, Color, Tipo_combustible, ID_Sucursal, Transmision) values ('Buick', 'Rendezvous', 2004, 'Aquamarine', 'Nafta', 10, 'Manual');
insert into Automoviles (Marca, Modelo, Año, Color, Tipo_combustible, ID_Sucursal, Transmision) values ('Acura', 'Legend', 1987, 'Maroon', 'Nafta', 2, 'Manual');
insert into Automoviles (Marca, Modelo, Año, Color, Tipo_combustible, ID_Sucursal, Transmision) values ('Acura', 'Integra', 2000, 'Khaki', 'Diesel', 9, 'Automatico');
insert into Automoviles (Marca, Modelo, Año, Color, Tipo_combustible, ID_Sucursal, Transmision) values ('Chevrolet', 'G-Series G30', 1992, 'Fuscia', 'Nafta', 10, 'Automatico');
insert into Automoviles (Marca, Modelo, Año, Color, Tipo_combustible, ID_Sucursal, Transmision) values ('Mercury', 'Sable', 1988, 'Khaki', 'Nafta', 7, 'Manual');
insert into Automoviles (Marca, Modelo, Año, Color, Tipo_combustible, ID_Sucursal, Transmision) values ('Volkswagen', 'Jetta', 1996, 'Goldenrod', 'Diesel', 2, 'Automatico');
insert into Automoviles (Marca, Modelo, Año, Color, Tipo_combustible, ID_Sucursal, Transmision) values ('GMC', 'Canyon', 2010, 'Violet', 'Nafta', 8, 'Manual');
insert into Automoviles (Marca, Modelo, Año, Color, Tipo_combustible, ID_Sucursal, Transmision) values ('Pontiac', 'Grand Am', 1992, 'Goldenrod', 'Electrico', 2, 'Manual');
insert into Automoviles (Marca, Modelo, Año, Color, Tipo_combustible, ID_Sucursal, Transmision) values ('Pontiac', 'G6', 2006, 'Orange', 'Diesel', 10, 'Automatico');