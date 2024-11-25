from sqlalchemy.orm import Session
from models.asignacion_model import Asignacion

def crear_asignacion(db: Session, descripcion: str, tema: str, usuario_asignado_id: int):
    nueva_asignacion = Asignacion(
        descripcion=descripcion,
        tema=tema,
        usuario_asignado_id=usuario_asignado_id,
    )
    db.add(nueva_asignacion)
    db.commit()
    db.refresh(nueva_asignacion)
    return nueva_asignacion

def obtener_asignaciones(db: Session):
    return db.query(Asignacion).all()

def actualizar_asignacion(db: Session, asignacion_id: int, descripcion: str, tema: str):
    asignacion = db.query(Asignacion).filter(Asignacion.id == asignacion_id).first()
    if asignacion:
        asignacion.descripcion = descripcion
        asignacion.tema = tema
        db.commit()
        db.refresh(asignacion)
    return asignacion

def eliminar_asignacion(db: Session, asignacion_id: int):
    asignacion = db.query(Asignacion).filter(Asignacion.id == asignacion_id).first()
    if asignacion:
        db.delete(asignacion)
        db.commit()
    return asignacion
