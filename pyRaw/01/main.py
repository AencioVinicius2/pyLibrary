from random import randint

list_npcs = []

player = {
    "name": "Aencio",
    "level": 1,
    "exp": 0,
    "exp_max": 50,
    "hp": 100,
    "hp_max": 100,
    "damage": 25,
}

def create_npcs(level):

    new_npc = {
        "name": f"Monster #{level}",
        "level": level,
        "damage": 5 * level,
        "hp": 100 * level,
        "exp": 7 * level,
    }

    return new_npc


def generate_npcs(n_npcs):
    for x in range(n_npcs):
        new_npc = create_npcs(x + 1)
        list_npcs.append(new_npc)

     
       
def show_npcs():
    for npc in list_npcs:
        print(
            f"Name: {npc["name"]} // Level: {npc["level"]} // Damage: {npc["damage"]} // Hp: {npc["hp"]}"
        )

def attack_npc(npc):
    npc["hp"] -= player["damage"]
# attack_player(npc) - player:hp - npc:damage


generate_npcs(5)
show_npcs()

selected_npc = list_npcs[0]

print("Npc selected:", selected_npc)
attack_npc(selected_npc)

print("Npc attacking:", selected_npc)
