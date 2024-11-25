from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from config.db_config import Base

# Modelo SQLAlchemy para Asignacion
class Asignacion(Base):
    __tablename__ = "asignaciones"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String, nullable=False)
    tema = Column(String, nullable=False)
    usuario_asignado_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)

    usuario_asignado = relationship("Usuario", back_populates="asignaciones")

# Modelo Pydantic para la creación de asignación
class AsignacionCreate(BaseModel):
    descripcion: str
    tema: str
    usuario_asignado_id: int

# Modelo Pydantic para la respuesta
class AsignacionResponse(BaseModel):
    id: int
    descripcion: str
    tema: str
    usuario_asignado_id: int

    class Config:
        from_attributes = True  # Usamos 'from_attributes' en lugar de 'orm_mode'
