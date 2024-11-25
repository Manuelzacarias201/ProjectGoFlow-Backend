from sqlalchemy.orm import Session
from models.usuario_models import Usuario

def crear_usuario(db: Session, nombre: str, apellido: str, email: str, password: str, permisos: str):
    nuevo_usuario = Usuario(nombre=nombre, apellido=apellido, email=email, contraseña=password, permisos=permisos)
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

def obtener_usuario_por_email(db: Session, email: str):
    return db.query(Usuario).filter(Usuario.email == email).first()

def obtener_usuarios(db: Session):
    return db.query(Usuario).all()

def eliminar_usuario_por_email(db: Session, email: str):
    try:
        user = db.query(Usuario).filter(Usuario.email == email).first()
        if user:
            db.delete(user)
            db.commit()
            return user  # Usuario eliminado
        return None  # Si no se encuentra el usuario
    except Exception as e:
        db.rollback()  # Rollback en caso de error
        raise Exception(f"Error al eliminar el usuario: {str(e)}")
