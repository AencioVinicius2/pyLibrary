from fastapi import APIRouter
from config.database import conexao
from models.jogador import Jogador
from schemas.jogador import jogador_entidade, lista_jogadores_entidade

jogador_router = APIRouter()

@jogador_router.get("/")
async def inicio():
    return {"Mensagem":"Teste"}

@jogador_router.get('/jogadores')
async def lista_jogadores():
    return lista_jogadores_entidade(conexao.local.jogador.find())

#insere novos jogadores
@jogador_router.post('/jogadores')
async def cadastra_jogadores(jogador: Jogador):
    conexao.local.jogador.insert_one(dict(jogador))
    return lista_jogadores_entidade(conexao.local.jogador.find())
