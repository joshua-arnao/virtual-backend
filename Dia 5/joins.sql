-- JOINS
-- Es la manera de ingresar desde una tabla hacia otra medainte una col en común
USE prueba;
-- El uso de los joins solamente se podrá realizar en el bloque de FROM devuelven todas las colunas de la tabla vacunatios haciendo una intersección
-- con la tanla vacunas en la que sea igual a col)vacunatorio) vacuna_id = (vacunas)id
SELECT *
FROM vacunatorios INNER JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id
WHERE vacuna_id = 1;

-- LEFT JOIN
-- Traera todo el contenido de la tabla de la izquiera y adicionalmente el contenido de la interseccion
SELECT *
FROM vacunatorios LEFT JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id;

-- RIGHT JOIN
-- Traera todo el contenido de la tabla de la derecha y adicionalmente el contedio de intesección con la tabla de la izquier
SELECT *
FROM vacunatorios RIGHT JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id;

INSERT INTO vacunatorios (nombre, latitud, longitud, direccion, horario_atencion, foto, vacuna_id) VALUES
						 ('POSTA JOSE GALVEZ', 14.26598, 32.2569, 'AV. EL SOL 755', 'LUN-VIE 15:00 22:00', null, null);

-- Si se usa en la clausua WHERE o en el SELECT una columna ambigua (que se repite el mismo nombre) hay que especificar de que tabla hablamos
SELECT *
FROM vacunatorios JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id
WHERE vacunas.nombre = 'Pfizer';

-- Para color un alias se usa AS FROM VACUNATORIOS AS <ALIAS> ON

-- 1. Devolver todos los vacunatorioS en los cuales la vacuna sea Sinopharm y su horario de atencion sea de LUN-VIE
SELECT *
FROM vacunatorios LEFT JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id
WHERE vacunas.nombre = 'SINOPHARM' 
AND vacunatorios.horario_atencion LIKE '%LUN-VIE%';

-- 2. Devolver solamente las vacunas cuyo vacunatorio este ubicado entre la latitud -5.00 y 10.00 IN()
SELECT vacunas.nombre
FROM vacunatorios LEFT JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id
WHERE latitud BETWEEN -5 AND 10;

-- 3. Devolver todas las vacunas que no tengan vacunatorio y solamente su procedencia y nombre
SELECT procedencia, vacunas.nombre
FROM vacunatorios RIGHT JOIN vacunas ON vacunatorios.vacuna_id = vacunas.id
WHERE vacuna_id IS NULL;