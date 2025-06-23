from fastapi import FastAPI

app = FastAPI()

jogadores = {
    1: {
        "nome":"Rony",
        "idade":26,
        "Time":"Palmeiras"
    },
    2: {
        "nome":"Gustavo",
        "idade":29,
        "Time":"Palmeiras"
    }
}
##uvicorn main:app --reload
@app.get("/")
def inicio():
    return jogadores

#get-jogadores/1 - Path Parameter
@app.get("/get-jogador/{id_jogador}")
def get_jogador(id_jogador:int):
    return jogadores[id_jogador]

#get-jogadores/?id=1 - Query Parameter