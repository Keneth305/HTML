# import the datetime library/class/module
import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()

# Print the current date and time
print(current_datetime)


print("Not using while Loop output")
dateTime = datetime.datetime.now()
print(dateTime.strftime("%H:%M:%S"))

# study the output of the code above and the output in the while loop to answer

# What is the while loop doing?

# add comment to explain what you understand the"datetime.datetime.now().strftime("%H:%M:%S")"

# Import the datetime module to work with dates and times
import datetime

# Get the current date and time using the datetime module
current_datetime = datetime.datetime.now()

# Format the current datetime object as a string with the format "HH:MM:SS"
formatted_time = current_datetime.strftime("%H:%M:%S")

# The 'formatted_time' variable now contains the current time in the "HH:MM:SS" format


# add comment to explain what you understand the 'end='

# The end="" parameter is used to specify an empty string "" 
"""
 Python's print() function comes with a parameter called 'end. 
 By default, the value of this parameter is '\n', i.e. the new line character. 
"""

# add comment to explain what you understand the "\r""'

# The escape sequence "\r" represents a carriage return character. 
"""
The '\r' character is used to return the cursor to the beginning 
of the current line without advancing to the next line.
"""

print("while Loop output")
while True:
    print(datetime.datetime.now().strftime("%H:%M:%S"), end="\r")
    # time.sleep(1)
