from fastapi import APIRouter, Query

from config.hogwarts_BD import conexion
from models.hechizos import Tablahechizos
from models.libros import Tablalibros
from models.peliculas import Tablapeliculas
from models.personaje import Tablapersonajes

buscador = APIRouter ()

@buscador.get("/buscador/{textoBusqueda}")
def buscar(textoBusqueda: str):

    resultadoLibros = conexion.execute(Tablalibros.select().where(Tablalibros.c.libro.like('%'+textoBusqueda+'%'))).fetchall()
    resultadoPersonajes = conexion.execute(Tablapersonajes.select().where(Tablapersonajes.c.personaje.like('%'+textoBusqueda+'%'))).fetchall()
    resultadoHechizos = conexion.execute(Tablahechizos.select().where(Tablahechizos.c.hechizo.like('%'+textoBusqueda+'%'))).fetchall()
    resultadoPeliculas = conexion.execute(Tablapeliculas.select().where(Tablapeliculas.c.titulo.like('%'+textoBusqueda+'%'))).fetchall()

    resultadoBusqueda = {
            "resultadoHechizos": resultadoHechizos,
            "resultadoPersonajes": resultadoPersonajes,
            "resultadoLibros": resultadoLibros,
            "resultadoPeliculas": resultadoPeliculas
        }

    return resultadoBusqueda