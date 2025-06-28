#camada de acesso aos dados, definir os atributos da coleção

from pydantic import  BaseModel

class Jogador(BaselModel):
    jogador_name: str
    jogador_idade: int
    jogador_time: str
    


