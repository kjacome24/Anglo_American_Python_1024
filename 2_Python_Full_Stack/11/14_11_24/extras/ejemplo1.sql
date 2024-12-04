-- ¿Qué consulta ejecutarías para obtener todos los países que hablan español? Tu consulta debe devolver el nombre del país, el idioma y el porcentaje de habla del idioma.  Tu consulta debe ordenar el resultado por porcentaje de habla del idioma en orden descendente. (1)

select paises.nombre,idiomas.idioma,idiomas.porcentage from paises
left join idiomas on paises.id= idiomas.pais_id
where idiomas.idioma="Español";

-- ¿Qué consulta ejecutarías para mostrar el número total de ciudades de cada país?  Tu consulta debe devolver el nombre del país, el idioma y el número total de ciudades. Tu consulta debe ordenar el resultado por el número de ciudades en orden descendente. (3)
select paises.nombre,count(ciudades.nombre) as 'numero_de_ciudades' from paises
left join ciudades on paises.id=ciudades.pais_id group by paises.nombre order by numero_de_ciudades desc;
 
-- ¿Qué consulta ejecutarías para obtener todos ciudades de Chile con una población mayor a 200,000? Tu consulta debe ordenar el resultado por población en orden descendente. (1)
SELECT ciudades.nombre AS ciudad, ciudades.poblacion 
FROM ciudades
JOIN paises ON ciudades.pais_id = paises.id
WHERE paises.nombre = "Chile" AND ciudades.poblacion > 200000
ORDER BY ciudades.poblacion DESC;

-- ¿Qué consulta ejecutarías para obtener todos los idiomas en cada país con un porcentaje de habla mayor a 89%? Tu consulta debe ordenar el resultado por porcentaje de habla en orden descendente. 
SELECT paises.nombre AS pais, idiomas.idioma, idiomas.porcentage 
FROM paises
JOIN idiomas ON paises.id = idiomas.pais_id
WHERE idiomas.porcentage > 89
ORDER BY idiomas.porcentage DESC;

-- ¿Qué consulta ejecutarías para obtener todos los países con un área de superficie menor a 501 y población mayor a 100,000?
select nombre,area_superficie,poblacion  from paises where area_superficie<501 and poblacion> 100000;

-- ¿Qué consulta ejecutarías para obtener países en el que el tipo de gobierno es República, un capital superior a 2000 y una esperanza de vida mayor a 78 años?  (1)
SELECT nombre AS pais, tipo_gobierno, capital, esperanza_vida
FROM paises
WHERE tipo_gobierno = "República" AND capital > 2000 AND esperanza_vida > 78;

-- ¿Qué consulta ejecutarías para obtener todas las ciudades de Colombia dentro del distrito de Valle con una población mayor a 200,000 habitantes?  La consulta debe devolver el nombre del país, el nombre de la ciudad, el distrito y la población.  (2)
SELECT paises.nombre AS pais, ciudades.nombre AS ciudad, ciudades.distrito, ciudades.poblacion
FROM ciudades
JOIN paises ON ciudades.pais_id = paises.id
WHERE paises.nombre = "Colombia" AND ciudades.distrito = "Valle" AND ciudades.poblacion > 200000;

-- ¿Qué consulta ejecutarías para resumir el número de países en cada región? Tu consulta debe mostrar el nombre de la región y el número de países. Además, debe ordenar el resultado por el número de países en orden descendente. (2)-- ¿Qué consulta ejecutarías para obtener todos los países que hablan español? Tu consulta debe devolver el nombre del país, el idioma y el porcentaje de habla del idioma.  Tu consulta debe ordenar el resultado por porcentaje de habla del idioma en orden descendente. (1)

SELECT region, COUNT(*) AS numero_de_paises
FROM paises
GROUP BY region
ORDER BY numero_de_paises DESC;
