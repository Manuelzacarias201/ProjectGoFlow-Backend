from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.tarea_model import Tarea

def crear_tarea(db: Session, nombre: str, descripcion: str, estado: str, usuario_id: int):
    nueva_tarea = Tarea(nombre=nombre, descripcion=descripcion, estado=estado, usuario_id=usuario_id)
    db.add(nueva_tarea)
    db.commit()
    db.refresh(nueva_tarea)
    return nueva_tarea

def obtener_tareas(db: Session):
    return db.query(Tarea).all()

def obtener_tarea_por_id(db: Session, tarea_id: int):
    return db.query(Tarea).filter(Tarea.id == tarea_id).first()

def actualizar_tarea(db: Session, tarea_id: int, datos_actualizados: dict):
    tarea = db.query(Tarea).filter(Tarea.id == tarea_id).first()
    if tarea:
        for key, value in datos_actualizados.items():
            setattr(tarea, key, value)
        db.commit()
        db.refresh(tarea)
    return tarea

def eliminar_tarea(db: Session, tarea_id: int):
    tarea = db.query(Tarea).filter(Tarea.id == tarea_id).first()
    
    # Si no se encuentra la tarea, lanzamos una excepción HTTP 404
    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada.")
    
    db.delete(tarea)  # Elimina la tarea
    db.commit()  # Guarda los cambios
    return tarea  # Devuelve la tarea eliminada
