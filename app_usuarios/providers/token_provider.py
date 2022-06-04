from datetime import datetime, timedelta
from jose import jwt

def obter_txt(file):
    """Retorna o texto preenchido no arquivo."""

    with open(file, encoding="utf8") as txt_file:
        return txt_file.read()

token_expire = int(obter_txt("app_usuarios\\providers\\token_expire.txt"))
secret_key = obter_txt("app_usuarios\\providers\\secret_key.txt")
algorithm_code = obter_txt("app_usuarios\\providers\\algorithm.txt")

def criar_access_token(data: dict):

    dados = data.copy()
    expiracao = datetime.utcnow() + timedelta(minutes=token_expire)
    dados.update({'exp': expiracao})
    token_jwt = jwt.encode(dados, secret_key, algorithm=algorithm_code)
    return token_jwt

def verificar_access_token(token: str):
    carga = jwt.decode(token, secret_key, algorithms=[algorithm_code])
    return carga.get('sub')
