from http.client import HTTPException
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import status
from jose import JWTError
from fastapi.security import OAuth2PasswordBearer

from . import models, repositorio_usuario
from .providers import token_provider

from .database import SessionLocal, engine
models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')

class DadosUsuario():

    def __init__(self, session: Session):
        self.session = session
    
    def obter_por_cpf(self, cpf) -> models.Usuario:
        query = select(models.Usuario).where(models.Usuario.cpf == cpf)
        return self.session.execute(query).scalars().first()

def obter_usuario_logado(token: str = Depends(oauth2_schema), db: Session = Depends(get_db)):
    
    try:
        cpf_logado = token_provider.verificar_access_token(token)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token inválido')
    
    if not cpf_logado:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token inválido')
    
    usuario_logado = repositorio_usuario.DadosUsuario(db).obter_por_cpf(cpf_logado)

    if not usuario_logado:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token inválido')

    return usuario_logado
