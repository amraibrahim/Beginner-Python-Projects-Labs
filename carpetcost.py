# carpet cost
# CSMC 254
# Amra Ibrahim


# State carpet cost and installation cost per square foot.
carpet_cost_per_sqft = 9.81
installation_cost_per_sqft = 1.50

# Get the length and width of the room from the user.
length = float(input("Enter the length of the room in feet: "))
width = float(input("Enter the width of the room in feet: "))

# Calculate the area of the room.
area = length * width

# Calculate the cost of the carpet.
carpet_cost = area * carpet_cost_per_sqft

# Calculate the installation cost.
installation_cost = area * installation_cost_per_sqft

# Calculate the total cost.
total_cost = carpet_cost + installation_cost

# Display the total cost to the user.
print(f"The total cost of carpeting the room is ${total_cost}")
