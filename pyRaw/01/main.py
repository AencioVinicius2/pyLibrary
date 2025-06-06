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
        "hp_max": 100 * level,
        "exp": 7 * level,
    }

    return new_npc


def generate_npcs(n_npcs):
    for x in range(n_npcs):
        new_npc = create_npcs(x + 1)
        list_npcs.append(new_npc)

def show_npcs():
    for npc in list_npcs:
       show_npc(npc)

def show_npc(npc):
        print(
            f"Name: {npc["name"]} // Level: {npc["level"]} // Damage: {npc["damage"]} // Hp: {npc["hp"]}"
        )

def show_player():
        print(
            f"Name: {player["name"]} // Level: {player["level"]} // Damage: {player["damage"]} // Hp: {player["hp"]}/{player["max_hp"]} // EXP: {player["exp"]}/{player["max_exp"]}"
        )

def reset_player():
    player["hp"] = player["hp_max"]
        
def reset_npc(npc):
    npc["hp"] = npc["hp_max"]

def level_up():
    if player["exp"] >= player["exp_max"]:
        player["level"] += 1
        player["exp"] = 0
        player["exp_max"] = player["exp_max"] * 2
        player["hp_max"] += 20

def start_battle(npc):
    while player["hp"] > 0 and npc["hp"]:
        attack_npc(npc)
        attack_player(selected_npc)
        show_battle_info(npc)   
    if player["hp"] > 0:
        print(f"{player["name"]} wins the battle and gains {npc["exp"]} of XP")
        player['exp'] += npc['exp']
    else:
        print(f"The {npc["name"]} wins the battle")

    level_up()
    reset_player()
    reset_npc(npc)

def attack_npc(npc):
    npc["hp"] -= player["damage"]

def attack_player(npc):
    player["hp"] -= npc["damage"]

def show_battle_info(npc):
    print(f"Player HP: {player["hp"]}/{player["hp_max"]}")
    print(f"NPC HP: {npc["name"]}: {npc["hp"]}/{npc["hp_max"]}")
    print('-------------------------\n')

generate_npcs(5)

selected_npc = list_npcs[0]
start_battle(selected_npc)

