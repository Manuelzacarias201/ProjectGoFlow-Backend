from auth.token_handler import generar_password_hash
from repositories.usuario_respositories import crear_usuario as repo_crear_usuario, obtener_usuarios
from repositories.usuario_respositories import eliminar_usuario_por_email
async def crear_usuario(user_data, db):
    hashed_password = generar_password_hash(user_data.password)
    return repo_crear_usuario(db, user_data.nombre, user_data.apellido, user_data.email, hashed_password, user_data.permisos)

async def obtener_todos_usuarios(db):
    return obtener_usuarios(db)

def eliminar_usuario_por_email_service(db, email):
    return eliminar_usuario_por_email(db, email)  # Sin `await`