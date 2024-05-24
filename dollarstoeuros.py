# dollars to euros
# CSMC 254
# Amra Ibrahim

# Constants for the exchange rate and fee percentage.
exchange_rate = 0.85
fee_percentage = 0.02

# Get the dollar amount from the user.
dollars = float(input("Enter the dollar amount: "))

# Calculate the amount after deducting the fee.
dollars_after_fee = dollars * (1 - fee_percentage)

# Convert the remaining dollars to Euros.
euros = dollars_after_fee * exchange_rate

# Display the result to the user.
print(f"You will receive {euros:.2f}")
