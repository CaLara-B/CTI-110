#9/30/24
#CaLara Boney
# Learning stuff


# User-defined functions
import random

# Define the add function
def add(x,y):
    """This function adds two intergers, x and y"""
    result = x + y
    return result

#Define a non-value returning function
def getList():
    """Create and return a list"""
    myList = []
    for item in range(3):
        myList.append(input("Enter a color: "))
    print(myList)
    
def getTotal(priceList):
    """Return the sum of a list of numbers"""
    return sum(priceList)


# Create the main function
def main():
    # Main program goes here
    rand1 = random.randint(1,100)
    rand2 = random.randint(1,100)
    # Call the add function
    num_sum = add(rand1,rand2)
    print(f"The sum of {rand1} and {rand2} is {num_sum}")


    # Call the getList function
    getList()

    # Create a list of floats
    myNums = []
    for item in range(4):
        myNums.append(float(input("Enter a price: ")))
        
    # Call the getTotal function, passing in myNums (List)
    total = getTotal(myNums)

    # Print each number in myNums
    print("The values are: ")
    for num in myNums:
        print(num)

    # Print the total
    print(f"The total is ${total:.2f}")

# Call the main function
if __name__ == "__main__":
    main()
