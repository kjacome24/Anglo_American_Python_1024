### 1. Consultas Básicas con SELECT
```sql
-- Seleccionar todas las columnas de cada tabla
SELECT * FROM personajes;
SELECT * FROM planetas;
SELECT * FROM naves;
SELECT * FROM alianzas;
```

```sql
-- Seleccionar columnas específicas en vez de todas
SELECT nombre, año_nacimiento FROM personajes;
SELECT nombre, modelo FROM naves;
```

##### 2. Condicionales con WHERE

```sql
SELECT nombre FROM personajes WHERE id = 5;                -- Obtiene el nombre del personaje con ID 5
SELECT nombre, año_nacimiento FROM personajes WHERE año_nacimiento > 0; -- Personajes nacidos después de 0 BBY
```

```sql
-- Consultas con LIKE y comodines
SELECT * FROM personajes WHERE nombre LIKE '%e';           -- Personajes cuyo nombre termina en 'e'
SELECT * FROM personajes WHERE nombre NOT LIKE 'A%';       -- Personajes cuyo nombre no empieza con 'A'
select * from personajes where nombre like '%da%'          -- Personajes cuyo nombre incluye 'da'
```

### 3. Ordenamiento con ORDER BY

```sql
-- Ordenar personajes en orden alfabético
SELECT nombre FROM personajes ORDER BY nombre ASC;

-- Ordenar personajes por año de nacimiento de forma descendente
SELECT nombre, año_nacimiento FROM personajes ORDER BY año_nacimiento DESC;

-- Mostrar los tres planetas más poblados
SELECT * FROM planetas ORDER BY poblacion DESC LIMIT 3;

-- Mostrar dos naves en orden alfabético, saltando la primera
SELECT * FROM naves ORDER BY modelo ASC LIMIT 2 OFFSET 1;

```

### 4. Insertar Nuevos Registros con INSERT INTO
```sql
INSERT INTO planetas (nombre, region, poblacion) VALUES ('Lothal', 'Borde Exterior', 1000000);
INSERT INTO personajes (nombre, año_nacimiento, planeta_id, especie_id) VALUES ('Ahsoka Tano', 19, 8, 4);
```

### 5. Actualizar Registros con UPDATE

```sql
update personajes set nombre='Ahsoka Tano 2' where id=12;
UPDATE naves SET modelo = 'YT-1300 modificado' WHERE nombre = 'Millennium Falcon';
UPDATE planetas SET poblacion = 50000 WHERE nombre = 'Hoth';
```

##  6. Eliminar Registros con DELETE

```sql
delete from personajes where id=12;

```

## 7. Funciones Comunes en SQL

```sql
-- Calcular el promedio de año de nacimiento de los personajes
SELECT AVG(año_nacimiento) AS promedio_nacimiento FROM personajes WHERE año_nacimiento > 0;

-- Calcular los días entre las fechas de creación y actualización de planetas
SELECT DATEDIFF(updated_at, created_at) AS dias_entre_fechas FROM planetas;

-- Calcular la edad en años usando la fecha de nacimiento
SELECT DATEDIFF(CURDATE(), '1990-05-15') / 365 AS age_years;

```


### 8 . Agrupación con GROUP BY

```sql
-- Contar la cantidad de planetas en cada región
SELECT region, COUNT(id) AS total_planetas FROM planetas GROUP BY region;

-- Contar cuántos personajes pertenecen a cada planeta (por ID)
SELECT planeta_id, COUNT(*) AS total_personajes FROM personajes GROUP BY planeta_id;

-- Contar cuántos personajes pertenecen a cada especie (por ID)
SELECT especie_id, COUNT(*) AS total_personajes FROM personajes GROUP BY especie_id;

-- Contar cuántos personajes nacieron en cada año
SELECT año_nacimiento, COUNT(*) AS total_personajes FROM personajes GROUP BY año_nacimiento;

```



#### 9 inner join
```sql
-- Obtener todos los registros combinados de personajes y planetas (solo los que hacen match)
SELECT * FROM personajes JOIN planetas ON personajes.planeta_id = planetas.id;

-- Mostrar el nombre del personaje y el nombre del planeta
SELECT personajes.nombre AS personaje, planetas.nombre AS planeta
FROM personajes
JOIN planetas ON personajes.planeta_id = planetas.id;

-- Combinar personajes con planetas y especies
SELECT *
FROM personajes
JOIN planetas ON personajes.planeta_id = planetas.id
JOIN especies ON personajes.especie_id = especies.id;

-- Combinar personajes con planetas y especies usando clumnas especificas
select personajes.nombre,personajes.año_nacimiento, planetas.nombre as 'nombre_planeta', especies.nombre as 'especie'
from personajes join planetas on personajes.planeta_id = planetas.id
join especies on personajes.especie_id=especies.id;
```



### 10 lef join

```sql
-- query Original solo trae los registros que hacen match
SELECT personajes.nombre AS personaje, planetas.nombre AS planeta, alianzas.nombre AS alianza
FROM personajes
JOIN planetas ON personajes.planeta_id = planetas.id
JOIN alianzas ON personajes.id = alianzas.lider_id;
```

```sql
-- query despues con left join
SELECT personajes.nombre AS personaje, planetas.nombre AS planeta, alianzas.nombre AS alianza
FROM personajes
left JOIN planetas ON personajes.planeta_id = planetas.id
left JOIN alianzas ON personajes.id = alianzas.lider_id;
```