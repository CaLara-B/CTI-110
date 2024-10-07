#CaLara Boney
#10/07/2024
#P5HW
#Coding A Game!

import random

def create_character():
    print("Please provide the following character attributes.")
    
    name = input("Character's name: ")
    age = input("Character's age: ")
    power = input("Character's power: ")
    strength = int(input("Character's strength: "))

    character = {
        "name": name,
        "age": age,
        "power": power,
        "strength": strength,
    }
    
    return character

def display_characters(char_list):
    for char in char_list:
        print(f"Name: {char['name']}, Age: {char['age']}, Power: {char['power']}, Strength: {char['strength']}")

def simulate_fight(attacker, victim):
    # Damage is based solely on the attacker's strength
    damage = random.randint(0, attacker["strength"])
    
    # Print the attack action
    print(f"{attacker['name']} attacks {victim['name']} for {damage} damage!")
    
    # Reduce the victim's strength
    victim["strength"] = max(0, victim["strength"] - damage)
    
    return attacker, victim

def main():
    # Create a list
    char_list = []

    # Create Two Characters
    character_1 = create_character()
    character_2 = create_character()

    # Add Characters to List
    char_list.append(character_1)
    char_list.append(character_2)

    # Display all characters
    display_characters(char_list)

    # Randomly choose attacker and victim
    attacker, victim = random.sample(char_list, 2)

    # Call function to attack
    print()
    print("Let the fight begin! \n")
    attacker, victim = simulate_fight(attacker, victim)

    # Display results after the fight
    print("\nAfter the fight:")
    display_characters(char_list)

# Call the main function to run the program
if __name__ == "__main__":
    main()
