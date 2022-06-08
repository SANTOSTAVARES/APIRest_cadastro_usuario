# **Sistema de Login com FastAPI**

## Objetivo do Projeto  
Disponibilizar API Rest para cadastro de usuários.

### Aplicações da API Rest
* Realizar CRUD sobre dados de usuário.
* Autenticar login de usuário.
* Gerar o JWT (Jason Web Token)

## Como usar o programa

### Ativação da API Rest
Deve ser ativado o servidor no terminal, por meio do seguinte comando:
    
    uvicorn app_usuarios.main:app --reload

#### Parâmetro da ativação da API Rest
uvicor: servidor
app_usuarios.main: arquivo a ser executado
app: a função a ser executada do arquivo main.py
--reload: monitora as alterações nos arquivos, para que o programa sempre utilize a última versão disponível.

Após isso será criado o arquivo 'sql_app.db' que, é a base de dados em que poderá ser realizado os métodos GET, PUT, POST e DELETE sobre os dados de usuário.

### Documentação sobre métodos disponíveis
A documentação automática estará disponível no endereço a seguir quando o servidor estiver ativo:
http://127.0.0.1:8000/docs

Os dados a serem tratados na base de dados são "nome", "cpf" e "senha". 

**Signup de usuários**
Para realizar um signup de usuário, salvando-o no banco de dados, deve ser utilizado os parâmetros abaixo atuando como cliente. A senha será devidamente criptografada.
URL: http://127.0.0.1:8000/usuarios
Método: Post
Exemplo de conteúdo Json:

    {
        "nome": "Heloisa",
        "cpf": "09078702601",
        "senha": "Admin123"
        }

Exemplo de resposta ao cliente:
    
    {
        "id": 1,
        "nome": "Heloisa",
        "cpf": "09078702610"
        }

**Obter base de dados**
Para consultar todos os registros de usuários na base de dados, deve ser acessado o seguinte endereço:
URL: http://127.0.0.1:8000/usuarios

**Consultar registro por id**
Para consultar o registro de um usuário específico na base de dados, o número referente a ele deve ser inserido como apresentado no link abaixo, caso queira consultar o registro de número 1.
URL: http://127.0.0.1:8000/usuarios/1

**Deletar registro por id**
Para deletar o registro de um usuário específico na base de dados, o número referente a ele deve ser inserido como apresentado no link abaixo, caso queira deletar o registro de número 1.
URL: http://127.0.0.1:8000/usuarios/1
Método: Delete

**Alterar registro por id**
Para alterar o registro de um usuário específico na base de dados, o número referente a ele deve ser inserido como apresentado no link abaixo, e as novas informações devem ser enviadas também como no exemplo.
URL: http://127.0.0.1:8000/usuarios/1
Método: Put
Exemplo de conteúdo Json:

    {
        "nome": "Heloisa Matarazzo",
        "cpf": "09078702601",
        "senha": "Admin123"
        }

**Login de usuários**
Para autenticar o registro de usuário na realização de login, deve ser seguido os parâmetros abaixo.
URL: http://127.0.0.1:8000/login
Método: Post

Exemplo de conteúdo Json:

    {
    "cpf": "09078702603",
        "senha": "1234"
    }

Exemplo de resposta ao cliente:

    {
    "pessoa": {
        "id": 3,
        "nome": "Ana Lú",
        "cpf": "09078702603"
    },
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIwOTA3ODcwMjYwMyIsImV4cCI6MTY1NDIxMjcxM30.OaHXGMxHsqFxW02opMbqyJyBqTrtU2Rk9HS2l-QmVNw"
    }

**Validar JWT (Jason Web Token)**
Para validar se o token é valido, deve ser seguido o exemplo de parâmetros abaixo.
Método: Get
URL: http://127.0.0.1:8000/me
Exemplo de envio de Token

    Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIwOTA3ODcwMjYwMyIsImV4cCI6MTY1NDIxMjcxM30.OaHXGMxHsqFxW02opMbqyJyBqTrtU2Rk9HS2l-QmVNw
