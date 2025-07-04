from fastapi import APIRouter
from config.database import conexao
from models.jogador import Jogador
from schemas.jogador import jogador_entidade, lista_jogadores_entidade
from bson import ObjectId

#@see https://www.mongodb.com/docs/languages/python/pymongo-driver/current/crud/

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
async def buscar_jogador_id(jogador_id):
    return jogador_entidade(conexao.local.jogador.find_one(
        {"_id": ObjectId(jogador_id)}
    ))

# insere novos jogadores
@jogador_router.post('/jogadores')
async def cadastra_jogadores(jogador: Jogador):
    conexao.local.jogador.insert_one(dict(jogador))
    return lista_jogadores_entidade(conexao.local.jogador.find())

#atualiza jogador
@jogador_router.put('/jogadores/{jogador_id}')
async def atualiza_jogador(jogador_id, jogador: Jogador):
    conexao.local.jogador.find_one_and_update(
        {
            "_id": ObjectId(jogador_id)
        },
        {
            "$set": dict(jogador)
        }
    )
    return jogador_entidade(
        conexao.local.jogador.find_one(
            {
                "_id": ObjectId(jogador_id)
            }
        )
    )

#deleta jogador
@jogador_router.delete('/jogador/{jogador_id}')
async def deleta_jogador(jogador_id):
    conexao.local.jogador.delete_one(
        {
            "_id": ObjectId(jogador_id)
        }
    )
    return {"Mensagem":"Jogador Deletado!"}