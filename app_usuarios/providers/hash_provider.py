from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'])

def gerar_hash(texto):
    """Converte str para hash."""

    return pwd_context.hash(texto)

def verificar_hash(texto, hash):
    """Verifica se o texto equivale ao hash."""

    return pwd_context.verify(texto, hash)
