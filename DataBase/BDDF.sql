DELIMITER $$
CREATE FUNCTION insert_client (
  n VARCHAR(15), 
  aP VARCHAR(20), 
  aM VARCHAR(20), 
  t VARCHAR(14), 
  c VARCHAR(45))
RETURNS INT
BEGIN
  DECLARE id INT;
  INSERT INTO cliente (nombre, apellidoP, apellidoM, fechaReg, tel, correo) VALUES (n, aP, aM, CURDATE(), t, c);
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
  INSERT INTO propiedad (idTipo, propietario, direccion, superficieT, superficieC, amueblada, numRecamaras, numNiveles, numBaños, mascotas, posesion, adjudicion) 
  VALUES (idTipo, propietario, direccion, superficieT, superficieC, amueblada, numRecamaras, numNiveles, numBaños, mascotas, posesion, adjudicion);
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
  INSERT INTO oferta (idPropiedad, estado, moneda, precio, disponibilidad) VALUES (idPropiedad, estado, moneda, precio, 1);
  SELECT idOferta INTO id FROM oferta WHERE idOferta = LAST_INSERT_ID();
  RETURN id;
END$$

DELIMITER $$
CREATE TRIGGER update_availability
  BEFORE DELETE
  ON rentas FOR EACH ROW
BEGIN
  UPDATE oferta SET disponibilidad = 1 WHERE idOferta = OLD.idOferta;
END$$