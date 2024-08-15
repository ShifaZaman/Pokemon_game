#INTRO TO THE GAME: choosing starter pokemon

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
