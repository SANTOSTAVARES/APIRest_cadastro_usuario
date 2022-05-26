from fastapi import FastAPI

from app_usuarios.rotas import usuario_router, login_router, token_router


app = FastAPI(title='API para manutenção de dados de usuário', 
                version='0.1', 
                description='Esta API está utilizando o SQLite para manutenção dos dados.')

app.include_router(usuario_router.router, tags=['usuarios'])
app.include_router(login_router.router, tags=['login'])
app.include_router(token_router.router, tags=['me'])