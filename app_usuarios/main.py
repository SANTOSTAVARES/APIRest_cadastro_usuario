from fastapi import status

from typing import List, Dict
from urllib import response

from fastapi import Depends, FastAPI, HTTPException, Response
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

from .providers import hash_provider

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/usuarios/", response_model=schemas.UsuarioBase)
def post_usuario(usuario_novo: schemas.UsuarioBase, db: Session = Depends(get_db)):
    evitar_duplicidade = crud.get_usuario_by_cpf(db, cpf_registrado=usuario_novo.cpf)
    if evitar_duplicidade:
        raise HTTPException(status_code=400, detail="Esse CPF já está cadastrado.")
    usuario_novo.senha = hash_provider.gerar_hash(usuario_novo.senha)
    return crud.criar_usuario(db=db, usuario=usuario_novo)

@app.post("/login/", response_model=schemas.LoginData)
def logar_usuario(usuario_senha: schemas.LoginData, db: Session = Depends(get_db)):
    consultar_cpf = crud.get_usuario_by_cpf(db, cpf_registrado=usuario_senha.cpf)
    print(consultar_cpf.cpf)
    print(consultar_cpf.senha)
    if not consultar_cpf:
        raise HTTPException(status_code=400, detail="Esse CPF não está cadastrado.")
    senha_valida = hash_provider.verificar_hash(usuario_senha.senha, consultar_cpf.senha)
    if not senha_valida:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Senha inválida')

@app.get("/usuarios/", response_model=List[schemas.UsuarioBase])
def get_usuarios_(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    usuarios_registrados = crud.get_usuarios(db, skip=skip, limit=limit)
    return usuarios_registrados

@app.get("/usuarios/{usuario_id}", response_model=schemas.UsuarioBase)
def get_usuario(usuario_id: int, db: Session = Depends(get_db)):
    buscar_usuario = crud.get_usuario_by_id(db, id_usuario=usuario_id)
    if buscar_usuario is None:
        raise HTTPException(status_code=404, detail="Esse CPF não está registrado.")
    return buscar_usuario

@app.delete("/usuarios/{id_cpf}")
def deletar_usuario(id_cpf: str, db: Session = Depends(get_db)):
    excluir_cpf = crud.get_usuario_by_id(db, id_usuario=id_cpf)
    if excluir_cpf:
        crud.delete_usuario(db, id_cpf=id_cpf)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Não foi encontrado o CPF.")

@app.put("/usuarios/{id_cpf}")
def put_usuario(id_cpf: int, usuario: schemas.UsuarioBase, db: Session = Depends(get_db)):
    buscar_usuario = crud.get_usuario_by_id(db, id_usuario=id_cpf)
    if buscar_usuario:
        crud.update_usuario(db, id_cpf, {x: y for x,y in usuario if y})
        return Response(status_code=status.HTTP_201_CREATED)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não foi encontrado o id {id_cpf}")