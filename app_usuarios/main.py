from fastapi import status

from typing import List, Dict
from urllib import response

from fastapi import Depends, FastAPI, HTTPException, Response
from sqlalchemy.orm import Session

from . import crud, models, schemas, repositorio_usuario
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

from .providers import hash_provider, token_provider

app = FastAPI(title='API para manutenção de dados de usuário', versin='0.1', description='Esta API está utilizando o SQLite para manutenção dos dados.')

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

@app.post("/login/", response_model=schemas.LoginSucesso)
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

@app.get('/me/', response_model=schemas.UsuarioSimples)
def me(usuario: schemas.UsuarioBase = Depends(repositorio_usuario.obter_usuario_logado)):
    return usuario