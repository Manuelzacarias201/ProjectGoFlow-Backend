# services/asignacion_services.py
from sqlalchemy.orm import Session
from models.asignacion_model import Asignacion
from schemas.asignacion_schemas import AsignacionCreate

def crear_asignacion(db: Session, asignacion: AsignacionCreate):
    db_asignacion = Asignacion(
        descripcion=asignacion.descripcion,
        tema=asignacion.tema,
        usuario_asignado_id=asignacion.usuario_asignado_id
    )
    db.add(db_asignacion)
    db.commit()
    db.refresh(db_asignacion)
    return db_asignacion

def obtener_asignaciones(db: Session):
    # Obtiene todas las asignaciones de la base de datos
    return db.query(Asignacion).all()

# Asegúrate de definir también otras funciones que necesites, como obtener_asignaciones_por_usuario
def obtener_asignaciones_por_usuario(db: Session, usuario_asignado_id: int):
    # Obtiene las asignaciones de un usuario específico
    return db.query(Asignacion).filter(Asignacion.usuario_asignado_id == usuario_asignado_id).all()
