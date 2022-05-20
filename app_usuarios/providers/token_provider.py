from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = 'd56b699830e77ba53855679cb1d252da'
ALGORITHM = 'HS256'
EXPIRES_IN_MIN = 60

def criar_access_token(data: dict):
    dados = data.copy()
    expiracao = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)

    dados.update({'exp': expiracao})

    token_jwt = jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt

def verificar_access_token(token: str):
    carga = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return carga.get('sub')