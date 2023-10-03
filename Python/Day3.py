highscores = [125, 63, 35, 12]
usersList = ["Anna", "Paul", "Joe", "Jane", "Anne", "Pauline", "Joan", "Janet"]

# Pair each user with their high score using zip
user_scores = list(zip(usersList, highscores))

# Sort the list of user-score pairs based on the scores (in descending order)
user_scores.sort(key=lambda x: x[1], reverse=True)

# Extract the sorted users' names
sorted_users = [user for user, score in user_scores]

# Display the sorted users
print("Sorted Users by High Score:")
for user in sorted_users:
    print(user)



print("Welcome to the table quiz.\n")
num = int(input("Enter a number: "))

for i in range(1, 11):  # Loop from 1 to 10 for multiplication table
    answer = int(input(f"What is {i} x {num}? "))
    correct = i * num
    print(f"The answer is {answer}")

    if answer == correct:
        print("Correct")
    else:
        print(f"Wrong. The correct answer is {correct}")

    print("Finished")





    num1 = int(input("Enter number for multiplication: "))

# Display the multiplication table for num1
for i in range(1, 11):  # Multiplication table from 1 to 10
    result = i * num1
    print(f"{i} x {num1} = {result}")







"""use a while loop when the number of iteration is unknown(dont know how many times you want/going 
to do something for)
A while loop also controls the flow of execution in a program"""


"""Comparison operator compare values
==    equal  ( 2 == 2)
< 	less than
> 	more than
<= 	less than or equal to 
>= 	greater than or equal to
!=    Not equal to"""

# While loop keeps looping/iterating until a condition is met
num = 1  # int(input("Enter number below 20: "))

while num <= 20:
    print(f"The number is {num}")
    num += 1  # what is this doing ? increments num by 1 every loop

"Exercise: Modify the code above to countdown from 20"

# "solution"
print("\ncountdown from 20")
num = 20
while num >= 0:
    print(f"The number is {num}")
    num -= 1  # what is this doing ? decrements num by 1 every loop




import datetime

while True:
    print("Current time:")
    dateTime = datetime.datetime.now()
    print(dateTime.strftime("%H:%M:%S"))

    # Add a delay of 1 second (optional)
    import time
    time.sleep(1)




# study the output of the code above and the output in the while loop to answer

# What is the while loop doing?
#-- Creating an indefinite loop that continuously displays the current time and updates it at regular intervals.

# add comment to explain what you understand the"datetime.datetime.now().strftime("%H:%M:%S")"

import datetime

print("Not using while Loop output")

# Get the current date and time using datetime.datetime.now()
# Format the current time as a string in "hour:minute:second" format using strftime()
formatted_time = datetime.datetime.now().strftime("%H:%M:%S")

# Print the formatted time
print(formatted_time)


# add comment to explain what you understand the 'end='
"""
 Python's print() function comes with a parameter called 'end. 
 By default, the value of this parameter is '\n', i.e. the new line character. 
"""

# add comment to explain what you understand the "\r""'
"""
The '\r' character is used to return the cursor to the beginning 
of the current line without advancing to the next line.
"""

print("while Loop output")
while True:
    print(datetime.datetime.now().strftime("%H:%M:%S"), end="\r")
    # time.sleep(1)