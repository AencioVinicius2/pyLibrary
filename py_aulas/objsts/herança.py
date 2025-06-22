# Classe Pai (super classe) - Generalista
class Game:
    total_games = 0 #Váriavel de classe para contar o número total de jogos
    def __init__(self, name="", yearLaunch=0, multiplayer=bool,note=0):
        self.name = name
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note
        Game.total_games += 1
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
        
# Classe derivada (subclasse) - Especializada

class Single_Player_Game(Game):
    def __init__(self, name="", yearLaunch=0, note=0, story_line=""):
        super().__init__(name, yearLaunch, multiplayer=False, note=note)
        self.store_line = story_line
        
    def technical_sheet(self):
        super().technical_sheet()
        print(f"Enredo: {self.story_line}")
        
mult_game = Game("Fortnite", 2017, True, 8.0)
mult_game.technical_sheet()

sing_game = Single_Player_Game("The Last of Us 2", 2020, 9.5,"Emocionante história de sobrevivência e vingança")
sing_game.technical_sheet()