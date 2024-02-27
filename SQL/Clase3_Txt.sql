-- DDL
-- CREATE
CREATE TABLE if not EXISTS Ventas (
	id_venta INTEGER PRIMARY KEY AUTOINCREMENT,
	nombre TEXT (20) not null,
	cantidad INTEGER not null,
	precio REAL not null
	);

-- DROP (Elimina base de datos, tablas, etc)
DROP TABLE Ventas;

-- ALTER (Permite modificar o agregar campos en una tabla existente)
-- ALTER TABLE Nombre_tabla DROP COLUMN Columna
ALTER TABLE Ventas DROP COLUMN precio;
-- ALTER TABLE Nombre_tabla ADD COLUMN Columna Tipo_De_Dato
ALTER TABLE Ventas ADD COLUMN precio REAL

-- INSERT (Permite insertar filas (registros) en una tabla)
-- INSERT INTO Nombre_tabla VALUES Tupla
INSERT INTO Ventas (nombre,cantidad,precio) VALUES
	('Daivis', 10, 100.5),
	('Milagros', 40, 10.5),
	('Tomas',25, 67.4)

-- SELECT (Recuperar datos de una tabla)
-- SELECT Columna FROM Nombre_Tabla
SELECT cantidad, nombre FROM Ventas

-- UPDATE (Actualizar registros de una tabla)
-- UPDATE Nombre_Tabla SET CampoActualizar = NuevoValor WHERE
UPDATE Ventas SET cantidad = 20, precio = 20.6 WHERE id_venta = 1

-- DELETE (Eliminar)
-- DELETE FROM NombreTabla WHERE
DELETE FROM Ventas WHERE id_venta = 2

-- EJERCICIO
-- Teniendo en cuenta la tabla Productos, realizar las siguientes consultas:
-- 1) Recuperar el id_producto, nombre y precio de la tabla Productos
-- 2) Recuperar los registros con los id_producto 44,45,46 y 49
-- 3) Recuperar los registros con precio mayor a 4000
-- 4) Recuperar el id_producto y precio de los productos con valor entre 1000 y 5000
-- 5) Eliminar los registros con los id_producto 50,51,52,53,54 y 55
-- 6) Recuperar los registros que empiecen con la letra "C"

-- 1)
SELECT id_producto, nombre, precio FROM Productos

-- 2)
SELECT * FROM Productos WHERE id_producto in (44,45,46,49)

-- 3)
SELECT * FROM Productos WHERE precio > 4000

-- 4)
SELECT id_producto, precio FROM Productos WHERE precio BETWEEN 1000 and 5000

-- 5)
DELETE FROM Productos WHERE id_producto in (50,51,52,53,54,55)

-- 6)
SELECT * FROM Productos WHERE nombre like 'c%'