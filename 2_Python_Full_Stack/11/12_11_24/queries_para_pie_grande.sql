-- Describe la estructura de cada tabla:
DESC usuarios;
DESC avistamientos;
DESC no_creo;


-- Utilizamos comando comodin para ver todas las columnas. 
SELECT * FROM usuarios;
SELECT * FROM avistamientos;


-- Obtiene solo las columnas id, nombres, apellidos y email de la tabla usuarios
SELECT id, nombres, apellidos, email FROM usuarios;

-- Obtiene solo las columnas ubicacion, descripcion y fecha_avistamiento de avistamientos
SELECT ubicacion, descripcion, fecha_avistamiento FROM avistamientos;


-- Inserta un nuevo usuario en la tabla usuarios
INSERT INTO usuarios (nombres, apellidos, email, password) 
VALUES ('Renata', 'Fernandez', 'rfrenandez@codingdojo.la', '123456');

-- Inserta un nuevo avistamiento en la tabla avistamientos
INSERT INTO avistamientos (ubicacion, descripcion, numero_de_pie_grandes, fecha_avistamiento, usuario_id) 
VALUES ('Bosque Nacional', 'Avistamiento cerca del lago', 3, '2024-11-10 14:30:00', 1);


-- Uso de comando count par aidentificar el numero de registros de una tabla
SELECT COUNT(*) FROM usuarios;


-- Conteo de promedio de numero de piegrandes vistos en los encuentros
select AVG(numero_de_pie_grandes) FROM avistamientos;


-- Uso de funcion group by para contar el numero de registros por cantidad de pie grandes
select numero_de_pie_grandes,count(*) from avistamientos group by numero_de_pie_grandes;

-- Contar Avistamientos por Descripción y Promedio de Criaturas Observadas:
SELECT descripcion, AVG(numero_de_pie_grandes) AS promedio_criaturas, COUNT(*) AS total_avistamientos
FROM avistamientos
GROUP BY descripcion;




-- Listar Todos los Avistamientos con Columnas Específicas:


SELECT id, ubicacion, descripcion, fecha_avistamiento FROM avistamientos;

-- Contar Cuántos Usuarios No Creen en Cada Avistamiento:

SELECT avistamiento_id, COUNT(usuario_id) AS total_no_creo
FROM no_creo
GROUP BY avistamiento_id;


-- Promedio de Criaturas Observadas en Todos los Avistamientos:
SELECT AVG(numero_de_pie_grandes) AS promedio_criaturas
FROM avistamientos;


-- Contar Avistamientos Reportados por Cada Usuario:
SELECT usuario_id, COUNT(*) AS total_avistamientos
FROM avistamientos
GROUP BY usuario_id;


-- Insertar Nuevos Registros y Verificar Resultados:
-- Inserta algunos nuevos usuarios y avistamientos, y luego ejecuta SELECT * para verificar los nuevos registros.

-- Agregar un nuevo usuario
INSERT INTO usuarios (nombres, apellidos, email, password) 
VALUES ('Carlos', 'Perez', 'cperez@codingdojo.la', 'abcdef');

-- Agregar un nuevo avistamiento
INSERT INTO avistamientos (ubicacion, descripcion, numero_de_pie_grandes, fecha_avistamiento, usuario_id) 
VALUES ('Montaña Nevada', 'Dos criaturas observadas en la nieve', 2, '2024-11-12 16:45:00', 2);

