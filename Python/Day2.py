# Input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the two numbers to find the minimum
if num1 < num2:
    minimum = num1
else:
    minimum = num2

# Display the minimum value
print(f"The minimum value between {num1} and {num2} is {minimum}.")




cardvalue = "King"
suitOfcards = "Hearts"

chkCardValue = input("Enter card value:").title()
chkCardSuit = input("Enter card suit:").title()

# Add the condition to use the "and" operator to check card value & suit to users inputs
if chkCardValue == cardvalue and chkCardSuit == suitOfcards:
    print("You have the King of Hearts!")
else:
    print("Sorry, it's not the King of Hearts.")



# Modify the condition to use the "or" and "not" operators
if chkCardValue == cardvalue or chkCardSuit != suitOfcards:
    print("Sorry, it's not the King of Hearts.")
else:
    print("You have the King of Hearts!")







# Display the menu to the user
while True:
    print("Subject Menu:")
    print("1. Mathematics")
    print("2. Science")
    print("3. History")
    print("4. Exit")

    # Get the user's choice
    choice = input("Enter your choice (1/2/3/4): ")

    # Check if the user wants to exit
    if choice == "4":
        print("Exiting the program. Goodbye!")
        break  # Exit the loop

    # Convert the user's choice to an integer
    choice = int(choice)

    # Check the user's choice and display the associated value
    if choice == 1:
        print("You selected Mathematics.")
        print("Mathematics explores the properties and relationships of numbers and shapes.")
    elif choice == 2:
        print("You selected Science.")
        print("Science is the study of the natural world and its phenomena.")
    elif choice == 3:
        print("You selected History.")
        print("History is the study of past events, particularly human history.")
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4).")



from random import randint

dice1 = randint(1, 6)
dice2 = 6  # randint(1, 6)


print(f"Dice 1: {dice1} | Dice 2: {dice2}")

dice = dice1 + dice2  # adding the values of both dice

if dice == 12:  # check if the total of both dice is 12
    dice = dice * 2  # double the total from both dice
    print(f"You threw {dice}")
else:
    if dice1 == dice2:
        dice = dice  # 10 = 10
        print(f"You threw {dice}")
# diceThrow = dice
# print(f"You threw a total {diceThrow}")
print(f"You threw a total {dice}")


# a message that you threw a double if both number on the two dice are a match
# multiply the total value of both dice by 2 if the total is 12




import time  # import the time library/class/module

name = "Jane"
print(name)

# invoke/call the time function and pass in seconds as argument
time.sleep(5)
print(f"Printed after 5 seconds: {name}")
