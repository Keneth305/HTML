# num1 = 12
# num2 = 2 #"two"

# print(f"the answer is {num1 + num3}")

try:
    
    myList = ["A","B", "C"]
    print(myList[4])
except IndexError:
    print("There is no value associated with the index provided")

try:
    # num1 = 12
    # num2 = 2    #"two"

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    answer = num1 / num2
    
except TypeError:
    print("Enter the correct data type")

except ZeroDivisionError:
     print("You can't divide by zero ")

except ValueError:
    print("Integer values only ")

else:
    print(f"the answer is {answer}")


finally:
    print("End of application")
