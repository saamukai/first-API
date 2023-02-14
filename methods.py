from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Usuario(BaseModel):
    id: int
    nome: str
    senha: str
    endereco: Optional[str]

users = [
    Usuario(id=1, nome='usuario um', senha='senhadouser1'),
    Usuario(id=2, nome='usuario dois', senha='senha douser2'),
    Usuario(id=3, nome='usuario tres', senha='senhadouser3')
]

@app.post('/cadastrouser')
def cadastrarUser(usuario: Usuario):
    users.append(usuario)
    return 'Usuario Cadastrado'

@app.get('/users')
def listUser():
    return users

@app.get('/user/{id}')
def searchById(id: int):
    for i in users:
        if i.id == id:
            return i

    return "User not exists"
