from fastapi import FastApi
from routes.jogador import jogador_router

app = FastApi()

app.include_router(jogador_router)