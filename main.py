from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {'mensagem': 'Testando Rotas - Home'}


@app.get("/cadastro")
def cadastro():
    return {'mensagem': 'Testando Rotas - Cadastro'}


@app.get("/login")
def login():
    return {'mensagem': 'Testando Rotas - Login'}
