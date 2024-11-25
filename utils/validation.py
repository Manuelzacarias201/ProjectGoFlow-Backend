import re
from fastapi import HTTPException

def validar_email(email: str):
    """
    Valida si un email tiene un formato correcto.
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        raise HTTPException(status_code=400, detail="Formato de email inválido")
