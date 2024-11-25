from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.usuario_schemas import UserCreate, UserLogin
from services.usuario_services import crear_usuario, obtener_todos_usuarios, eliminar_usuario_por_email_service
from services.auth_service import autenticar_usuario
from config.db_config import get_db

router = APIRouter()

@router.post("/register")
async def registrar_usuario(user: UserCreate, db: Session = Depends(get_db)):
    nuevo_usuario = await crear_usuario(user, db)
    return {"message": "Usuario registrado exitosamente", "data": nuevo_usuario}

@router.post("/login")
async def iniciar_sesion(user: UserLogin, db: Session = Depends(get_db)):
    token = await autenticar_usuario(user.email, user.password, db)
    if not token:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return {"message": "Inicio de sesión exitoso", "token": token}

@router.get("/users")
async def listar_usuarios(db: Session = Depends(get_db)):
    return await obtener_todos_usuarios(db)

@router.delete("/delete/{email}")
async def delete_user_by_email(email: str, db: Session = Depends(get_db)):
    try:
        user = eliminar_usuario_por_email_service(db, email)  # Sin `await`
        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
        return {"message": "Usuario eliminado exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")