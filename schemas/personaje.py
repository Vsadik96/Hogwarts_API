from typing import Optional, List
from pydantic import BaseModel


class PersonajesBase (BaseModel):
    id: Optional [int]
    personaje: str
    casa_hogwarts: str
    descripcion: str
    progenitor: Optional [int]
    fecha_nacimiento: str
    imagen: str
    hijos: str

