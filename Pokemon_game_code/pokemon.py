# POKEMON CHARACTERISTICS and choosing the random wild pokemon

import random

class pokemon_info:
    def __init__(self, name, hp, move1, move1_damage, move2, move2_damage, move3, move3_effect):
        self.name = name
        self.type = type
        self.hp = hp
        self.attack_moves = {move1.upper(): move1_damage,
            move2.upper(): move2_damage}
            # Using a dict. called 'attack_moves' in the class allows for a pairing between 2 attributes while still a class
        self.effect_moves = {move3.upper(): move3_effect}
        self.attack_modifier = 0 # Although not a parameter in init method, you can still add attr. in the class
        self.effect_move_counter = 0  # Initialize the effect move counter. Goal: only be able to use effect twice


    def apply_attack_modifier(self):
    # Function that increases/decreases each move damage for a pokemon and remains UPDATED throughout battle
        for move in self.attack_moves:
            self.attack_moves[move] += self.attack_modifier

def get_wild_pokemon():
    random_hp = random.randint(50,75)
    poochyena = pokemon_info("POOCHYENA", random_hp, "TACKLE", 15, "SCRATCH", 20, "GROWL", "lower attack")
    zigzagoon = pokemon_info("ZIGZAGOON", random_hp, "SCRATCH", 20, "HEADBUTT", 25, "TAIL WHIP", "lower defence")
    wurmple = pokemon_info("WURMPLE", random_hp, "TACKLE", 15, "POISON STING", 20, "HOWL", "increase attack")
    wingull = pokemon_info("WINGULL", random_hp, "WATER GUN", 15, "PECK", 25, "SCREECH", "lower defence")
    lotad = pokemon_info("LOTAD", random_hp, "ASTONISH", 15, "ABSORB", 20, "GROWL", "lower attack")
    wild_pokemon_list = [poochyena, zigzagoon, wurmple, wingull, lotad]
    return wild_pokemon_list

def create_starter_pokemon (starter_pokemon):
    if starter_pokemon == "torchic":
       starter_pokemon = pokemon_info("TORCHIC",50, "SCRATCH",20, "EMBER", 30, "GROWL", "lower attack")
       return starter_pokemon
    if starter_pokemon == "mudkip":
       starter_pokemon = pokemon_info("MUDKIP",50, "TACKLE",20, "WATER GUN", 30, "TAIL WHIP", "lower defence")
       return starter_pokemon
    if starter_pokemon == "treecko":
       starter_pokemon = pokemon_info("TREECKO",50, "ABSORB",20, "POUND", 30, "HOWL", "increase attack")
       return starter_pokemon