CREATE TABLE vacunaciones(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) UNIQUE NOT NULL, -- Nombre que no se pueda repetir y que no admita valores vacíos
    estado BOOL DEFAULT true, -- Estado que solo acepte bool [su valor por defeccto sea true]
    fecha_vencimiento DATE, -- Fecha_vencimeinto
    procedencia ENUM('USA', 'CHINA', 'RUSIA', 'UK'), -- Procedencia sus valores puede ser
    lote VARCHAR(10) -- Lote NO puede superar los 10 Caracteres
);

CREATE TABLE vacunatorios (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    latitud FLOAT,
    longitud FLOAT,
    direccion VARCHAR(200),
    horario_atencion VARCHAR(100),
    -- La llave foranea (FK Foreign Key) es la representacion de la relación ente la otra tabla e indicara todo su contenido
    -- representado por su id
    vacuna_id INT,
    FOREIGN KEY (vacuna_id) REFERENCES vacunas(id)
);

RENAME TABLE nuevas_vacunas TO vacunatorios;
RENAME TABLE vacunaciones TO vacunas;

-- DDL: Data Defition Lagunage => se usara para la defincion de donde se almacenra los datos de mi bd
-- Para renombrea una tabla con un nuevo nombre RENAME TABBLE valor_antigui TO nuevo_valor
-- CREAR TABLES | CEEAR DATABASE
-- DROP elimina la tabla y su contenido a diferencia 
-- DROP TABLE vacunatorios;
-- DROP DATABASE prueba;

DROP TABLE nuevas_vacunas;
-- Eliminara la columna de la tabla y perderemos todos los datos que hubiesen en ella
-- ALTER TABLE vacunatorios DROP COLUMN latitud

-- Agregara una nueva columna indicando el tipo de dato
-- No podemos agregar valores por defecto a los tipos de datos BLOB, TEXT, GEOMETRY o JASON
ALTER TABLE vacunatorios ADD COLUMN imagen VARCHAR(100) DEFAULT 'imagen.png' AFTER horario_atencion;
ALTER TABLE vacunas ADD COLUMN estado BOOL AFTER nombre;

-- RENAME COLUMN => renombra la columna
ALTER TABLE vacunatorios RENAME COLUMN imagen TO foto;

-- MODIFY COLUMN => cambiaar el tipo de datos y las configuraciones adicionales
-- NO podremos cambiar el TIPO DE DATO si ya hay información en esa columna y no corresponde con el nuevo tipo de dato
-- ALTER TABLE vacunatorios MODIFY COLUMN imagen UNIQUE NOT NULL;

-- Un vacunatorio podrá tener una sola vacuna pero una vacuna puede esta presente en varios vacunatorios
-- vacunas => vacunatorios

-- Solo funcion en MySQL y nos describira la tabla
DESC vacunatorios;


