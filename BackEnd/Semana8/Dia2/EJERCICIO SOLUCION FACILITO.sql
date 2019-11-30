CREATE DATABASE IF NOT EXISTS ALMACEN;
USE ALMACEN;

CREATE TABLE PRODUCTOS(
PROD_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
PROD_DESC VARCHAR(50),
PROD_PREC DECIMAL(5,2)
);
CREATE TABLE ALMACEN(
ALMA_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
ALMA_DESC VARCHAR(50)
);
CREATE TABLE ALMA_PROD(
ALMA_PROD_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
ALMA_ID INT,
PROD_ID INT,
FOREIGN KEY (ALMA_ID) REFERENCES ALMACEN(ALMA_ID),
FOREIGN KEY (PROD_ID) REFERENCES PRODUCTOS(PROD_ID)
);
CREATE TABLE CLIENTE(
CLI_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
CLI_NOMB VARCHAR(50),
CLI_DIR VARCHAR(50)
);
CREATE TABLE CABECERA_COMPROBANTE(
CAB_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
CAB_FECHA DATETIME,
CLI_ID INT,
FOREIGN KEY (CLI_ID) REFERENCES CLIENTE(CLI_ID)
);
CREATE TABLE CUERPO_COMPROBANTE(
CUERPO_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
CUERPO_CANT DECIMAL(4,2),
CUERPO_TOTAL DECIMAL(5,2),
PROD_ID INT,
CAB_ID INT,
FOREIGN KEY (PROD_ID) REFERENCES PRODUCTOS(PROD_ID),
FOREIGN KEY(CAB_ID) REFERENCES CABECERA_COMPROBANTE(CAB_ID)
);
 
 SELECT CABECERA.CAB_ID, CLIENTE.CLI_NOMB AS 'NOMBRE CLIENTE', CLIENTE.CLI_DIR AS 'DIRECCION CLIENTE',
 CUERPO.CUERPO_CANT AS 'CANTIDAD', PRODUCTOS.PROD_DESC AS 'NOMBRE PRODUCTO', PRODUCTOS.PROD_PREC AS 'PRECIO UNITARIO',
 CUERPO.CUERPO_TOTAL AS 'TOTAL'
 FROM CABECERA_COMPROBANTE AS CABECERA INNER JOIN CUERPO_COMPROBANTE AS CUERPO ON
 CABECERA.CAB_ID = CUERPO.CAB_ID INNER JOIN CLIENTE ON CABECERA.CLI_ID = CLIENTE.CLI_ID INNER JOIN
 PRODUCTOS ON CUERPO.PROD_ID=PRODUCTOS.PROD_ID;