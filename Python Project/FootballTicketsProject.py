# Welcome message
print("Welcome to the Football Stadium Ticketing System!")

# Ticket prices
adult_price = 20.00
child_price = 10.00
senior_price = 15.00

# Ask for the number of tickets required
num_adult_tickets = int(input("How many adult tickets are required? "))
num_child_tickets = int(input("How many child tickets are required? "))
num_senior_tickets = int(input("How many senior tickets are required? "))

# Calculate the total charge
total_charge = (num_adult_tickets * adult_price) + (num_child_tickets * child_price) + (num_senior_tickets * senior_price)

# Display the total charge
print("\nTotal Charge:")
print(f"Adult Tickets x{num_adult_tickets}: ${num_adult_tickets * adult_price:.2f}")
print(f"Child Tickets x{num_child_tickets}: ${num_child_tickets * child_price:.2f}")
print(f"Senior Tickets x{num_senior_tickets}: ${num_senior_tickets * senior_price:.2f}")
print(f"Total: ${total_charge:.2f}")

# Thank you message
print("\nThank you for using the Football Stadium Ticketing System. Enjoy the game!")
