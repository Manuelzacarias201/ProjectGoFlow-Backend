from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    nombre: str
    apellido: str
    email: EmailStr
    password: str
    permisos: str = "Persona"  # Valor predeterminado

class UserLogin(BaseModel):
    email: EmailStr
    password: str
