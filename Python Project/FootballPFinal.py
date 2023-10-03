import datetime

print("Welcome to the Football Stadium Ticketing System!")

# Ticket prices
adult_price = 20.00
child_price = 10.00
senior_price = 15.00
parking_pass_price = 5.00

# Ask for the number of tickets required
num_adult_tickets = int(input("How many adult tickets are required? "))
num_child_tickets = int(input("How many child tickets are required? "))
num_senior_tickets = int(input("How many senior tickets are required? "))

# Ask for the lead booker surname
lead_booker_surname = input("Please enter the lead booker's surname: ")

# Ask if they require a parking pass
parking_pass_required = input("Do you require a parking pass for the car park? (yes/no): ").strip().lower()

# Calculate the total charge
total_ticket_charge = (num_adult_tickets * adult_price) + (num_child_tickets * child_price) + (num_senior_tickets * senior_price)
total_parking_charge = 0

if parking_pass_required == 'yes':
    total_parking_charge = parking_pass_price

# Calculate the total cost
total_cost = total_ticket_charge + total_parking_charge

# Print a ticket
print("\n********** Ticket **********")
print(f"Lead Booker: {lead_booker_surname}")
print(f"Adult Tickets x{num_adult_tickets}")
print(f"Child Tickets x{num_child_tickets}")
print(f"Senior Tickets x{num_senior_tickets}")
print(f"Total Ticket Cost: ${total_ticket_charge:.2f}")
print(f"Date of Purchase: {datetime.date.today()}")


# Print a parking pass if requested
if parking_pass_required == 'yes':
    print("\n********** Parking Pass **********")
    print(f"Lead Booker: {lead_booker_surname}")
    print(f"Valid for today: {datetime.date.today()}")
    print("****************************\n")

print("Thank you for your purchase. Enjoy the game!")
