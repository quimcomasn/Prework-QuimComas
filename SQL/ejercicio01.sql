/* Ejercicio 1
1. Crear una tabla llamada "Clientes" con las columnas: id (entero, clave primaria), nombre (texto) y email (texto).
*/
CREATE TABLE IF NOT EXISTS Clientes(
	id int PRIMARY KEY,
	nombre VARCHAR(255),
	email VARCHAR(255)
)
/*
2. Insertar un nuevo cliente en la tabla "Clientes" con id=1, nombre="Juan" y
email="juan@example.com".
*/
INSERT INTO public.clientes (id, nombre, email)
VALUES(1,'Juan','juan@example.com')
/*
3. Actualizar el email del cliente con id=1 a "juan@gmail.com".
*/
UPDATE public.clientes
SET email = 'juan@gmail.com'
WHERE id = 1;
/*
4. Eliminar el cliente con id=1 de la tabla "Clientes".
*/
DELETE FROM public.clientes
WHERE id = 1;
/*
5. Crear una tabla llamada "Pedidos" con las columnas: id (entero, clave primaria),
cliente_id (entero, clave externa referenciando a la tabla "Clientes"), producto (texto) y cantidad (entero).
*/
CREATE TABLE IF NOT EXISTS Pedidos(
	id INT PRIMARY KEY, 
	cliente_id INT,
	producto VARCHAR(255),
	cantidad INT,
	FOREIGN KEY (cliente_id) REFERENCES clientes(id)
)
/*
6. Insertar un nuevo pedido en la tabla "Pedidos" con id=1, cliente_id=1,
producto="Camiseta" y cantidad=2. 
*/
INSERT INTO public.pedidos (id, cliente_id, producto,cantidad)
VALUES(1,1,'Camiseta',2)
/*
7. Actualizar la cantidad del pedido con id=1 a 3.
*/
UPDATE public.pedidos
SET cantidad = 3
WHERE id=1;
/*
8. Eliminar el pedido con id=1 de la tabla "Pedidos".
*/
DELETE FROM public.pedidos
WHERE id = 1;
/*
9. Crear una tabla llamada "Productos" con las columnas: id (entero, clave
primaria), nombre (texto) y precio (decimal).
*/

/*
10. Insertar varios productos en la tabla "Productos" con diferentes valores.
*/

/*
11. Consultar todos los clientes de la tabla "Clientes".
*/

/*
12. Consultar todos los pedidos de la tabla "Pedidos" junto con los nombres de los
clientes correspondientes.
*/

/*

*/

/*

*/

/*

*/