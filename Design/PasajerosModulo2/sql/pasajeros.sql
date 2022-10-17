CREATE TABLE pasajeros(
    
id_pasajero integer PRIMARY KEY AUTOINCREMENT,

nombre VARCHAR (50) NOT NULL,

primer_ap VARCHAR (50) NOT NULL,

segundo_ap VARCHAR (50),

numero_usuario VARCHAR (10) NOT NULL,

email VARCHAR (50) NOT NULL,

password VARCHAR (32) NOT NULL,

registros int NOT NULL

);

insert into pasajeros(nombre,primer_ap,segundo_ap,numero_usuario,email,password,registros)
values 
("Sofia","Tunez","Rural","1","sofia@email.com","12345",1),
("Maria","Polinesia","Garica","2","maria@email.com","54321",2);