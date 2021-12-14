from fastapi import APIRouter
from config.hogwarts_BD import conexion
from models.hechizos import Tablahechizos
from schemas.hechizos import HechizosBase
from sqlalchemy import select
from auth.auth_bearer import JWTBearer
from fastapi import Depends


hechizo = APIRouter()

@hechizo.get("/hechizos")
def get_hechizo():
    return conexion.execute(
        Tablahechizos.select()).fetchall()                #para generar la conexion

@hechizo.post("/hechizos",dependencies=[Depends(JWTBearer())])
def create_hechizo(hechizosbase: HechizosBase):
    nuevo_hechizo={
        "hechizo": hechizosbase.hechizo,
        "uso": hechizosbase.uso
    }
    resultado = conexion.execute(Tablahechizos.insert().values(nuevo_hechizo))
    return conexion.execute(Tablahechizos.select().where(Tablahechizos.c.id == resultado.lastrowid)).first()

@hechizo.get("/hechizos/{id}")
def search_hechizo(id: str):
    return conexion.execute(Tablahechizos.select().where(Tablahechizos.c.id == id)).first()

@hechizo.delete("/hechizos/{id}",dependencies=[Depends(JWTBearer())])
def delete_hechizo(id: str):
    resultado = conexion.execute(Tablahechizos.delete().where(Tablahechizos.c.id == id))
    return "Hechizo eliminado"

@hechizo.put("/hechizos/{id}",dependencies=[Depends(JWTBearer())])
def update_hechizo(id: str, hechizobase: HechizosBase):
    conexion.execute(Tablahechizos.update().values(
        hechizo= hechizobase.hechizo,
        uso= hechizobase.uso
    ).where(Tablahechizos.c.id==id))
    return "Hechizo actualizado"