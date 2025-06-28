#camada de acesso aos dados, definir os atributos da coleção

from pydantic import  BaseModel
# essa classe vai virar uma coleção quando for inserir os dados
class Jogador(BaseModel):
    jogador_nome: str
    jogador_idade: int
    jogador_time: str
    


