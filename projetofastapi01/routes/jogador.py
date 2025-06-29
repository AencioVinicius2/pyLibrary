from fastapi import APIRouter
from config.database import conexao
from models.jogador import Jogador
from schemas.jogador import jogador_entidade, lista_jogadores_entidade
from bson import ObjectId

jogador_router = APIRouter()

@jogador_router.get("/")
async def inicio():
    return {"Mensagem":"Teste"}

# Listar jogadores
@jogador_router.get('/jogadores')
async def lista_jogadores():
    return lista_jogadores_entidade(conexao.local.jogador.find())

# Detalhe de um jogador
@jogador_router.get('/jogador/{jogador_id}')
def buscar_jogador_id(jogador_id):
    return jogador_entidade(conexao.local.jogador.find_one(
        {"_id": ObjectId(jogador_id)}
    ))

# insere novos jogadores
@jogador_router.post('/jogadores')
async def cadastra_jogadores(jogador: Jogador):
    conexao.local.jogador.insert_one(dict(jogador))
    return lista_jogadores_entidade(conexao.local.jogador.find())
