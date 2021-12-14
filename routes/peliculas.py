from fastapi import APIRouter
from config.hogwarts_BD import conexion
from models.peliculas import Tablapeliculas
from schemas.peliculas import PeliculasBase
from sqlalchemy import select

pelicula = APIRouter()

@pelicula.get("/peliculas")
def get_pelicula():
    return conexion.execute(
        Tablapeliculas.select()).fetchall()                 #para generar la conexion

@pelicula.post("/peliculas")
def create_pelicula(peliculabase: PeliculasBase):
    nueva_pelicula = {
        "titulo": peliculabase.titulo,
        "director": peliculabase.director,
        "fecha_lanzamiento": peliculabase.fecha_lanzamiento,
        "descripcion": peliculabase.descripcion,
        "imagen": peliculabase.imagen
    }

    resultado = conexion.execute(Tablapeliculas.insert().values(nueva_pelicula))
    return conexion.execute(Tablapeliculas.select().where(Tablapeliculas.c.id == resultado.lastrowid)).first()

@pelicula.get("/peliculas/{id}")
def search_pelicula(id: str):
    return conexion.execute(Tablapeliculas.select().where(Tablapeliculas.c.id == id)).first()

@pelicula.delete("/peliculas/{id}")
def delete_pelicula(id: str):
   resultado = conexion.execute(Tablapeliculas.delete().where(Tablapeliculas.c.id == id))
   return "Pelicula eliminada"

@pelicula.put("/peliculas/{id}")
def update_pelicula(id: str, peliculasbase: PeliculasBase):
    conexion.execute(Tablapeliculas.update.values(
        titulo= peliculasbase.titulo,
        director= peliculasbase.director,
        fecha_lanzamiento= peliculasbase.fecha_lanzamiento,
        descripcion= peliculasbase.descripcion,
        imagen= peliculasbase.imagen
    ).where(Tablapeliculas.c.id == id))
    return "Pelicula actualizada"
