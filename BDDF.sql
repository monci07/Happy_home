INSERT INTO `tipospropiedad`(`tipo`) VALUES ('Casa');
INSERT INTO `tipospropiedad`(`tipo`) VALUES ('Departamento');
INSERT INTO `tipospropiedad`(`tipo`) VALUES ('Terreno');
INSERT INTO `tipospropiedad`(`tipo`) VALUES ('Local C.');
INSERT INTO `tipospropiedad`(`tipo`) VALUES ('Bodega');
INSERT INTO `tipospropiedad`(`tipo`) VALUES ('Edificio');

DELIMITER $$
CREATE FUNCTION insert_client (
  nombre VARCHAR(15), 
  apellidoP VARCHAR(20), 
  apellidoM VARCHAR(20), 
  tel VARCHAR(14), 
  correo VARCHAR(45))
RETURNS INT
BEGIN
  DECLARE id INT;
  INSERT INTO cliente (nombre, apellidoP, apellidoM, fechaReg, tel, correo) VALUES (nombre, apellidoP, apellidoM, CURDATE(), tel, correo);
  SELECT idCliente INTO id FROM cliente WHERE idCliente = LAST_INSERT_ID();
  RETURN id;
END$$

DELIMITER $$
CREATE FUNCTION insert_propiedad(
  idTipo INT, propietario INT, direccion VARCHAR(100), superficieT FLOAT, superficieC FLOAT, 
  amueblada VARCHAR(4), numRecamaras INT, numNiveles INT, numBaños INT, 
  mascotas TINYINT, posesion VARCHAR(9), adjudicion TINYINT)
RETURNS INT
BEGIN
  DECLARE id INT;
  INSERT INTO propiedad (idTipo, propietario, direccion, superficieT, superficieC, amueblada, numRecamaras, numNiveles, numBaños, mascotas, posesion, adjudicion, disponibilidad) 
  VALUES (idTipo, propietario, direccion, superficieT, superficieC, amueblada, numRecamaras, numNiveles, numBaños, mascotas, posesion, adjudicion, 1);
  SELECT idPropiedad INTO id FROM propiedad WHERE idPropiedad = LAST_INSERT_ID();
  RETURN id;
END$$

DELIMITER $$
CREATE FUNCTION insert_oferta(
  idPropiedad INT, 
  estado VARCHAR(5), 
  moneda VARCHAR(7), 
  precio FLOAT)
RETURNS INT
BEGIN
  DECLARE id INT;
  INSERT INTO oferta (idPropiedad, estado, moneda, precio) VALUES (idPropiedad, estado, moneda, precio);
  SELECT idOferta INTO id FROM oferta WHERE idOferta = LAST_INSERT_ID();
  RETURN id;
END$$
