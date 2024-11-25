from fastapi import FastAPI
from controllers.usuario_controller import router as user_router
from controllers.tarea_controller import router as tarea_router
from controllers.asignacion_controller import router as asignacion_router
from config.db_config import Base, engine

app = FastAPI()

# Crear tablas
Base.metadata.create_all(bind=engine)

# Incluir rutas
app.include_router(user_router, prefix="/api/users", tags=["Usuarios"])

app.include_router(asignacion_router, prefix="/api", tags=["Asignaciones"])

app.include_router(tarea_router, prefix="/api/tareas", tags=["Tareas"])