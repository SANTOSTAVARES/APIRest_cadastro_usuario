from sqlalchemy.orm import Session
from . import models, schemas, datatypes

def criar_usuario(db: Session, usuario: schemas.UsuarioBase):
    novo_usuario = models.Usuario(nome=usuario.nome, cpf=usuario.cpf, senha=usuario.senha)
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

def get_usuario_by_id(db: Session, id_usuario: int):
    return db.query(models.Usuario).filter(models.Usuario.id == id_usuario).first()

def get_usuario_by_cpf(db: Session, cpf_registrado: str):
    return db.query(models.Usuario).filter(models.Usuario.cpf == cpf_registrado).first()

def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Usuario).offset(skip).limit(limit).all()

def delete_usuario(db: Session, id_cpf: int):
    validar_registro_cpf = get_usuario_by_id(db, id_cpf)
    if validar_registro_cpf:
        db.delete(validar_registro_cpf)
        db.commit()
    
def update_usuario(db: Session, id_cpf: int, valor: datatypes.UpdateUsuarioType):
    validar_registro_cpf = get_usuario_by_id(db, id_cpf)
    if validar_registro_cpf:
        db.query(models.Usuario).filter(models.Usuario.id == id_cpf).update(valor)
        db.commit()
        db.refresh(validar_registro_cpf)
        return validar_registro_cpf