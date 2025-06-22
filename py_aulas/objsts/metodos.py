class Game:
    def __init__(self, name="", yearLaunch=0, multiplayer=bool,note=0):
        self.name = name
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note
    
    def __str__(self):
        return f"Game: {self.name}"

#Primeiro jogo
game1 = Game("The Witcher 3", 2015, False, 9.5)

print("###Dados do jogo###")
print(f"Nome do jogo: {game1.name}\nAno de lançamento: {game1.yearLaunch}")
