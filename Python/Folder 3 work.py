"""Exercise: Complete the code block below to print a list of converted numbers to letter as specified in the range, the 
questions marks indicates where the code is missing"""
# def alphabets(): # created the function alphabets
#     alphabetList = ? # create an empty list
#     for ? in range(65, 123):
#         alphabetList.append(chr(letters))  # converts numbers to letters
#     return ?


def alphabets():
    alphabetList = []  # create an empty list
    for letters in range(65, 123):
        alphabetList.append(chr(letters))  # converts numbers to letters
    return alphabetList

# Call the function to get the list of alphabets
result = alphabets()

# Print the list of alphabets
print(result)



# Exercise: sort and print the items in the commons variable in ascending and descending order

# Sample list
commons = [5, 2, 8, 1, 6, 4, 3]

# Sort the list in ascending order using the sort() method (in-place)
commons.sort()

# Print the sorted list in ascending order
print("Ascending Order:", commons)

# Sort the list in descending order using the sorted() function
descending_order = sorted(commons, reverse=True)

# Print the sorted list in descending order
print("Descending Order:", descending_order)


# Exercise:  create two lists with at least two/three common names in both lists


list1 = ["Alice", "Bob", "Charlie", "David", "Eve"]
list2 = ["Charlie", "David", "Frank", "Grace", "Alice"]

common_names = [name for name in list1 if name in list2]

print("Common Names:", common_names)


# Use the input and then the if to search the common names list for a specific name
# Two lists with common names
list1 = ["Alice", "Bob", "Charlie", "David", "Eve"]
list2 = ["Charlie", "David", "Frank", "Grace", "Alice"]

# Find and create a commonNames list with common names
commonNames = [name for name in list1 if name in list2]

# Get a name from the user
user_input = input("Enter a name to search in common names list: ")

# Check if the user's input name is in the commonNames list
if user_input in commonNames:
    print(f"{user_input} is a common name.")
else:
    print(f"{user_input} is not a common name.")
