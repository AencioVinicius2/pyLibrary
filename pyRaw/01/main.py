from random import randint

list_npcs = []

list_player = {
    "name": "Aencio",
    "level": 1,
    "exp": 0,
    "exp_max": 50,
    "hp": 100,
    "hp_max": 100,
    "damage": 25,
}

def create_npcs():
    level = randint(0,50)

    new_npc = {
        "name": f"Monster #{level}",
        "level": level,
        "demage": 5 * level,
        "hp": 100 * level,
        "exp": 7 * level,
    }

    return new_npc


def generate_npcs(n_npcs):
    for x in range(n_npcs):
        new_npc = create_npcs()
        list_npcs.append(new_npc)

     
       
def show_npcs():
    for npc in list_npcs:
        print(
            f"Name: {npc["name"]} // Level: {npc["level"]} // Demage: {npc["demage"]} // Hp {npc["hp"]}"
        )

# Attack npc


generate_npcs(5)
show_npcs()

