from fastapi import FastAPI
import sqlite3
from typing import List
from pydantic import BaseModel
from pydantic import EmailStr
from fastapi import HTTPException
from fastapi import status



class mensaje(BaseModel):
	mensaje: str

class pasajeros(BaseModel):
	id_pasajero: int
	nombre: str
	primer_ap: str
	segundo_ap: str
	numero_usuario: str
	email: str



class pasajerosIN(BaseModel):
	id_pasajero: int
	nombre: str
	primer_ap: str
	segundo_ap: str
	numero_usuario: str
	email: str
	

class pasajeros_post(BaseModel):
	nombre: str
	primer_ap: str
	segundo_ap: str
	numero_usuario: str
	email: str
	password: str
	

description = """
	# Pasajeros API REST
	API para crear un CRUD de la tabla pasajeros 
	"""
app = FastAPI(
	tittle = "Pasajeros API REST",
	description = description,
	version = "0.0.1",
	terms_of_service="http://example.com/terms/",
	contact = {
		"name": "Oscar OY",
		"email": "oscar_orta94@hotmail.com",
	},
	license_info={
		"name":"Apache 2.0",
		"url":"https://www.apache.org/licenses/LICENSE-2.0.html",
	},
)

@app.get (
	"/",
	response_model=mensaje,
	status_code=status.HTTP_202_ACCEPTED,
	summary="Endpoint principal",
	description=" Regresa un mensaje de bienvenida",
)

async def read_root ():
	response = {"mensaje": "version 0.1"}
	return response

@app.get (
	"/pasajeros/{id_pasajero}",
	response_model=pasajerosIN,
	status_code=status.HTTP_202_ACCEPTED,
	summary="Pasajero a obtener",
	description="Endpoint que regresa un array con el id de un solo pasajero",
)

async def get_pasajeros(id_pasajero:int):
	try:
		with sqlite3.connect("Design/PasajerosModulo2/sql/pasajeros.db") as connection:
			connection.row_factory = sqlite3.Row
			cursor = connection.cursor()
			sql="SELECT id_pasajero, nombre, primer_ap, segundo_ap, numero_usuario, email FROM pasajeros WHERE id_pasajero=?;"
			values=(id_pasajero, )
			cursor.execute(sql,values)
			response= cursor.fetchone()
			return response
	except Exception as error:
		print(f"Error interno: {error.args}")
		raise HTTPException(
			status_code = status.HTTP_400_BAD_REQUEST,
			detail = "Error al consultar los datos",
		)
		 	

@app.get (
	"/pasajeros/",
	response_model = List[pasajeros],
	status_code = status.HTTP_202_ACCEPTED,
	summary = "Lista de pasajeros",
	description = "Endpoint que regresa un array con todos los pasajeros",
)

async def get_pasajeros():
	try:
		with sqlite3.connect("Design/PasajerosModulo2/sql/pasajeros.db") as connection:
			connection.row_factory = sqlite3.Row
			cursor = connection.cursor()
			cursor.execute("SELECT id_pasajero, nombre, primer_ap, segundo_ap, numero_usuario, email FROM pasajeros;")
			response = cursor.fetchall()
			return response
	except Exception as error:
		print(f"Error interno: {error.args}")
		raise HTTPException(
			status_code = status.HTTP_400_BAD_REQUEST,
			detail = "Error al consultar los datos",
		) 


@app.post(
	"/pasajeros/",
	response_model=mensaje,
	status_code= status.HTTP_202_ACCEPTED,
	summary="pasajero a insertar",
	description="Endpoint para insertar un pasajero",
)

async def post_pasajeros(pasajero:pasajeros_post):
	try:
		with sqlite3.connect("Design/PasajerosModulo2/sql/pasajeros.db") as connection:
			connection.row_factory = sqlite3.Row
			cursor = connection.cursor()
			sql="INSERT INTO pasajeros VALUES (null, ?, ?, ?, ?, ?, ?);"
			values=(pasajero.nombre, pasajero.primer_ap, pasajero.segundo_ap, pasajero.numero_usuario, pasajero.email, pasajero.password,)
			cursor.execute(sql,values)
			response = {"mensaje":"Pasajero insertado"}
			return response
	except Exception as error:
		print(f"Error al insertar los datos: {error.args}")
		raise HTTPException(
			status_code = status.HTTP_400_BAD_REQUEST,
			detail = "Error al insertar los datos",
		) 
		
@app.put(
	"/pasajeros/{id_pasajero}",
	response_model=mensaje,
	status_code= status.HTTP_202_ACCEPTED,
	summary="Actualizar pasajero",
	description="Endpoint actualización de datos",
)

async def pasajero_put(id_pasajero: int, pasajero:pasajeros_post):
	try:
		with sqlite3.connect("Design/PasajerosModulo2/sql/pasajeros.db") as connection:
			connection.row_factory=sqlite3.Row
			cursor=connection.cursor()
			sql=("UPDATE pasajeros SET nombre=?, primer_ap=?, segundo_ap=?, numero_usuario=?, email=?, password=? WHERE id_pasajero=?;")
			values=(pasajero.nombre, pasajero.primer_ap, pasajero.segundo_ap, pasajero.numero_usuario,  pasajero.email, pasajero.password, id_pasajero,)
			cursor.execute(sql,values)
			response = {"mensaje":"Pasajero acuralizado"}
			return response
	except Exception as error:
		print(f"Error interno:{error.args}")
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Error al actualizar datos",
		)

@app.delete(
	"/pasajeros/{id_pasajero}",
	response_model=mensaje,
	status_code= status.HTTP_202_ACCEPTED,
	summary="Eliminar pasajero",
	description="Endpoint para la eliminación de datos",
)

async def pasajero_delete(id_pasajero: int):
	try:
		with sqlite3.connect("Design/PasajerosModulo2/sql/pasajeros.db") as connection:
			connection.row_factory=sqlite3.Row
			cursor=connection.cursor()
			sql=("DELETE FROM pasajeros WHERE id_pasajero=?;")
			values=(id_pasajero,)
			cursor.execute(sql,values)
			response = {"mensaje":"Pasajero eliminado"}
			return response
	except Exception as error:
		print(f"Error interno:{error.args}")
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Error al eliminar el pasajero",
		)