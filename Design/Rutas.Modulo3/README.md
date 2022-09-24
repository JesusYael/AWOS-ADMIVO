## Tabla rutas

|Campo|Tipo de dato|Descripción|
|---|---|---|
|id_ruta|integer|identificador de la ruta|
|id_base|integer|identeificador de base a la que pertenece la ruta|
|ruta_inicial|varchar|lugar de inicio de la ruta|
|destino|varchar|lugar de destino de la ruta|
|monto|integer|costo de pasaje|

## Script
CREATE TABLE rutas(

id_ruta integer primary key AUTOINCREMENT,

id_base integer NOT NULL,

ruta_inicial VARCHAR (50) NOT NULL,

destino VARCHAR (50) NOT NULL,

monto int NOT NULL,

FOREIGN KEY (id_base) REFERENCES base (id_base)

);

|Property|Value|
|---|---|
|Description|End point para consultar todos los registros|
|Method|Get|
|Endpoint|http://localhost:8000/rutas|
|Query param|NA|
|Path param|NA|
|Data| NA|
|Status code|202|
|Response type|JSON|
|Response|{"id_ruta":int, "id_base":int, "ruta_inicial":string, "destino":string, "monto":int}|
|Status code (error)|400|
|Responte type (error)|JSON|
|Response (error)|{"mensaje":"No se pudo realizar la consulta"}|
|cURL|curl -d {"id_ruta":int,"id_base":int,"ruta_inicial":string, "destino":string, "monto":int} -x GET -H http://localhost:8000/rutas|


|Property|Value|
|---|---|
|Description|End point para consultar un registro|
|Method|Get|
|Endpoint|http://localhost:8000/rutas/{id_ruta}|
|Query param|id_ruta|
|Path param|NA|
|Data| NA|
|Status code|202|
|Response type|JSON|
|Response|{"id_ruta":int, "id_base":int, "ruta_inicial":string, "destino":string, "monto":int}|
|Status code (error)|400|
|Responte type (error)|JSON|
|Response (error)|{"mensaje":"No se pudo realizar la consulta"}|
|cURL|curl -d {"id_ruta":int,"id_base":int,"ruta_inicial":string, "destino":string, "monto":int} -x GET -H http://localhost:8000/rutas/{id_ruta}|

|Property|Value|
|---|---|
|Description|End point para agregar una nueva ruta|
|Method|POST|
|Endpoint|http://localhost:8000/rutas|
|Query param|NA|
|Path param|NA|
|Data|{"id_ruta":int, "id_base":int, "ruta_inicial":string, "destino":string, "monto":int}|
|Status code|202|
|Response type|JSON|
|Response|{"mensaje":"Registro insertado correctamente"}|
|Status code (error)|400|
|Responte type (error)|JSON|
|Response (error)|{"mensaje":"Error al insertar el registro"}|
|cURL|curl -d {"id_ruta":int,"id_base":int,"ruta_inicial":string, "destino":string, "monto":int} -x POST -H http://localhost:8000/rutas|

|Property|Value|
|---|---|
|Description|End point para actualizar rutas por ID|
|Method|PUT|
|Endpoint|http://localhost:8000/rutas{id_ruta}|
|Query param|NA|
|Path param|id_ruta|
|Data|{"id_ruta":int, "id_base":int, "ruta_inicial":string, "destino":string, "monto":int}|
|Status code|202|
|Response type|JSON|
|Response|{"mensaje":"Se ha actualizado correctamente"}|
|Status code (error)|400|
|Responte type (error)|JSON|
|Response (error)|{"mensaje":"Error al actualizar"}|
|cURL|curl -d {"id_ruta":int,"id_base":int,"ruta_inicial":string, "destino":string, "monto":int} -x PUT -H http://localhost:8000/rutas/{id_ruta}|

|Property|Value|
|---|---|
|Description|End point para borrar una ruta por ID|
|Method|DELETE|
|Endpoint|http://localhost:8000/rutas{id_ruta}|
|Query param|NA|
|Path param|id_ruta|
|Data|NA|
|Status code|202|
|Response type|JSON|
|Response|{"mensaje":"Se ha eliminaado correctamente"}|
|Status code (error)|400|
|Responte type (error)|JSON|
|Response (error)|{"mensaje":"Error al eliminar"}|
|cURL|curl -d {"id_ruta":int,"id_base":int,"ruta_inicial":string, "destino":string, "monto":int} -x DELETE -H http://localhost:8000/rutas/{id_ruta}|
