#9/30/2024
#CaLara Boney
#P5LAB
#Money Calculator/Self Checkout Coding

import random

#Define disperse_change function
def disperse_change(change):


    #Converting value to an integer
    change = round(change * 100)

    print(f"Change Amount: {change}")

    #Determine how many coins are needed
    num_dollars = change // 100
    change = change - (num_dollars * 100)

    num_quarters = change // 25
    change = change - (num_quarters * 25)

    num_dimes = change // 10
    change = change - (num_dimes * 10)

    num_nickels = change // 5
    change = change - (num_nickels * 5)

    num_pennies = change

    #Formatting how values will print
    if num_dollars > 0:
        if num_dollars == 1:
            print(f"{num_dollars} Dollar")
        else:
            print(f"{num_dollars} Dollars")

    if num_quarters > 0:
        if num_quarters == 1:
            print(f"{num_quarters} Quarter")
        else:
            print(f"{num_quarters} Quarters")

    if num_dimes > 0:
        if num_dimes == 1:
            print(f"{num_dimes} Dime")
        else:
            print(f"{num_dimes} Dimes")

    if num_nickels > 0:
        if num_nickels == 1:
            print(f"{num_nickels} Nickel")
        else:
            print(f"{num_nickels} Nickels")

    if num_pennies > 0:
        if num_pennies == 1:
            print(f"{num_pennies} Penny")
        else:
            print(f"{num_pennies} Pennies")

# Create the main function
def main():
    # Generate random float
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"Total for purchase is ${total_owed:.2f}")

    # Prompt user to give amount paid
    amount_paid = float(input("Enter amount to pay: "))

    # Calculate change owed
    change_owed = amount_paid - total_owed
    print(f"Change owed to customer: ${change_owed:.2f}")


# Call the main function to run the program
if __name__ == "__main__":
    main()





    
