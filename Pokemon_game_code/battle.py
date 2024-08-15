# BATTLE SEQUENCE LOGIC

import random
from pokemon import get_wild_pokemon, create_starter_pokemon

def battle(starter_pokemon_name):
    starter_pokemon = create_starter_pokemon(starter_pokemon_name)
    starter_health = starter_pokemon.hp
    wild_pokemon = random.choice(get_wild_pokemon()) # Randomly chooses a pokemon from the list returned by the function
    wild_pokemon_health = wild_pokemon.hp
    print(f"A wild {wild_pokemon.name} appeared! (It has {wild_pokemon_health} HP) Go {starter_pokemon.name}!")

    def apply_effect_move(attacker, defender, move_name ,effect):
        if defender.effect_move_counter < 2: # Check if the effect has been applied less than twice
            if effect == "lower attack":
                defender.attack_modifier -= 5  # Decrease opposite's attack modifier by 5
                defender.apply_attack_modifier()  # Apply the modifier to attack moves
                print(f"\n{attacker.name} used {move_name.upper()}!")
                print(f"{defender.name}'s attack fell!")
            elif effect == "lower defence":
                attacker.attack_modifier += 5  # Increase attacker's attack modifier by 5 (same as defender having low defence)
                attacker.apply_attack_modifier()  # Apply the modifier to attack moves
                print(f"\n{attacker.name} used {move_name.upper()}!")
                print(f"{defender.name}'s defence fell!")
            elif effect == "increase attack":
                attacker.attack_modifier += 5
                attacker.apply_attack_modifier()
                print(f"\n{attacker.name} used {move_name.upper()}!")
                print(f"{attacker.name}'s attack rose!")
            defender.effect_move_counter += 1  # Increment the effect move counter everytime effect is used
        else:
            print(f"\n{attacker.name} tried to use {move_name.upper()}, but it had no effect!")
            # Therefore for either starter or wild pokemon, they can only use effect twice (to avoid having a pokemon
            # do zero damage and get stuck)

    def wild_pokemon_attack(starter_health):
        all_moves = list(wild_pokemon.attack_moves.keys()) + list(wild_pokemon.effect_moves.keys()) # Combine both dict.
        wild_pokemon_move = random.choice(all_moves)
        # Get a random move name from list of all move names (which are keys in both dict)
        if wild_pokemon_move in list(wild_pokemon.attack_moves.keys()):
            wild_pokemon_damage = wild_pokemon.attack_moves[wild_pokemon_move]
            # Access damage value from the dict. using key as wild_pokemon_move
            starter_health = starter_health - wild_pokemon_damage
            print(f"\n{wild_pokemon.name} used {wild_pokemon_move}!")
            print(f"{starter_pokemon.name} lost {wild_pokemon_damage} HP! {starter_pokemon.name} has {starter_health} HP left.")
        elif wild_pokemon_move in wild_pokemon.effect_moves:
            effect = wild_pokemon.effect_moves[wild_pokemon_move]
            apply_effect_move(wild_pokemon, starter_pokemon, wild_pokemon_move, effect)
        return (starter_health)  # Returns updated starter's health. MUST be at the end of func. so something is returned

    potion_counter = 2

    while starter_health > 0 and wild_pokemon_health > 0:
        all_moves = list(starter_pokemon.attack_moves.keys()) + list(starter_pokemon.effect_moves.keys())
        print(f"\nWhat will {starter_pokemon.name} do? Options: {', '.join(all_moves)} or use a POTION")
        # This joins the move names (saved as keys in the dict) into a single string separated by commas
        my_move = input("> Move: " )

        if my_move.upper() in list(starter_pokemon.attack_moves.keys()): # Checks if move is in list of attack move keys
            move_damage = starter_pokemon.attack_moves[my_move.upper()]
            # value for move damage is taken from dict, looking for key that matches players input
            wild_pokemon_health = wild_pokemon_health - move_damage
            print(f"\n{starter_pokemon.name} used {my_move.upper()}!")
            print(f"{wild_pokemon.name} lost {move_damage} HP! It has {wild_pokemon_health} HP left.")
            if wild_pokemon_health <= 0:
                print(f"\n{wild_pokemon.name} has fainted. You and {starter_pokemon.name} have won the battle!")
                break
        elif my_move.upper() in list(starter_pokemon.effect_moves.keys()):
            effect = starter_pokemon.effect_moves[my_move.upper()]
            apply_effect_move(starter_pokemon, wild_pokemon, my_move, effect)
        elif my_move.upper() == "POTION":
            if potion_counter > 0:
                potion_counter = potion_counter - 1
                hp_max = 50 # Maximum starter's health is 50
                previous_health = starter_health # To keep track of prev. health to see how much was restored
                starter_health = min(starter_health + 15, hp_max)
                # min ensures result is the smaller of either 'starter_health + 20' or 'hp_max'
                health_restored = starter_health - previous_health
                print(f"\n{starter_pokemon.name} used a POTION! You have {potion_counter} potion/s left.")
                print(f"{starter_pokemon.name} restored {health_restored} HP! It now has {starter_health} HP.")
            else:
                print("\nYou have no more potions to use.")
                continue # Skip the rest of the loop and prompt for the move again
        else:
            print("\n* Please make sure you type in the option correctly. *")
            continue  # Skip the rest of the loop and prompt for the move again

        if wild_pokemon_health > 0:
            # THIS runs when all the above gets checked. If player's move is one of the options, then the if/elif
            # statements progress and AFTER, this code runs. If the player types in something else, "else" progresses
            starter_health = wild_pokemon_attack(starter_health)
            # NEED to call this function and save it as starter_health in order to keep the updated variable
            if starter_health <= 0:
                print(f"\n{starter_pokemon.name} has fainted. You have lost the battle.")
                break
