id_base int NOT NULL,

id_chofer int NOT NULL,

modelo varchar (30) NOT NULL,

anio varchar (10) NOT NULL,

placas varchar (10) NOT NULL,

kilometraje varchar (10) NOT NULL,

numero_seguro varchar (50) NOT NULL,

fecha_verificacion date NOT NULL,

num_tarjeta_circulacion varchar (50) NOT NULL

) ENGINE=INNODB;

ALTER TABLE unidades ADD FOREIGN KEY (id_consesionario) REFERENCES consesionario (id_consesionario);

ALTER TABLE unidades ADD FOREIGN KEY (id_base) REFERENCES base (id_base);

ALTER TABLE unidades ADD FOREIGN KEY (id_chofer) REFERENCES choferes (id_chofer);

CREATE TABLE pasajeros(

id_pasajero integer PRIMARY KEY AUTO_INCREMENT,

nombre VARCHAR (50) NOT NULL,

primer_ap VARCHAR (50) NOT NULL,

segundo_ap VARCHAR (50),

numero_usuario VARCHAR (10) NOT NULL,

email VARCHAR (50) NOT NULL,

password VARCHAR (32) NOT NULL,

registros int NOT NULL

) ENGINE=INNODB;

CREATE TABLE registro(

id_registro int primary key AUTO_INCREMENT,

id_pasajero int NOT NULL,

id_ruta int NOT NULL,

id_unidad int NOT NULL,

monto int (10) NOT NULL,

fecha timestamp NOT NULL

) ENGINE=INNODB;

ALTER TABLE registro ADD FOREIGN KEY (id_consesionario) REFERENCES consesionario (id_consesionario);

ALTER TABLE registro ADD FOREIGN KEY (id_pasajero) REFERENCES pasajeros (id_pasajero);

ALTER TABLE registro ADD FOREIGN KEY (id_ruta) REFERENCES rutas (id_ruta);

ALTER TABLE registro ADD FOREIGN KEY (id_unidad) REFERENCES unidades (id_unidad);

CREATE TABLE mantenimiento(

id_mantenimiento integer primary key AUTO_INCREMENT,

id_consesionario int NOT NULL,

id_unidad integer NOT NULL,

falla varchar (60) NOT NULL,

fecha_reparación date NOT NULL,

costo integer NOT NULL,

FOREIGN KEY (id_unidad) REFERENCES unidades (id_unidad)

) ENGINE=INNODB;

ALTER TABLE mantenimiento ADD FOREIGN KEY (id_consesionario) REFERENCES consesionario (id_consesionario);

CREATE TABLE registro_pasajero(

id_registro int primary key AUTO_INCREMENT,

id_pasajero int NOT NULL,

id_ruta int NOT NULL,

id_unidad int NOT NULL,

monto int (10) NOT NULL,

fecha timestamp NOT NULL

) ENGINE=INNODB;

ALTER TABLE registro ADD FOREIGN KEY (id_pasajero) REFERENCES pasajeros (id_pasajero);

ALTER TABLE registro ADD FOREIGN KEY (id_ruta) REFERENCES rutas (id_ruta);

ALTER TABLE registro ADD FOREIGN KEY (id_unidad) REFERENCES unidades (id_unidad);
