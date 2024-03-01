-- CLASE 4 EJERCICIOS
--1- Seleccionar todos los campos de la tabla Alumnos
Select * from Alumnos; -- OK
--2- Actualizar la direccion de "Juan Perez" nacido en 1995-05-10 a "Calle Uruguay 200"
select * from Alumnos where nombre = 'Juan' and apellido = 'Perez' 
and fecha_nac like '%1995-05-10%'
update Alumnos set direccion = 'Calle Uruguay 200' where ID_Alumno = 1
--3- Borrar el registro de "Maria Gonzalez"
select * from Alumnos where nombre = 'Maria' and apellido = 'Gonzalez'
delete from Alumnos where ID_Alumno = 2
--4- Seleccionar todos los alumnos nacidos en 1995
select * from Alumnos where fecha_nac like '%1995%'
select * from Alumnos where fecha_nac BETWEEN '1995-01-01' and '1995-12-31'
--5- Seleccionar los alumnos cuyo nombre empiece con "A"
select * from Alumnos where nombre like 'A%'
--6- Seleccionar los alumnos cuya direccion contenga "calle"
select * from Alumnos where direccion like '%calle%'
--7- Seleccionar los alumnos cuyo nombre este en la lista ("Juan", "Maria","Pedro")
select * from Alumnos where nombre in ('Juan','Maria','Pedro')
--8- Seleccionar los alumnos cuya fecha de nacimiento este entre '1990-01-01' y 
--'1995-01-01' y ordenarlos por fecha de nacimiento de forma descendente.
select * from Alumnos where fecha_nac BETWEEN '1990-01-01' and '1995-01-01' 
order by fecha_nac desc

-- CLASE 5 EJERCICIOS
--9. Seleccionar los alumnos cuya fecha de nacimiento sea mayor a '1990-01-01'
-- y tengan direccion en 'Calle lavalle'
SELECT * FROM Alumnos WHERE fecha_nac > '1990-01-01' AND direccion like '%Calle lavalle%'
--10. Seleccionar los alumnos cuyo nombre contenga la letra 'c'
SELECT * FROM Alumnos WHERE nombre like '%c%'
--11. Seleccionar los 10 alumnos mas jovenes
-- SELECT * FROM tabla WHERE condicion (o no) ORDER by campo (DESC o ASC) LIMIT numero
SELECT * FROM Alumnos ORDER by fecha_nac DESC LIMIT 10 -- LIMIT (Para que solo me muestre los 10 primeros)
--12. Seleccionar los 5 primeros alumnos ordenados alfabeticamente por apellido
SELECT * FROM Alumnos ORDER by apellido ASC LIMIT 5
--13. Actualizar la fecha de baja de 'Juan Perez' con domicilio en calle Florida a '2024-02-28'
select * from Alumnos where nombre = 'Juan' and apellido = 'Perez' 
and direccion like '%Florida%'
UPDATE Alumnos SET fecha_baja = '2024-02-28' WHERE id_alumno = 75
--14. Borrar los registros de los alumnos nacidos antes de '1970-01-01'
SELECT * FROM Alumnos WHERE fecha_nac < '1970-01-01'
DELETE FROM Alumnos WHERE fecha_nac < '1970-01-01'
--15. Seleciona los alumnos cuyo apellido termine con 'ez'
SELECT * FROM Alumnos WHERE apellido like '%ez'
--16. Seleccionar los alumnos cuya direccion no sea 'Avenida de Mayo'
SELECT * FROM Alumnos WHERE direccion not like '%Avenida de Mayo%'
--17. Seleccionar los alumnos cuyo nombre comience con 'M' o 'N'
SELECT * from Alumnos where nombre like 'M%' or nombre like 'N%'
--18. Seleccionar los alumnos cuyo nombre contiene exactamente 5 letras y su direccion no contiene 'Avenida'
SELECT * FROM Alumnos where nombre like '_____' AND direccion not like '%Avenida%'
--19. Seleccionar los 3 alumnos mas jovenes cuyo nombre empiece con 'L', ordenarlos
-- por fecha de nacimiento en orden ascendente
SELECT * FROM Alumnos where nombre like 'L%' ORDER by fecha_nac ASC LIMIT 3
--20. Seleccionar los alumnos cuyo nombre tiene mas de 6 letras y su fecha baja no esta establecida
SELECT * FROM Alumnos WHERE nombre like '%_______' and fecha_baja is NULL
SELECT * FROM Alumnos WHERE length(nombre) > 6 and fecha_baja is NULL -- Tambien se puede hacer asi con el length
