from fastapi import FastAPI
from routes.user import user
from routes.buscar import buscar, buscador
from routes.personaje import personaje
from routes.peliculas import pelicula
from routes.libros import libro
from routes.hechizos import hechizo
from routes.hechizo_personaje import hechizo_personaje
from fastapi.middleware.cors import CORSMiddleware

main = FastAPI()

origins = [
    "http://localhost:3306",
    "http://localhost:4200",
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8000/peliculas/",
    "http://localhost:8000/login",
    "http://localhost:4200/login"
]

main.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

main.include_router(personaje)
main.include_router(pelicula)
main.include_router(libro)
main.include_router(hechizo)
main.include_router(hechizo_personaje)
main.include_router(buscador)
main.include_router(user)






