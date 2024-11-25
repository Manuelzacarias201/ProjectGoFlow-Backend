from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# URL de conexión a la base de datos
# Nota: Cambiar las credenciales por variables de entorno en producción para mayor seguridad
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://administrador:426855@localhost:5432/modulos_base")

# Configuración del motor de base de datos
engine = create_engine(
    DATABASE_URL,
    echo=True,  # Muestra las consultas SQL en la consola (útil para depuración)
    pool_pre_ping=True,  # Verifica la conexión antes de usarla
    pool_size=10,  # Número máximo de conexiones en el pool
    max_overflow=20  # Conexiones extra si el pool está lleno
)

# Configuración de la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base para modelos ORM
Base = declarative_base()

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
