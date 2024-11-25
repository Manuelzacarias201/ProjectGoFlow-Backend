from auth.token_handler import verificar_password, generar_token
from repositories.usuario_respositories import obtener_usuario_por_email

async def autenticar_usuario(email: str, password: str, db):
    usuario = obtener_usuario_por_email(db, email)
    if not usuario or not verificar_password(password, usuario.contraseña):
        return None

    token_data = {"id": usuario.id, "email": usuario.email, "permisos": usuario.permisos}
    return generar_token(token_data)
