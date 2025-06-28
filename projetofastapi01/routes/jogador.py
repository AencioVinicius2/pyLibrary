from fastapi import APIRouter
from config.database import conection
from models.jogador import Jogador

jogador_router = APIRouter()

@jogador_router.get("/")
async def inicio():
    return {"Mensagem":"Teste"}

@jogador_router.get('/jogadores')
async def lista_jogadores():
    return conection.local.jogador.find()