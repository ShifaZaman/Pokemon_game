# ENTRY POINT to the game

from intro_choosing_starter import starter_pokemon_choice  # From /file name/, import /function/ as it's called here
from battle import battle

def main():
    print("\nLet's play POKéMON! There are 3 starting pokémon for you to choose from: TORCHIC, TREECKO and MUDKIP.")
    starter_info = input("> Please type which pokémon you would like more info on: ")

    starter_pokemon = starter_pokemon_choice(starter_info)
    starter_pokemon = starter_pokemon.lower()
    # Assign a variable to the function so you can retrieve your returned value

    print (f"\nCongratulations on your new {starter_pokemon.upper()}! It has 50 HP.")

    while True: # Main game loop that continues to play the battle sequence if player chooses to later
        print("\nLet's battle a Pokémon!")
        battle(starter_pokemon)

        while True:
            import sys
            print (f"\nWould you like to heal up and try another BATTLE or GIVE UP?")
            choice = input("> Please select one of the capitalized options: ")
            if choice.lower() == "battle":
                break # This breaks this inner while loop and goes back to the main game loop and a battle restarts
            elif choice.lower() == "give up":
                print("\nThank you for playing Pokémon Emerald: SHIFA'S VERSION")
                sys.exit() # Force ends the code
            else:
                print("\n* Please select one of the capitalized options: *")

if __name__ == "__main__":
    main()

# Every module (or script) has a built-in variable called __name__. When a script is run directly, Python sets the
# __name__ variable to "__main__".  If the script is imported as a module into another script, __name__ is set to the
# name of the script (module) without the .py extension.
# The if __name__ == "__main__":  line checks if the script is being run directly and not imported as a module