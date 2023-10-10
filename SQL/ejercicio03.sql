/* Ejercicios 3
1. Crea una tabla llamada "Productos" con las columnas: "id" (entero, clave
primaria), "nombre" (texto) y "precio" (numérico).
*/
CREATE TABLE IF NOT EXISTS Productos (
	id INT PRIMARY KEY,
	nombre VARCHAR(255),
	precio NUMERIC
)
/*
2. Inserta al menos cinco registros en la tabla "Productos".
*/
INSERT INTO public.productos
VALUES
    (1, 'Rueda', 100),
    (2, 'Volante', 45),
    (3, 'Ambientador', 8),
    (4, 'Funda Volante', 12),
    (5, 'Alfombrilla', 25)
/*
3. Actualiza el precio de un producto en la tabla "Productos".
*/
UPDATE public.productos
SET precio = 50
WHERE ID = 2;
/*
4. Elimina un producto de la tabla "Productos".
*/
DELETE FROM public.productos
WHERE ID = 5;
/*
5. Realiza una consulta que muestre los nombres de los usuarios junto con los
nombres de los productos que han comprado (utiliza un INNER JOIN con la
tabla "Productos").
*/
SELECT usuarios.nombre, productos.nombre FROM public.usuarios
INNER JOIN public.productos ON usuarios.id = productos.id;

