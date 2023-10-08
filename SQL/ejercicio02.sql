/*Ejercicio 2
1. Crea una base de datos llamada "MiBaseDeDatos".
*/
CREATE DATABASE MiBaseDeDatos;
/*
2. Crea una tabla llamada "Usuarios" con las columnas: "id" (entero, clave
primaria), "nombre" (texto) y "edad" (entero).
*/
CREATE TABLE IF NOT EXISTS Usuarios (
	id int PRIMARY KEY,
	nombre VARCHAR(255),
	edad INT
)
/*
3. Inserta dos registros en la tabla "Usuarios".
*/
INSERT INTO public.usuarios
VALUES(1, 'Quim', 20),(2, 'Pablo', 34)
/*
4. Actualiza la edad de un usuario en la tabla "Usuarios"
*/
UPDATE public.usuarios
SET edad = 29
WHERE id = 2;
/*
5. Elimina un usuario de la tabla "Usuarios"
*/
DELETE FROM public.usuarios
WHERE id = 2;
/*
1. Crea una tabla llamada "Ciudades" con las columnas: "id" (entero, clave
primaria), "nombre" (texto) y "pais" (texto).
*/
CREATE TABLE IF NOT EXISTS Ciudades(
	id int PRIMARY KEY,
	nombre VARCHAR(255),
	pais VARCHAR(255)
)
/*
2. Inserta al menos tres registros en la tabla "Ciudades".
*/
INSERT INTO public.ciudades
VALUES(1,'Barcelona','España'),(2,'Paris', 'Francia'),(3,'Berlín','Alemania')
/*
3. Crea una foreign key en la tabla "Usuarios" que se relacione con la columna "id"
de la tabla "Ciudades".
*/
ALTER TABLE public.usuarios
ADD CONSTRAINT fk_ciudades
FOREIGN KEY (id) REFERENCES ciudades(id);
/*
4. Realiza una consulta que muestre los nombres de los usuarios junto con el
nombre de su ciudad y país (utiliza un LEFT JOIN).
*/

/*
5. Realiza una consulta que muestre solo los usuarios que tienen una ciudad
asociada (utiliza un INNER JOIN).
*/
SELECT ciudades.nombre, usuarios.nombre FROM public.usuarios
INNER JOIN public.ciudades ON usuarios.id = ciudades.id;