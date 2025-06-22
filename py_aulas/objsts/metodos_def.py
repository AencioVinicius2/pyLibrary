class Game:
    def __init__(self, name="", yearLaunch=0, multiplayer=bool,note=0):
        self.name = name
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note
        self.total_evaluation = 0
        self.evaluators = 0
    
    def __str__(self):
        return f"Game: {self.name}"

    def technical_sheet(self):
        print("##Dados do jogo")
        print(f"Nome do jogo: {self.name}")
        print(f"Ano de lançamento: {self.yearLaunch}")
        print(f"Modo multiplayer: {"Sim" if self.multiplayer else "Não"}")
        print(f"Avaliação do jogo: {self.note}")

    def evaluate(self, note):
        self.total_evaluation += note
        self.evaluators += 1
        
    def average(self):
        print(f"Média do jogo {self.name}: {(self.total_evaluation / self.evaluators):.2f}")
        

#Primeiro jogo
game1 = Game("The Witcher 3", 2015, False, 9.5)

print("###Dados do jogo###")
print(f"Nome do jogo: {game1.name}\nAno de lançamento: {game1.yearLaunch}")
print("-----------------------------------------------------------------------")
game1.technical_sheet()
print("-----------------------------------------------------------------------")
game1.evaluate(9.0)
game1.evaluate(7.5)
game1.average()
