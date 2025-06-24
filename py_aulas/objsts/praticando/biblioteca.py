class Biblioteca(object):
    def __init__ (self, nome, ativo):
        self.nome = nome
        self.ativo = ativo
    

biblioteca_cidade = Biblioteca('Biblioteca da cidade', True)
biblioteca_shopping = Biblioteca('Biblioteca do shopping', True)
bibliotecas = [biblioteca_cidade, biblioteca_shopping]

print("----------------------------------------------------------------------------------------------------------------------------------")
for tecas in bibliotecas:
    print(vars(tecas))
print("----------------------------------------------------------------------------------------------------------------------------------")    
print(vars(biblioteca_cidade))