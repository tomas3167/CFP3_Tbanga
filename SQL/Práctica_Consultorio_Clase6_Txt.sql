CREATE TABLE if not EXISTS Consultorio (
	ID_consultorio INTEGER PRIMARY KEY AUTOINCREMENT,
	Dirección TEXT NOT NULL,
	Horario INTEGER not NULL,
	Teléfono TEXT not NULL,
	Email TEXT not NULL
	);

CREATE TABLE Medicos (
	ID_medico INTEGER PRIMARY KEY AUTOINCREMENT,
	ID_especialidad INTEGER not NULL,
	ID_consultorio INTEGER not NULL,
	Nombre TEXT (20) not NULL,
	Apellido TEXT (20) not NULL,
	Edad INTEGER not NULL,
	Sexo TEXT (20) not NULL,
		FOREIGN key (ID_consultorio) REFERENCES Consultorio(ID_consultorio),
		FOREIGN key (ID_especialidad) REFERENCES especialidad(ID_especialidad)
	);

CREATE TABLE if not EXISTS Consulta (
	ID_consulta INTEGER PRIMARY KEY AUTOINCREMENT,
	ID_paciente INTEGER not NULL,
	Fecha datetime not NULL,
	ID_medico INTEGER not NULL,
	ID_especialidad INTEGER not NULL,
		FOREIGN key (ID_paciente) REFERENCES Pacientes(ID_paciente),
		FOREIGN key (ID_medico) REFERENCES Médicos(ID_medico)
		FOREIGN key (ID_especialidad) REFERENCES Especialidad(ID_especialidad)
	);
	

CREATE TABLE Pacientes (
	ID_paciente INTEGER PRIMARY KEY AUTOINCREMENT,
	ID_consulta INTEGER not NULL,
	Nombre TEXT (20) not NULL,
	Apellido text (20) not null,
	DNI TEXT not NULL,
	Fecha_nac datetime not NULL,
	Sexo TEXT (20) not null,
	Dirección TEXT not NULL,
	Teléfono TEXT not null,
	Email TEXT not NULL,
		FOREIGN key (ID_consulta) REFERENCES Consulta(ID_consulta)
	);

CREATE TABLE Patologia (
	ID_patología INTEGER PRIMARY KEY AUTOINCREMENT,
	Patología TEXT not NULL,
	ID_especialidad INTEGER not NULL,
		FOREIGN key (ID_especialidad) REFERENCES Especialidad(ID_especialidad)
	);

CREATE TABLE Especialidad (
	ID_especialidad INTEGER PRIMARY KEY AUTOINCREMENT,
	Tipo_especialidad TEXT not NULL,
	ID_medico INTEGER not NULL,
		FOREIGN key (ID_medico) REFERENCES Medicos(ID_medico)
	);