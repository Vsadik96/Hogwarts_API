from fastapi import APIRouter
from config.hogwarts_BD import conexion
from models.hechizos_personajes import Tablahechizos_personajes
from sqlalchemy import select

hechizo_personaje = APIRouter()

@hechizo_personaje.get("/hechizos")
def get_hechizo():
    return conexion.execute(
        Tablahechizos_personajes.select()).fetchall()