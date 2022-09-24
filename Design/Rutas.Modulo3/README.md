## Tabla Base

|Campo|Tipo de dato|Descripcion|
|----|----|---|
|id_ruta|integer|Identificador de la ruta|
|dirección|varchar(50)|Nombre de la dirección de ruta|
|unidades|INT|Número de unidades que tiene la base|

## Scrip

CREATE TABLE base(

id_base integer primary key AUTOINCREMENT,

direccion VARCHAR (50) NOT NULL,

unidades INT NOT NULL

);


|Parametros|Datos|
|---|---|
|Description|End point para insertar una nueva base|
|Method|Post|
|URI|http://localhost:8000/base|
|Query param|NA|
|Path param|NA|
|Data|{"dirección":varchar,"unidades":INT}|
|Status code|201
|Response type|JSON|
|Response|{"mensaje":"Registro insertado"}|
|Status code (error)|400|
|Response type (error)|{"mensaje":"Error al insertar datos"}|
|CURL|curl -d {"dirección":varchar,"unidades":INT} -x post -H http://localhost:8000/choferes|



|Parametros|Datos|
|---|---|
|Description|End point para consultar todas las bases|
|Method|Get|
|URI|http://localhost:8000/base|
|Query param|NA|
|Path param|NA|
|Data|NA|
|Status code|200
|Response type|JSON|
|Response|[{"dirección":varchar,"unidades":INT}, {"dirección":varchar,"unidades":INT}]|
|Status code (error)|404|
|Response type (error)|{"mensaje":"Error al realizar la consulta"}|
|CURL|curl -x get -H http://localhost:8000/base|



|Parametros|Datos|
|---|---|
|Description|End point para consultar un solo registro|
|Method|Get|
|URI|http://localhost:8000/base?id_base=x|
|Query param|id_base|
|Path param|NA|
|Data|NA|
|Status code|200
|Response type|JSON|
|Response|{"dirección":varchar,"unidades":INT}|
|Status code (error)|400|
|Response type (error)|{"mensaje":"Error no se pudo realizar la consulta"}|
|CURL|curl -x get -H http://localhost:8000/base?id_base=x|


|Parametros|Datos|
|---|---|
|Description|End point para actualizar una sola base|
|Method|Put|
|URI|http://localhost:8000/base?id_base=x|
|Query param|id_base|
|Path param|NA|
|Data|{"dirección":varchar,"unidades":INT}|
|Status code|200
|Response type|JSON|
|Response|{"mensaje":"Se ha actualizado correctamente"}|
|Status code (error)|400|
|Response type (error)|{"mensaje":"Error al actualizar datos"}|
|CURL|curl -d {"dirección":varchar,"unidades":INT} -x put -H http://localhost:8000/base?id_base=x|


|Parametros|Datos|
|---|---|
|Description|End point para eliminar una base|
|Method|Delete|
|URI|http://localhost:8000/base?id_base=x|
|Query param|id_base|
|Path param|NA|
|Data|NA|
|Status code|202
|Response type|JSON|
|Response|{"mensaje":"Se ha eliminado correctamente"}|
|Status code (error)|400|
|Response type (error)|{"mensaje":"Error al eliminar datos"}|
|CURL|curl -x delete -H http://localhost:8000/choferes?id_chofer=x|




