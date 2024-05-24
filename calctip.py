# calculate tip
# CSMC 254
# Amra Ibrahim


# Input: Ask the user to enter the price of the meal
meal_price = float(input("Enter the price of the meal: $"))

# Calculate the tip amount (18% of the meal price)
tip_amount = 0.18 * meal_price

# Calculate the total amount to pay (meal price + tip amount)
total_amount = meal_price + tip_amount

# Display the total amount to pay
print(f"Total amount to pay (including an 18% tip): ${total_amount}")
