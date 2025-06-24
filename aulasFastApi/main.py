from fastapi import FastAPI
#usado para manipular e validar dados simples @see https://docs.pydantic.dev/latest/#pydantic-examples
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

jogadores = {
    1: {
        "nome":"Rony",
        "idade":26,
        "time":"Palmeiras"
    },
    2: {
        "nome":"Gustavo",
        "idade":29,
        "time":"Palmeiras"
    }
}

class Jogador(BaseModel):
    nome: str
    idade: int
    time: str

class Atualiza_Jogador(BaseModel):
    nome: Optional[str] = None
    idade: Optional[int] = None
    time: Optional[str] = None

##uvicorn main:app --reload
@app.get("/")
def inicio():
    return jogadores

#get-jogadores/1 - Path Parameter
@app.get("/get-jogador/{id_jogador}")
def get_jogador(id_jogador:int):
    return jogadores[id_jogador]

#get-jogadores/?id=1 - Query Paramete
#get-jogador-time?time="nometime"
@app.get("/get-jogador-time")
def get_jogador_time(time:str):
    for jogador_id in jogadores:
        if jogadores[jogador_id]["time"] == time:
            return jogadores[jogador_id]
    return {"Dados": "Não foi encontrado"}

@app.post("/cadastra-jogador/{jogador_id}")
def cadastra_jogador(jogador_id: int, jogador:Jogador):
    if jogador_id in jogadores:
        return {"Erro":"Jogador já existe"}
    jogadores[jogador_id] = jogador
    return jogadores[jogador_id]

@app.put("/atualiza-jogador{jogador_id}")
def atualiza_jogadores(jogador_id: int, jogador: Atualiza_Jogador):
    if not jogador_id in jogadores:
        return {"Erro":"Jogador não existe"}
    if jogador.nome != None:
        jogadores[jogador_id]["nome"] = jogador.nome
    if jogador.idade != None:
        jogadores[jogador_id]["idade"] = jogador.idade
    if jogador.time != None:
        jogadores[jogador_id]["time"] = jogador.time
    return jogadores[jogador_id]

@app.delete("/deleta-jogador{jogador_id}")
def deleta_jogadores(jogador_id: int):
    if not jogador_id in jogadores:
        return {"Erro":"Jogador não existe"}
    jogadores.pop(jogador_id)
    return {"Mensagem:Jogador deletado!"}