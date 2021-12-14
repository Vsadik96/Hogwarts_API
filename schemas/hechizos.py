from pydantic import BaseModel
from typing import Optional

class HechizosBase (BaseModel):
    id: Optional[int]
    hechizo: str
    uso: str