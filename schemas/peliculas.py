from pydantic import BaseModel
from typing import Optional

class PeliculasBase (BaseModel):
    id: Optional[int]
    titulo: str
    fecha_lanzamiento: str
    director: str
    descripcion: str
    imagen: str