secret_key = "secret_key.txt"
algorithm = "algorithm.txt"
token_expire = "token_expire.txt"

def obter_txt(file):
    """Retorna o texto preenchido no arquivo."""

    with open(file, encoding="utf8") as txt_file:
        return txt_file.read()

def teste():
    return int(obter_txt(f".\{token_expire}"))

print(teste())