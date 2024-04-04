--2 Cuantos clientes hay en nuestra base de datos
SELECT count(*) as 'Total de clientes' FROM Clientes
--3 Cuantos autos en total
SELECT count(*) as 'Total de autos' from Automoviles
--4 Cuantos vendedores tienen menos de 30 años?
SELECT count(*) as 'Vendedores menores a 30' FROM Vendedores WHERE Edad < 30
--5 Cuantos clientes tienen entre 20 y 35 años?
SELECT count(*) as 'Clientes entre 20 y 35 años' FROM Clientes WHERE Edad BETWEEN 20 and 35
--6 Cuantos automoviles hay en la sucursal 1?
SELECT count(*) as 'Autos de la sucursal 1' FROM Automoviles WHERE ID_Sucursal = 1
--7 Cuantas sucursales tienen mas de 2 autos?
--
--8 Cuantos automoviles tienen transmision automatica
SELECT count(*) as 'Autos automaticos' from Automoviles WHERE Transmision like 'Aut%'
--9 clientes tienen entre 25 y 45 años inclusivo?
SELECT count(*) as Clientes_25_40 FROM Clientes WHERE Edad BETWEEN 25 and 45
--10 Autos de color rojo
SELECT count(*) as 'Autos de color rojo' FROM Automoviles WHERE color like 'red'

--Clausulas (as, sum, min, max, avg) sum = suma, avg = promedio
--1 Edad maxima de los Vendedores
SELECT max(Edad) as 'Edad maxima' from Vendedores
--2 Cual es el año del auto mas antiguo
SELECT min(año) FROM Automoviles
--3 Suma total de las edad de los Clientes
SELECT sum(Edad) as Edad_Total from Clientes
--4 Cual es el promedio de edad de todos los vendedores
SELECT avg(Edad) as 'Promedio de las edades' from Vendedores
--5 El año mas reciente de los autos
SELECT max(Año) From Automoviles
-- Auto mas antiguo de la sucursal 1
SELECT min(Año) as 'Auto mas antiguo de la sucursal 1' FROM Automoviles WHERE ID_Sucursal = 1
-- Promedio de años de los autos de la sucursal 4
SELECT avg(Año) as 'Prom auto' FROM Automoviles WHERE ID_Sucursal = 4
-- Auto mas antiguo de la marca Ford
SELECT min(Año) as 'Auto mas antiguo de Ford' FROM Automoviles WHERE Marca = 'Ford'
-- Promedio de edad de los Vendedores de la sucursal 3
SELECT avg(Edad) Prom_edad FROM Vendedores WHERE ID_Sucursal = 3
-- Año mas reciente de los Automoviles de color verde
SELECT max(Año) Auto_Año_Reciente FROM Automoviles WHERE Color = 'Green'
-- Subconsultas
-- Cual es el modelo del automovil mas antiguo
SELECT Modelo as 'Modelo del auto mas antiguo' FROM Automoviles
WHERE Año = (SELECT min(Año) from Automoviles)
-- Cual es el nombre del empleado mas joven de las sucursales
SELECT Nombre as 'Empleado mas joven' FROM Vendedores WHERE Edad = (SELECT min(Edad) FROM Vendedores) limit 1

