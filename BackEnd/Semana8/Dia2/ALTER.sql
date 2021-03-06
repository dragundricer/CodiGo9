use codigo9;
show tables;
# PARA HACER UNA MODIFICACION EN UNA TABLA SE USA EL COMANDO ALTER TABLE
# PARA AGREGAR UNA COLUMNA SE USA EL COMANDO ADD COLUMN
ALTER TABLE EMPLEADOS ADD COLUMN SALARIO INT AFTER EMP_NOMBRE;
SELECT * FROM EMPLEADOS;
# MODIFY COLUMN => MODIFICA UNA COLUMNA YA CREADA PARA CAMBIAR SU TIPO DE 
# DATO
ALTER TABLE EMPLEADOS MODIFY COLUMN SALARIO FLOAT(6,2);
# DROP COLUMN => SIRVE PARA ELIMINAR UNA COLUMNA SIEMPRE Y CUANDO NO SEA
# PK Y TENGA HERENCIA
ALTER TABLE EMPLEADOS DROP COLUMN SALARIO;

# PARA CREAR UNA FK
ALTER TABLE EMPLEADOS ADD CONSTRAINT FK_1 FOREIGN KEY (DEP_ID) REFERENCES 
DEPARTAMENTO(ID_DEP); 
# PARA MODIFICAR EL AUTO_INCREMENT (QUE POR DEFECTO ES 1)
ALTER TABLE EMPLEADOS AUTO_INCREMENT = 100;