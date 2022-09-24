## Tabla choferes

|campo|tipo de dato|descripcion|
|----|----|---|
|id_chofer|integer|identificador del chofer|
|id_unidad|integer|identificador de la unidad|
|nombre|varchar(50)|nombre del chofer|
|primer_a|varchar(50)|primer apellido|
|segundo_a|varchar(50)|segundo apellido|
|CURP|varchar(30)|curp del chofer|
|numero_licencia|varchar(50)|numero de licencia del chofer|

## Scrip

CREATE TABLE choferes(

id_chofer integer primary key AUTO_INCREMENT,

id_consesionario int NOT NULL,

nombre varchar (50) NOT NULL,

primer_ap varchar(50),

segundo_ap varchar (50),

curp varchar (50) NOT NULL,

numero_licencia varchar(50) NOT NULL

) ENGINE=INNODB;


|Parametros|Datos|
|---|---|
|Description|End point para insertar un registro|
|Method|Post|
|Endpoint|http://localhost:8000/choferes|
|Query param|NA|
|Path param|NA|
|Data|{"id_consesionario":int,"nombre":string,"primer_ap":string,"segundo_ap":string,"curp":string,"numero_licencia":string}|
|Status code|202
|Response type|JSON|
|Response|{"mensaje":"Se ha insertado correctamente"}|
|Status code (error)|400|
|Response type (error)|{"mensaje":"Error al insertar datos"}|
|cURL|curl -d {"id_consesionario":int,"nombre":string,"primer_ap":string,"segundo_ap":string,"curp":string,"numero_licencia":string} -x post -H http://localhost:8000/choferes|



|Parametros|Datos|
|---|---|
|Description|End point para consultar todos los registros|
|Method|Get|
|Endpoint|http://localhost:8000/choferes|
|Query param|NA|
|Path param|NA|
|Data|{"id_chofer":int,"id_consesionario":int,"nombre":string,"primer_ap":string,"segundo_ap":string,"curp":string,"numero_licencia":string}|
|Status code|202
|Response type|JSON|
|Response||
|Status code (error)|400|
|Response type (error)|{"mensaje":"Error no se pudo realizar la consulta"}|
|cURL|curl -d {"id_chofer":int,"id_consesionario":int,"nombre":string,"primer_ap":string,"segundo_ap":string,"curp":string,"numero_licencia":string} -x get -H http://localhost:8000/choferes|



|Parametros|Datos|
|---|---|
|Description|End point para consultar un registro|
|Method|Get|
|Endpoint|http://localhost:8000/choferes?id_chofer=x|
|Query param|id_chofer|
|Path param|NA|
|Data|{"id_chofer":int,"id_consesionario":int,"nombre":string,"primer_ap":string,"segundo_ap":string,"curp":string,"numero_licencia":string}|
|Status code|202
|Response type|JSON|
|Response||
|Status code (error)|400|
|Response type (error)|{"mensaje":"Error no se pudo realizar la consulta"}|
|cURL|curl -d {"id_chofer":int,"id_consesionario":int,"nombre":string,"primer_ap":string,"segundo_ap":string,"curp":string,"numero_licencia":string} -x get -H http://localhost:8000/choferes?id_chofer=x|


|Parametros|Datos|
|---|---|
|Description|End point para actualizar un chofer|
|Method|Put|
|Endpoint|http://localhost:8000/choferes?id_chofer=x|
|Query param|id_chofer|
|Path param|NA|
|Data|{"id_consesionario":int,"nombre":string,"primer_ap":string,"segundo_ap":string,"curp":string,"numero_licencia":string}|
|Status code|202
|Response type|JSON|
|Response|{"mensaje":"Se ha actualizado correctamente"}|
|Status code (error)|400|
|Response type (error)|{"mensaje":"Error al actualizar datos"}|
|cURL|curl -d {"id_consesionario":int,"nombre":string,"primer_ap":string,"segundo_ap":string,"curp":string,"numero_licencia":string} -x put -H http://localhost:8000/choferes?id_chofer=x|


|Parametros|Datos|
|---|---|
|Description|End point para eliminar un chofer|
|Method|Delete|
|Endpoint|http://localhost:8000/choferes?id_chofer=x|
|Query param|id_chofer|
|Path param|NA|
|Data||
|Status code|202
|Response type|JSON|
|Response|{"mensaje":"Se ha eliminado correctamente"}|
|Status code (error)|400|
|Response type (error)|{"mensaje":"Error al eliminar datos"}|
|cURL|curl -d {"id_consesionario":int,"nombre":string,"primer_ap":string,"segundo_ap":string,"curp":string,"numero_licencia":string} -x delete -H http://localhost:8000/choferes?id_chofer=x|



