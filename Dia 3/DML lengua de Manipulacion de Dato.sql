USE prueba;

-- Sub parte de SQL:
-- DML: Data Manipulation Language (Lenguage de manipulación de Datos)
-- Se utiliza para la manipulación de la información dentro de una base de datos
-- INSERT, SELECT, UPDATE, DELETE

INSERT INTO clientes (nombre, documento, tipo_documento, estado) VALUES
					('Joshua','74123050','DNI', true),
                    
INSERT INTO clientes (nombre, documento, tipo_documento, estado) VALUES
                    ('Omaira','7898213','RUC', false),
                    ('Fabian','45632132','DNI', true);
                    
                    
-- SELECT: sirve para visualizar la información de una determinada tabla o tablas
-- SELECT col1, col2, ... FROM tabla;
SELECT nombre, documento FROM clientes;

-- si queremos ver todas las columnas de esa tabla o tablas se usa SELECT * FROM clientes
SELECT * FROM clientes;

-- Para filtrar una base de datos se usa WHERE col_nombre = valor (< > >= <=)
SELECT * FROM clientes WHERE documento = '74123050';

SELECT * FROM clientes WHERE documento = '74123050' AND nombre='Fabian';
                    
SELECT * FROM clientes WHERE documento = '74123050' OR nombre='Omaira';

SELECT * FROM clientes WHERE tipo_documento = 'DNI' AND estado = true;

-- SE usa LIKE para buscar las letras de una palabra %abc = esta al final, abc%=esta al incio, %abc% = esta en algún lado y abc%o = empeiza con y termina en O
SELECT * FROM clientes WHERE nombre LIKE '%Jos%';

-- UPDATE sirve para actualizar uno o varios registros de una determinada tabla
UPDATE clientes SET nombre = 'Sandy', documento = '44432512' WHERE id = 15;

-- Para desactivar el modo seguro
-- SET SQL_SAFE_UPDATES = false;

DELETE FROM clientes WHERE id = 1;
