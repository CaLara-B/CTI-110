# CaLara Boney
# 10/2/2024
# P5HW
# Using AI and functions to create a game

# Define a dictionary to create a character
# Make a python function called "create_character" that returns a dictionary
    

def create_character():
    print("Please provide the following character attributes.")
    
    name = input("Character's name: ")
    age = input("Character's age: ")
    power = input("Character's power: ")

    character = {
        "name": name,
        "age": age,
        "power": power,
    }
    
    return character
print()

def display_characters(char_list):
    for char in char_list:
        print(char["name"])

def main():
    character_1 = create_character()
    print(character_1)
    
# Call the main function to run the program
if __name__ == "__main__":

    # Create a list
    char_list = []

    # Create Three Characters

    character_1 = create_character()
    character_2 = create_character()

    # Add Characters to List
    char_list.append(character_1)
    char_list.append(character_2)

    # Diplay all characters
    display_characters(char_list)

def simulate_fight(attacker, victim):
    # Damage is based solely on the attacker's strength
    damage = attacker["strength"]

    # Reduce the victim's strength
    victim["strength"] = max(0, victim["strength"] - damage)

    return attacker, victim

    # Call function to attack
    character_1, character_2 = simulate_fight(character_1, character_2)
