from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app_usuarios.tipagem_e_dados import schemas
from app_usuarios.providers import hash_provider, token_provider
from app_usuarios.tipagem_e_dados.conexao_db import get_db
from app_usuarios.tipagem_e_dados import repositorio_usuario


router = APIRouter()


@router.post("/login/", response_model=schemas.LoginSucesso)
def logar_usuario(usuario_senha: schemas.LoginData, db: Session = Depends(get_db)):
    logar_senha = usuario_senha.senha
    logar_cpf = usuario_senha.cpf
    usuario = repositorio_usuario.DadosUsuario(db).obter_por_cpf(logar_cpf)
    
    if not usuario:
        raise HTTPException(status_code=400, detail="Esse CPF não está cadastrado.")
    senha_valida = hash_provider.verificar_hash(logar_senha, usuario.senha)
    if not senha_valida:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Senha inválida')
    
    token = token_provider.criar_access_token({"sub": usuario.cpf})
    return schemas.LoginSucesso(pessoa=usuario, access_token=token)
