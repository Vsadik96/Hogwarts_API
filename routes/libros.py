from fastapi import APIRouter, Depends

from auth.auth_bearer import JWTBearer
from models.libros import Tablalibros
from schemas.libros import LibrosBase
from config.hogwarts_BD import conexion
from sqlalchemy import select

libro = APIRouter()

@libro.get("/libros")
def get_libro():
    return  conexion.execute(
        Tablalibros.select()).fetchall()               #para generar la conexion

@libro.post("/libros",dependencies=[Depends(JWTBearer())])
def create_libro(librobase: LibrosBase):
    nuevo_libro = {
        "libro": librobase.libro,
        "autora": librobase.autora,
        "fecha_lanzamiento": librobase.fecha_lanzamiento,
        "descripcion": librobase.descripcion,
        "imagen": librobase.imagen
    }
    resultado = conexion.execute(Tablalibros.insert().values(nuevo_libro))
    return conexion.execute(Tablalibros.select().where(Tablalibros.c.id == resultado.lastrowid)).first()

@libro.get("/libros/{id}")
def search_libro(id: str):

    return conexion.execute(Tablalibros.select().where(Tablalibros.c.id == id)).first()

@libro.delete("/libros/{id}",dependencies=[Depends(JWTBearer())])
def delete_libro(id: str):
    resultado = conexion.execute(Tablalibros.delete().where(Tablalibros.c.id == id))
    return "Libro eliminado"

@libro.put("/libros/{id}",dependencies=[Depends(JWTBearer())])
def update_libro(id: str, librobase: LibrosBase):
    conexion.execute(Tablalibros.update().values(
        libro=librobase.libro,
        autora=librobase.autora,
        fecha_lanzamiento= librobase.fecha_lanzamiento,
        descripcion= librobase.descripcion,
        imagen= librobase.imagen
    ).where(Tablalibros.c.id == id))
    return "Libro actualizado"
