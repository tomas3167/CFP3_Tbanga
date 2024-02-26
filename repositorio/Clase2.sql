-- DDL
-- CREATE (creo una tabla)
CREATE TABLE if not EXISTS Alumnos (
	id_alumno INTEGER,
	nombre TEXT(20),
	edad INTEGER
	);

-- DROP (Elimino una tabla o base de datos)
DROP TABLE Alumnos;
 
-- punto y coma(;) significa que termina una accion o funcion

-- ALTER (Editar columnas de una tabla existente)
ALTER TABLE Alumnos	add COLUMN direccion TEXT

-- ALTER con DROP
ALTER TABLE Alumnos DROP COLUMN edad

-- ALTER con RENAME
ALTER TABLE Alumnos RENAME COLUMN direccion to dirección

-- DML
CREATE TABLE Productos (
	id_producto INTEGER PRIMARY KEY AUTOINCREMENT, --AUTOINCREMENT significa que va aumentado de a 1 como un contador
	nombre TEXT(30) NOT NULL,
	precio INTEGER NOT NULL,
	peso REAL NOT NULL, --REAL significa tipo numerico flotante
	fecha_alta datetime NOT NULL,
	fecha_baja datetime
	);

-- INSERT (Permite insertar filas (registros) en una tabla
INSERT INTO Productos (nombre, precio, peso, fecha_alta, fecha_baja) VALUES
  ('Tornillos M6x10 (100 unidades)', 500, 0.5, '2024-02-22', NULL),
  ('Martillo de carpintero', 1200, 1.0, '2024-02-21', NULL),
  ('Cinta métrica 5 metros', 350, 0.2, '2024-02-20', NULL),
  ('Nivel láser autonivelante', 4500, 1.5, '2024-02-19', NULL),
  ('Escalera telescópica 4x4', 8000, 20.0, '2024-02-18', NULL),
  ('Caja de herramientas 20 compartimentos', 2500, 2.5, '2024-02-17', NULL),
  ('Llave inglesa ajustable', 800, 0.8, '2024-02-16', NULL),
  ('Destornillador Phillips PH2', 300, 0.1, '2024-02-15', NULL),
  ('Alicate de corte diagonal', 500, 0.3, '2024-02-14', NULL),
  ('Gafas de seguridad transparentes', 200, 0.1, '2024-02-13', NULL),
  ('Guantes de trabajo talla L', 400, 0.2, '2024-02-12', NULL),
  ('Casco de seguridad con visera', 1500, 0.8, '2024-02-11', NULL),
  ('Mascarilla antipolvo FFP2', 100, 0.1, '2024-02-10', NULL),
  ('Cinta adhesiva de embalaje 50m', 400, 0.5, '2024-02-09', NULL),
  ('Film plástico transparente 5m x 2m', 600, 1.0, '2024-02-08', NULL),
  ('Bolsas de basura negras 100 unidades', 300, 0.5, '2024-02-07', NULL),
  ('Palet de madera europeo 80x120cm', 1200, 20.0, '2024-02-06', NULL),
  ('carretilla de mano plegable', 2500, 5.0, '2024-02-05', NULL),
  ('Transpaleta manual 2500kg', 4000, 50.0, '2024-02-04', NULL);

-- DELETE FROM (Permite eliminar filas de una tabla)
DELETE FROM Productos WHERE id_producto = 9

-- UPDATE (Actualizar informacion de una tabla)
UPDATE Productos set precio = 1500 where id_producto = 3

-- SELECT (Seleccionar o recuperar una lista de campos para verla)
-- SELECT "COLUMN1, column2" FROM "nombre_Tabla" WHERE "criterio de seleccion"
SELECT * FROM Productos -- El * significa todo, en este caso todas las columnas
SELECT id_producto, nombre FROM Productos
SELECT * FROM Productos WHERE precio < 1000

-- Consulta para traer precios distintos de 400
SELECT nombre,precio,peso from Productos where precio != 400

-- IN
UPDATE Productos set precio = 5000 WHERE id_producto in (7,9,12)
-- En vez de hacer esto:
 --UPDATE Productos set precio = 5000 WHERE id_producto = 7
 --UPDATE Productos set precio = 5000 WHERE id_producto = 9
 --UPDATE Productos set precio = 5000 WHERE id_producto = 12
SELECT * from Productos WHERE id_producto in (3,8,13,15,7)
delete from Productos where id_producto in (1,17)

-- EJERCICIOS:
-- 1) Mostrar los productos con precio mayor a 1000 y peso mayor a 1
SELECT * from Productos where precio > 1000 AND peso > 1
-- 2) Mostrar los productos con precio distinto a 1000
SELECT * from Productos where precio != 1000
-- 3) Mostrar id_producto, nombre y precio de los productos con el precio mayor a 3000
SELECT id_producto, nombre, precio from Productos where precio > 3000
-- 4) Mostrar los productos con precio entre 1000 y 5000
SELECT * from Productos where precio > 1000 AND precio < 5000
SELECT * from Productos where precio BETWEEN 1000 and 5000

-- like (Permite obtener de manera busqueda los datos que cumplan la condicion)
SELECT * from Productos where nombre like '%martillo%' 
-- hay que poner ' y los % significa que importa lo que este adelante o detras de la palabra
SELECT * from Productos where nombre like '%s%'
SELECT * from Productos where precio like '3%'