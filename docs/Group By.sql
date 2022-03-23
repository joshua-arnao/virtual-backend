USE recetario;
-- LIMIT da la pauta de la cantidad de elementos que filtrara
-- OFSET se salta la cantidad de elementos que se le indica
SELECT * FROM recetas LIMIT 3 OFFSET 3;

-- COUNT() para sabar cuantos elementos tenemos en un tabla indicado que coumna usamos como contador
SELECT COUNT(*) FROM recetas;

-- GROUP BY se utiliza para clasificar enfunción del valor de la columna
-- Esto es obligatorio cuando se usa un AG(AGGREGATE FUNCTION) en los motores de bd POSTGRESQL, MSSQL, ORACLE(algunas)
SELECT COUNT(dificultad), dificultad FROM recetas GROUP BY dificultad;

SELECT COUNT(dificultad), dificultad FROM recetas GROUP BY dificultad, nombre;