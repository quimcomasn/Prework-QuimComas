/*
1. Crea una tabla llamada "Pedidos" con las columnas: "id" (entero, clave
primaria), "id_usuario" (entero, clave foránea de la tabla "Usuarios") y
"id_producto" (entero, clave foránea de la tabla "Productos").
*/
CREATE TABLE IF NOT EXISTS Pedidos (
    id INT PRIMARY KEY NOT NULL,
    id_usuario INT, 
    id_producto INT,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
    FOREIGN KEY (id_producto) REFERENCES productos(id)
)
/*
2. Inserta al menos tres registros en la tabla "Pedidos" que relacionen usuarios con
productos.
*/
INSERT INTO public.pedidos
VALUES (1,1,1),(2,2,3),(3,3,2)
/*
3. Realiza una consulta que muestre los nombres de los usuarios y los nombres de
los productos que han comprado, incluidos aquellos que no han realizado
ningún pedido (utiliza LEFT JOIN y COALESCE).
*/
SELECT usuarios.nombre, COALESCE(productos.nombre, 'No hay ningun pedido') AS n_producto FROM public.usuarios 
LEFT JOIN public.pedidos ON usuarios.id = pedidos.id
LEFT JOIN public.productos ON pedidos.id = productos.id;
/*
4. Realiza una consulta que muestre los nombres de los usuarios que han
realizado un pedido, pero también los que no han realizado ningún pedido
(utiliza LEFT JOIN)
*/
SELECT usuarios.nombre FROM public.usuarios
LEFT JOIN public.pedidos ON usuarios.id = pedidos.id
WHERE pedidos.id IS NOT NULL OR pedidos.id IS NULL;
/*
5. Agrega una nueva columna llamada "cantidad" a la tabla "Pedidos" y actualiza
los registros existentes con un valor (utiliza ALTER TABLE y UPDATE)
*/
ALTER TABLE public.pedidos
ADD COLUMN cantidad INT;
UPDATE public.pedidos
SET cantidad = 1;