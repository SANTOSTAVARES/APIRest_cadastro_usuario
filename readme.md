# **Sistema de Login com FastAPI**

## Objetivo do Projeto  
Disponibilizar API Rest para cadastro de usuários.

### Aplicações da API Rest
* Realizar CRUD sobre dados de usuário.
* Autenticar registro de usuário.
* Gerar o JWT (Jason Web Token)

## Como usar o programa
Deve ser ativado o servidor no terminal, por meio do seguinte comando:
    uvicorn app_usuarios.main:app --reload

Após isso será criado o arquivo 'sql_app.db' que, é a base de dados em que poderá ser realizado os métodos GET, PUT, POST e DELETE sobre os dados de usuário.
Os dados de usuário a serem registrados são (nome; CPF; senha). A senha será devidamente criptografada.
O acesso a API deverá ocorrer pelo endereço a seguir:
http://127.0.0.1:8000/usuarios

A documentação automática estará disponível no endereço a seguir quando o servidor estiver ativo:
http://127.0.0.1:8000/docs


##  Pré-requisitos de sistema
* Python 3.7

PIP List:

Package            Version
------------------ -------
anyio              3.6.1
asgiref            3.5.2
bcrypt             3.2.2
cffi               1.15.0
click              8.1.3
colorama           0.4.4
ecdsa              0.17.0
fastapi            0.78.0
greenlet           1.1.2
h11                0.13.0
idna               3.3
importlib-metadata 4.11.4
jose               1.0.0
passlib            1.7.4
pip                22.1.1
pyasn1             0.4.8
pycparser          2.21
pydantic           1.9.1
python-jose        3.3.0
rsa                4.8
setuptools         40.8.0
six                1.16.0
sniffio            1.2.0
SQLAlchemy         1.4.36
starlette          0.19.1
typing_extensions  4.2.0
uvicorn            0.17.6
zipp               3.8.0