
INSERT INTO `cliente` (`idCliente`, `nombre`, `apellidoP`, `apellidoM`, `fechaReg`, `tel`, `correo`) VALUES
(1, 'David', 'Moncivais', 'Maciel', '2022-11-28', '6644292741', 'david@moncivais.com'),
(2, 'john', 'doe', 'N/A', '2022-12-01', '0123456789', 'john@doe.com');

INSERT INTO `tipospropiedad` (`idTipo`, `tipo`) VALUES
(1, 'Casa'),
(2, 'Departamento'),
(3, 'Terreno'),
(4, 'Local C.'),
(5, 'Bodega'),
(6, 'Edificio');

INSERT INTO `propiedad` (`idPropiedad`, `idTipo`, `propietario`, `direccion`, `superficieT`, `superficieC`, `amueblada`, `numRecamaras`, `numNiveles`, `numBaños`, `mascotas`, `posesion`, `adjudicion`) VALUES
(1, 1, 1, 'Priv. Alcazar 12203, Res. Aguacaliente', 45646, 46456, 'Si', 4, 4, 7, 1, 'Regular', 0),
(2, 6, 1, '44 Ochre Point Ave, Newport, RI', 50000, 60000, 'Si', 20, 3, 20, 1, 'Regular', 0),
(3, 1, 1, '140 Lower Woodville Rd, Natchez, MS', 350000, 150000, 'Si', 13, 3, 15, 1, 'Regular', 0),
(4, 3, 1, '1600 Rockland Rd, Wilmington, DE', 1200000, 4400, 'Semi', 8, 5, 10, 0, 'Irregular', 1),
(5, 5, 1, 'Elvis Presley Blvd, Memphis, TN', 60000, 20000, '', 10, 4, 13, 0, 'Irregular', 1),
(6, 6, 1, '914 Division St, Billings, MT', 8094, 4042, 'Semi', 10, 4, 12, 1, 'Regular', 0),
(7, 5, 1, '1402 Broadway Avenue J, Galveston, TX', 1619, 940, 'Si', 12, 1, 14, 1, 'Irregular', 1),
(8, 2, 1, '501 Lincoln St, Sitka, AK', 2023, 123, 'No', 4, 2, 9, 0, 'Irregular', 0);

INSERT INTO `oferta` (`idOferta`, `idPropiedad`, `estado`, `moneda`, `precio`, `disponibilidad`) VALUES
(1, 1, 'Renta', 'Dolares', 456465, 1),
(2, 2, 'Venta', 'Dolares', 10000000, 1),
(3, 3, 'Renta', 'Dolares', 18600000, 1),
(4, 4, 'Renta', 'Dolares', 191000, 1),
(5, 5, 'Venta', 'Dolares', 38116000, 1),
(6, 6, 'Renta', 'Dolares', 190300, 1),
(7, 7, 'Renta', 'Dolares', 189300, 1),
(8, 8, 'Venta', 'Dolares', 1843000, 1);