from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.db_config import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    # Columnas básicas
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    contraseña = Column(String, nullable=False)
    permisos = Column(String, nullable=False)

    # Relación con asignaciones
    asignaciones = relationship(
        "Asignacion",  # Nombre del modelo relacionado
        back_populates="usuario_asignado",  # Relación inversa en el modelo `Asignacion`
        cascade="all, delete-orphan",  # Para eliminar asignaciones al eliminar un usuario
    )

    # Relación con tareas
    tareas = relationship(
        "Tarea",  # Nombre del modelo relacionado
        back_populates="usuario",  # Relación inversa en el modelo `Tarea`
        cascade="all, delete-orphan",  # Para eliminar tareas al eliminar un usuario
    )
