from fastapi import FastAPI
from routes.jogador import jogador_router
from fastapi.middleware.cors import CORSMiddleware

cliente_app = [
    "http://localhost:3000"
]

app = FastAPI()

app.include_router(jogador_router)

#habilitar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins = cliente_app,
    allo_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)