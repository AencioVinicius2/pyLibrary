class Biblioteca(object):
    bibliotecas = []
    def __init__ (self, nome, ativo):
        self.nome = nome
        self.ativo = ativo
        Biblioteca.bibliotecas.append(self)
    def __str__(self):
        return self.nome
    
    def listar_blibliotecas():
        for i in Biblioteca.bibliotecas:
            print(bibliotecas.nome)
    def alterna_estado(self):
        self.ativo = not self.ativo
    
    @property
    def ativo(self):
        return "ativada" if self.ativo else "desativada"
                    
        
biblioteca_cidade = Biblioteca("Biblioteca da cidade", True)
biblioteca_shopping = Biblioteca("Biblioteca do shopping", True)
print(biblioteca_cidade)

Biblioteca.listar_blibliotecas()

    
