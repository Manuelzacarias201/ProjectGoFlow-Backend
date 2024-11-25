from repositories.tarea_repositories import (
    crear_tarea,
    obtener_tareas,
    obtener_tarea_por_id,
    actualizar_tarea,
    eliminar_tarea,
)

async def crear_nueva_tarea(db, tarea_data):
    return crear_tarea(
        db,
        nombre=tarea_data.nombre,
        descripcion=tarea_data.descripcion,
        estado=tarea_data.estado,
        usuario_id=tarea_data.usuario_id,
    )

async def obtener_lista_tareas(db):
    return obtener_tareas(db)

async def obtener_tarea_detalle(db, tarea_id):
    return obtener_tarea_por_id(db, tarea_id)

async def actualizar_tarea_existente(db, tarea_id, tarea_data):
    return actualizar_tarea(db, tarea_id, tarea_data.dict(exclude_unset=True))

async def eliminar_tarea_por_id(db, tarea_id):
    return eliminar_tarea(db, tarea_id)
