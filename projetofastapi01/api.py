from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"Mensagem":"Inicializando com FARM Stack"} #uvicorn api:app --reload