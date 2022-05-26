from fastapi import APIRouter, Depends

from app_usuarios.tipagem_e_dados import schemas
from app_usuarios.tipagem_e_dados import repositorio_usuario


router = APIRouter()


@router.get('/me/', response_model=schemas.UsuarioSimples)
def me(usuario: schemas.UsuarioBase = Depends(repositorio_usuario.obter_usuario_logado)):
    return usuario