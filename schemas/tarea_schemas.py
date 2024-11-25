from pydantic import BaseModel
from typing import Optional
from enum import Enum

class EstadoTarea(str, Enum):
    inicio = "inicio"
    en_progreso = "en_progreso"
    completada = "completada"

class TareaBase(BaseModel):
    nombre: str
    descripcion: str
    estado: EstadoTarea

class TareaCreate(TareaBase):
    usuario_id: int

class TareaUpdate(BaseModel):
    nombre: Optional[str]
    descripcion: Optional[str]
    estado: Optional[EstadoTarea]

class TareaResponse(TareaBase):
    id: int
    usuario_id: int

    class Config:
        orm_mode = True
