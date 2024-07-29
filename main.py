# INTRO TO THE GAME - Choosing starting Pokemon
print("\nLet's play POKéMON! There are 3 starting pokémon for you to choose from: TORCHIC, TREECKO and MUDKIP.")
starter_info = input("> Please type which pokémon you would like more info on: ")

def starter_pokemon_choice(starter_info): #argument (data) given in function is starter_info
    while True: #Just means it runs indefinitely until a break in loop
        if starter_info.lower() == "torchic":
            print("\nTORCHIC is a FIRE type chick pokémon that sticks with its trainer, following behind with unsteady steps. This pokémon breathes fire of over 1,800 degrees F, including fireballs that leave the foe scorched black.")
            starter_info = input("> Would you like to CHOOSE Torchic or see info on TREECKO or MUDKIP: ")
            if starter_info.lower() == "choose":
                starter_pokemon = "Torchic"
                return starter_pokemon
        if starter_info.lower() == "treecko":
            print("\nTREECKO is a GRASS type wood gecko pokémon that has small hooks on the bottom of its feet that enable it to scale vertical walls. This Pokémon attacks by slamming foes with its thick tail.")
            starter_info = input("> Would you like to CHOOSE Treecko or see info on TORCHIC or MUDKIP: ")
            if starter_info.lower() == "choose":
                starter_pokemon = "Treecko"
                return starter_pokemon
        if starter_info.lower() == "mudkip":
            print("\nMUDKIP is a WATER type fish pokémon. The fin on Mudkip's head acts as highly sensitive radar. Using this fin to sense movements of water and air, this Pokémon can determine what is taking place around it without using its eyes.")
            starter_info = input("> Would you like to CHOOSE Mudkip or see info on TORCHIC or TREECKO? ")
            if starter_info.lower() == "choose":
                starter_pokemon = "Mudkip"
                return starter_pokemon
        else:
            starter_info = input("\n> Please type one of the CAPITALIZED options: ")

starter_pokemon = starter_pokemon_choice(starter_info)
starter_pokemon = starter_pokemon.lower()
# Assign a variable to the function so you can retrieve your returned value
print (f"\nCongratulations on your new {starter_pokemon.upper()}! It has 50 HP.")



#BATTLE SEQUENCE
import random
print("\nLet's battle a Pokémon!")
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

random_hp = random.randint(50,75)
poochyena = pokemon_info("POOCHYENA", random_hp, "TACKLE", 15, "SCRATCH", 20, "GROWL", "lower attack")
zigzagoon = pokemon_info("ZIGZAGOON", random_hp, "SCRATCH", 20, "HEADBUTT", 25, "TAIL WHIP", "lower defence")
wurmple = pokemon_info("WURMPLE", random_hp, "TACKLE", 15, "POISON STING", 20, "HOWL", "increase attack")
wingull = pokemon_info("WINGULL", random_hp, "WATER GUN", 15, "PECK", 25, "SCREECH", "lower defence")
lotad = pokemon_info("LOTAD", random_hp, "ASTONISH", 15, "ABSORB", 20, "GROWL", "lower attack")
wild_pokemon_list = (poochyena, zigzagoon, wurmple, wingull, lotad)

if starter_pokemon == "torchic":
   starter_pokemon = pokemon_info("TORCHIC",50, "SCRATCH",20, "EMBER", 30, "GROWL", "lower attack")
if starter_pokemon == "mudkip":
   starter_pokemon = pokemon_info("MUDKIP",50, "TACKLE",20, "WATER GUN", 30, "TAIL WHIP", "lower defence")
if starter_pokemon == "treecko":
   starter_pokemon = pokemon_info("TREECKO",50, "ABSORB",20, "POUND", 30, "HOWL", "increase attack")


def battle():
    starter_health = starter_pokemon.hp
    wild_pokemon = random.choice(wild_pokemon_list)
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
                attacker.attack_modifier += 5  # Increase attacker's attack modifier by 5 (same as defender having low def)
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


battle()

import sys
print (f"\nWould you like to heal up and try another BATTLE or GIVE UP?")
choice = input("> Please select one of the capitalized options: ")
if choice.lower() == "battle":
    print("\nLet's battle a Pokémon!")
    battle()
elif choice.lower() == "give up":
    print("\nThank you for playing Pokémon Emerald: SHIFA'S VERSION")
    sys.exit()


#BATTLE SEQUENCE LOG:
# day 1: understand classes, create a class, assign attributes, create torchic attacking with health decreasing
# day 2: fix loop, add different moves for both, randomize poochyena attacks, add random hp, add when wrong input made
# day 3: make EVERYTHING generalized so only one if statement works for all moves inputted instead of a statement
       # for every single move, add starter pokemons, add other wild pokemons
# day 4: randomize wild pokemon appearing, add defence/attack boost move (THERE ARE TOO MANY ERRORS WITH THIS)
# day 5: fix and generalize defence/attack (the error was that it was uppercase... omg), add potions, add starter dying
# day 6: fix starter health updating error, fix restoration health to be accurate, allow a limit for how many effect
       # moves can be used (same for potions), add choice to battle again, retest everything with intro