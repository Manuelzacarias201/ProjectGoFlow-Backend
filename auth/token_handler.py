from passlib.context import CryptContext
from jose import jwt, JWTError

# Configuración del hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Configuración del token
SECRET_KEY = "tu_clave_secreta"  # Cambiar a una variable de entorno en producción
ALGORITHM = "HS256"

def generar_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verificar_password(password_plano: str, password_hash: str) -> bool:
    return pwd_context.verify(password_plano, password_hash)

def generar_token(datos: dict) -> str:
    return jwt.encode(datos, SECRET_KEY, algorithm=ALGORITHM)

def verificar_token(token: str) -> dict:
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        return None
