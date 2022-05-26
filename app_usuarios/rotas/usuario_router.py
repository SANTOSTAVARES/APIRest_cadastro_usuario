from fastapi import APIRouter, Response

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app_usuarios.tipagem_e_dados import schemas, crud
from app_usuarios.providers import hash_provider
from app_usuarios.tipagem_e_dados.conexao_db import get_db


router = APIRouter()


@router.post("/usuarios/", response_model=schemas.UsuarioBase)
def post_usuario(usuario_novo: schemas.UsuarioBase, db: Session = Depends(get_db)):
    evitar_duplicidade = crud.get_usuario_by_cpf(db, cpf_registrado=usuario_novo.cpf)
    if evitar_duplicidade:
        raise HTTPException(status_code=400, detail="Esse CPF já está cadastrado.")
    usuario_novo.senha = hash_provider.gerar_hash(usuario_novo.senha)
    return crud.criar_usuario(db=db, usuario=usuario_novo)
     
@router.get("/usuarios/", response_model=List[schemas.UsuarioBase])
def get_usuarios_(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    usuarios_registrados = crud.get_usuarios(db, skip=skip, limit=limit)
    return usuarios_registrados

@router.get("/usuarios/{usuario_id}", response_model=schemas.UsuarioBase)
def get_usuario(usuario_id: int, db: Session = Depends(get_db)):
    buscar_usuario = crud.get_usuario_by_id(db, id_usuario=usuario_id)
    if buscar_usuario is None:
        raise HTTPException(status_code=404, detail="Esse CPF não está registrado.")
    return buscar_usuario

@router.delete("/usuarios/{id_cpf}")
def deletar_usuario(id_cpf: str, db: Session = Depends(get_db)):
    excluir_cpf = crud.get_usuario_by_id(db, id_usuario=id_cpf)
    if excluir_cpf:
        crud.delete_usuario(db, id_cpf=id_cpf)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Não foi encontrado o CPF.")

@router.put("/usuarios/{id_cpf}")
def put_usuario(id_cpf: int, usuario: schemas.UsuarioBase, db: Session = Depends(get_db)):
    buscar_usuario = crud.get_usuario_by_id(db, id_usuario=id_cpf)
    if buscar_usuario:
        crud.update_usuario(db, id_cpf, {x: y for x,y in usuario if y})
        return Response(status_code=status.HTTP_201_CREATED)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não foi encontrado o id {id_cpf}")