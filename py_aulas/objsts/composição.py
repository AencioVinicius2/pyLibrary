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
# "Composição tem um" a classe Game_Studio pode ter atributos que são de outras classes
class Game_studio:
    def __init__(self,name=""):
        self.name = name
        self.games = []
        
    def add_game(self, game):
        self.games.append(game) # composição: Estúdio tem um (ou mais) game(s)
    
    def evaluate_studio_quality(self):
        total_notes = sum(game.note for game in self.games)  
        num_games = len(self.games)
        if num_games == 0:
            print(f"O stúdio {self.name} ainda não lançou jogo")
        else:
            average_note = total_notes / num_games
            print(f"Avaliação média dos jogos do stúdio {self.name}: {average_note:.2f}")

game1 = Game("The Last of Us 2", 2020, True, 9.5)

studio = Game_studio("AWPL")
studio.add_game(game1)

studio.evaluate_studio_quality()
