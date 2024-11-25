from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.asignacion_schemas import AsignacionCreate
from schemas.tarea_schemas import TareaResponse  # Importa el esquema TareaResponse
from models.tarea_model import Tarea  # Importa el modelo Tarea
from services.asignacion_services import crear_asignacion
from services.tarea_services import eliminar_tarea
from config.db_config import get_db

router = APIRouter()

# Endpoint para crear una asignación
@router.post("/asignaciones/create")
async def crear_asignacion_endpoint(asignacion: AsignacionCreate, db: Session = Depends(get_db)):
    return await crear_asignacion(db, asignacion.descripcion, asignacion.tema, asignacion.usuario_asignado_id)

@router.get("/usuario/{usuario_id}", response_model=list[TareaResponse])
async def get_tareas_por_usuario(usuario_id: int, db: Session = Depends(get_db)):
    # Consultar tareas asociadas al usuario
    tareas = db.query(Tarea).filter(Tarea.usuario_id == usuario_id).all()

    # Validar si existen tareas
    if not tareas:
        raise HTTPException(status_code=404, detail=f"No se encontraron tareas para el usuario con ID {usuario_id}.")
    
    return tareas

@router.get("/", response_model=list[TareaResponse])
async def get_todas_las_tareas(db: Session = Depends(get_db)):
    tareas = db.query(Tarea).all()

    # Validar si hay tareas registradas
    if not tareas:
        raise HTTPException(status_code=404, detail="No hay tareas registradas.")
    
    return tareas

@router.delete("/{tarea_id}", status_code=204)
async def eliminar_tarea_endpoint(tarea_id: int, db: Session = Depends(get_db)):
    tarea = eliminar_tarea(db, tarea_id)
    if tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return {"message": "Tarea eliminada exitosamente."}