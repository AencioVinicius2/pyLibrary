class Biblioteca(object):
    bibliotecas = []
    def __str__(self):
        return self.nome
    
    @classmethod
    def listar_blibliotecas(cls):
        print(f"{'Nome da biblioteca'.ljust(25)} | {'Status'}")
        for i in Biblioteca.bibliotecas:
            print(f"{bibliotecas.nome} | {Biblioteca.ativo} ")
    
    def alterna_estado(self):
        self.ativo = not self.ativo
    
    @property
    def ativo(self):
        return "ativada" if self.ativo else "desativada"

        
biblioteca_cidade = Biblioteca("Biblioteca da cidade", True)
#biblioteca_shopping = Biblioteca("Biblioteca do shopping")
print(biblioteca_cidade)

Biblioteca.listar_blibliotecas

    
