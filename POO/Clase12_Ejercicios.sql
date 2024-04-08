--1. GROUP BY: Se utiliza en SQL para agrupar filas que tienen el mismo valor en una o mas columnas.
-- esto permite realizar operaciones de agregacion como sumar, contar o calcular promedio,
-- en cada grupo de filas.

-- SINTAXIS:
-- (Funcion_agregacion = suma, resta, promedio, max, min, count, etc)
	-- SELECT Columna1, Columna2, Funcion_agregacion(Columna) FROM Tabla GROUP BY Columna1, Columna2

-- Obtener el numero de ventas realizadas por cada vendedor
SELECT ID_Vendedor, count(*) as 'Cantidad de ventas' FROM Ventas GROUP BY ID_Vendedor

--2. HAVING: La clausula HAVING se utiliza junto con GROUP BY para filtrar grupos de filas
-- basandose en una condicion. Es el WHERE pero para GROUP BY y se aplica despues de agrupar filas
	-- SELECT Columna1, Columna2, Funcion_agregacion(Columna) FROM Tabla GROUP BY Columna1, Columna2
	-- HAVING <Condicion>

-- Obtener el numero de ventas realizadas por cada vendedor que haya realizado mas de 5 ventas
SELECT ID_Vendedor, count(*) as Cantidad_Ventas FROM Ventas
GROUP BY ID_Vendedor
HAVING count(*) > 5 -- o
HAVING Cantidad_Ventas > 5

--3. JOIN: La clausula JOIN se utiliza para combinar filas de dos o mas tablas basandose en una
-- condicion relacionada entre ellas.
	-- SELECT columna1, Columna2, etc
	-- FROM Tabla1
	-- JOIN Tabla2
	-- ON Condicion_union

-- Obtener el nombre del vendedor y el nombre del cliente para cada venta
SELECT vd.ID_Vendedor, vd.Nombre as 'Vendedor', cl.Nombre as 'Cliente'
FROM Ventas v
JOIN Vendedores vd
ON v.ID_Vendedor = vd.ID_Vendedor
JOIN Clientes cl
ORDER BY 1 -- 1 es la columna, tambien se puede poner (ORDER BY vd.ID_Vendedor)

--4. Subconsultas: Es una consulta anidada dentro de otra consulta SQL, se puede usar en varias clausulas
-- como SELECT, FROM, WHERE, HAVING o JOIN
	-- SELECT Columnas
	-- FROM Tabla
	-- WHERE Columna in (SELECT FROM Otra_Tabla WHERE <Condicion>)

-- Obtener el ID del vendedor que ha realizado la venta con el precio mas alto.
SELECT ID_Vendedor
FROM Ventas
WHERE Precio = (SELECT max(Precio) FROM Ventas)
-- Tambien se puede hacer asi, pero la mejor forma es con el max
SELECT ID_Vendedor
FROM Ventas
ORDER BY Precio DESC limit 1

-- Obtener el nombre de la sucursal donde se realizo la venta con el precio mas bajo
SELECT ID_Sucursal, Nombre
FROM Sucursales
	WHERE ID_Sucursal in (
		SELECT ID_Sucursal FROM Ventas
		WHERE Precio = (SELECT min(Precio) FROM Ventas)
	)
-- Obtener el ID del auto mas caro vendido en cada sucursal
SELECT ID_Automovil, max(Precio), ID_Sucursal FROM Ventas
GROUP BY ID_Sucursal
-- Obtener el ID del cliente que ha realizado la compra mas reciente
SELECT ID_Cliente, Fecha_compra FROM Ventas
WHERE Fecha_compra = (SELECT max(Fecha_compra) FROM ventas)
-- Obtener el nombre del cliente que realizo la compra mas cara
SELECT Nombre
FROM Clientes
WHERE ID_Cliente in (
	SELECT ID_Cliente
	FROM Ventas
	WHERE Precio in (SELECT max(Precio) FROM Ventas)
	)
-- Obtener el nombre del cliente y la fecha de compra para cada venta realizada,
-- incluyendo la marca y modelo del auto vendido
SELECT c.Nombre, v.Fecha_compra, a.Marca, a.Modelo
FROM Ventas v
JOIN Clientes c ON v.ID_Cliente = c.ID_Cliente
JOIN Automoviles a ON v.ID_Automovil = a.ID_Automovil
