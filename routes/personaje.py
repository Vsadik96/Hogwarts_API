from fastapi import APIRouter
from config.hogwarts_BD import conexion
from models.personaje import Tablapersonajes
from sqlalchemy import select, insert
from schemas.personaje import PersonajesBase
from auth.auth_bearer import JWTBearer
from fastapi import Depends



personaje = APIRouter()

@personaje.get("/personajes" )
def get_personaje():
    return conexion.execute(
        Tablapersonajes.select()).fetchall()

@personaje.post("/personajes",dependencies=[Depends(JWTBearer())])
def create_personaje (personajebase: PersonajesBase):
    nuevo_personaje= {
        "personaje": personajebase.personaje,
        "casa_hogwarts": personajebase.casa_hogwarts,
        "descripcion":personajebase.descripcion,
        "fecha_nacimiento": personajebase.fecha_nacimiento,
        "imagen": personajebase.imagen
    }
    resultado = conexion.execute(Tablapersonajes.insert().values(nuevo_personaje))
    return conexion.execute(Tablapersonajes.select().where(Tablapersonajes.c.id == resultado.lastrowid)).first()

@personaje.get("/personajes/{id}")
def search_personaje(id: str):
    return  conexion.execute(Tablapersonajes.select().where(Tablapersonajes.c.id == id)).first()

@personaje.delete("/personajes/{id}")
def delete_personaje(id: str):
    resultado = conexion.execute(Tablapersonajes.delete().where(Tablapersonajes.c.id == id))
    return "Personaje eliminado"

@personaje.put("/personajes/{id}",dependencies=[Depends(JWTBearer())])
def update_personaje(id:str, personajebase: PersonajesBase):

    conexion.execute(Tablapersonajes.update().values(
        personaje= personajebase.personaje,
        casa_hogwarts= personajebase.casa_hogwarts,
        descripcion= personajebase.descripcion,
        fecha_nacimiento= personajebase.fecha_nacimiento,
        imagen= personajebase.imagen

    ).where(Tablapersonajes.c.id == id))
    return "Personaje actualizado"
