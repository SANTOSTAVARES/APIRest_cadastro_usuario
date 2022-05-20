from typing import Optional
from pydantic import BaseModel

class UsuarioBase(BaseModel):
    id: Optional[int] = None
    nome: str
    cpf: str
    senha: str

    class Config:
        orm_mode = True

class UsuarioSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    cpf: str

    class Config:
        orm_mode = True

class LoginData(BaseModel):
    cpf: str
    senha: str
    class Config:
        orm_mode = True
""" 
class LoginSucesso(BaseModel):
    usuario: UsuarioSimples
    access_token: str
     """
class LoginSucesso(BaseModel):
    pessoa: UsuarioSimples
    access_token: str
