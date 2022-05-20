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

Após isso será criado o arquivo 'sql_app.db' que, é a base de dados em que poderá ser realizado os métodos GET, PUT, POST e deletar sobre os dados de usuário.
Os dados de usuário a serem registrados são (nome; CPF; senha). A senha será devidamente criptografada.
O acesso a API deverá ocorrer pelo endereço a seguir:
http://127.0.0.1:8000/usuarios

A documentação automática estará disponível no endereço a seguir quando o servidor estiver ativo:
http://127.0.0.1:8000/docs


##  Pré-requisitos de sistema
* Python 3.7

Principais pacotes:
* Uvicorn
* SQLAlchemy 
* FastAPI

PIP List:


|Package Version                 |-
|----------------------- |:---------:
|anyio                   3.5.0    
|asgiref                 3.5.0    
|bcrypt                  3.2.2    
|certifi                 2021.10.8
|cffi                    1.15.0   
|charset-normalizer      2.0.12   
|click                   8.1.3    
|colorama                0.4.4    
|coreapi                 2.3.3
|coreschema              0.0.4
|Django                  3.0.14
|django-filter           21.1
|djangorestframework     3.13.1
|djangorestframework-gis 0.18
|drf-yasg                1.20.0
|ecdsa                   0.17.0
|fastapi                 0.77.1
|greenlet                1.1.2
|h11                     0.13.0
|idna                    3.3
|importlib-metadata      4.11.3
|inflection              0.5.1
|itypes                  1.2.0
|Jinja2                  3.1.1
|MarkupSafe              2.1.1
|packaging               21.3
|passlib                 1.7.4
|pip                     22.1
|psycopg2                2.9.3
|pyasn1                  0.4.8
|pycparser               2.21
|pydantic                1.9.0
|pyparsing               3.0.8
|python-jose             3.3.0
|pytz                    2022.1
|requests                2.27.1
|rsa                     4.8
|ruamel.yaml             0.17.21
|ruamel.yaml.clib        0.2.6
|setuptools              57.5.0
|six                     1.16.0
|sniffio                 1.2.0
|SQLAlchemy              1.4.36
|sqlparse                0.4.2
|starlette               0.19.1
|typing_extensions       4.1.1
|uritemplate             4.1.1
|urllib3                 1.26.9
|uvicorn                 0.17.6
|zipp                    3.8.0