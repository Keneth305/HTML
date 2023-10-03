# Define the addition() function
def addition():
    # Prompt the user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Calculate the sum
    answer = num1 + num2

    # Print the result
    print(f"The sum of {num1} and {num2} is {answer}")

# Call (invoke) the addition() function
addition()





# Subroutine for addition
def addition():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}")

# Subroutine for subtraction
def subtraction():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 - num2
    print(f"The result of {num1} minus {num2} is {result}")

# Subroutine for multiplication
def multiplication():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 * num2
    print(f"The product of {num1} and {num2} is {result}")

# Subroutine for division
def division():
    num1 = float(input("Enter the dividend: "))
    num2 = float(input("Enter the divisor: "))
    if num2 == 0:
        print("Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is {result}")

# Get user's choice of operation
operation = input("Choose an operation (addition, subtraction, multiplication, division): ")

# Perform the selected operation
if operation == "addition":
    addition()
elif operation == "subtraction":
    subtraction()
elif operation == "multiplication":
    multiplication()
elif operation == "division":
    division()
else:
    print("Invalid operation choice.")






def username():
    first_name = "Firstname"
    last_name = "Lastname"
    interests = "Interests"
    print(f"Your first name is: {first_name}\nYour last name is: {last_name}\nYour interests are: {interests}")

# Call the username() function to display the information
username()

def username(first_name, last_name, interests):
    print(f"Your first name is: {first_name}\nYour last name is: {last_name}\nYour interests are: {interests}")

# Call the username() function with specific values
username("John", "Doe", "Programming, Music")

# You can call the function with different values as needed
username("Alice", "Smith", "Art, Reading")


def username():
    first_name = "Firstname"
    last_name = "Lastname"
    interests = "Interests"
    print(f"Your first name is: {first_name}\nYour last name is: {last_name}\nYour interests are: {interests}")

# Call the username() function to display the information
username()
