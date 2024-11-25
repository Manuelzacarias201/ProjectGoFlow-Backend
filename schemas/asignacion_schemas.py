from pydantic import BaseModel
from typing import Optional

class AsignacionBase(BaseModel):
    descripcion: str
    tema: str
    usuario_asignado_id: int

class AsignacionCreate(AsignacionBase):
    descripcion: str
    tema: str
    usuario_asignado_id: int

class AsignacionUpdate(BaseModel):
    descripcion: Optional[str]
    tema: Optional[str]

class AsignacionResponse(BaseModel):
    id: int
    descripcion: str
    tema: str
    usuario_asignado_id: int

    class Config:
        orm_mode = True
