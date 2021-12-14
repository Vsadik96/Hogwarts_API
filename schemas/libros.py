from pydantic import BaseModel
from typing import Optional

class LibrosBase (BaseModel):
    id: Optional[int]
    libro: str
    fecha_lanzamiento: str
    autora: str
    descripcion: str
    imagen: str