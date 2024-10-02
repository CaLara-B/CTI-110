def create_character():
    print("Please provide the following character attributes:")
    
    name = input("Character's name: ")
    age = input("Character's age: ")
    strength = int(input("Character's strength: "))  # Changed to strength

    character = {
        "name": name,
        "age": age,
        "strength": strength,  # Changed from power to strength
    }
    
    return character

def display_characters(char_list):
    for char in char_list:
        print(f"Name: {char['name']}, Age: {char['age']}, Strength: {char['strength']}")

def simulate_fight(attacker, victim):
    # Damage is based solely on the attacker's strength
    damage = attacker["strength"]

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

    # Call function to attack
    updated_character1, updated_character2 = simulate_fight(character_1, character_2)

    print("After the fight:")
    print("Attacker:", updated_character1)
    print("Victim after fight:", updated_character2)

# Call the main function to run the program
if __name__ == "__main__":
    main()
