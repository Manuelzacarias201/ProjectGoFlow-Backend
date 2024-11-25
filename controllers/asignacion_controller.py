from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from schemas.asignacion_schemas import AsignacionCreate
from services.asignacion_services import crear_asignacion, obtener_asignaciones, obtener_asignaciones_por_usuario
from models.asignacion_model import  AsignacionResponse  # Importa desde el nuevo archivo
from config.db_config import get_db  # Asegúrate de tener una función para obtener la sesión de la base de datos

router = APIRouter()

# Ruta para crear una asignación
@router.post("/asignaciones/", response_model=AsignacionResponse)
async def crear_asignacion_endpoint(asignacion: AsignacionCreate, db: Session = Depends(get_db)):
    # Llama a la función para crear la asignación
    asignacion_creada = crear_asignacion(db, asignacion)
    return asignacion_creada

# Ruta para obtener todas las asignaciones
@router.get("/", response_model=List[AsignacionResponse])
async def obtener_asignaciones_view(db: Session = Depends(get_db)):
    return obtener_asignaciones(db)

# Ruta para obtener asignaciones de un usuario específico
@router.get("/usuario/{usuario_asignado_id}", response_model=List[AsignacionResponse])
async def obtener_asignaciones_por_usuario_view(usuario_asignado_id: int, db: Session = Depends(get_db)):
    return obtener_asignaciones_por_usuario(db, usuario_asignado_id)
