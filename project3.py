import sys

# Step 1: Read the program argument as input and store it in a variable.
if len(sys.argv) != 2:
    print("Usage: python project3.py <number_of_rows>")
    sys.exit(1)

try:
    num_rows = int(sys.argv[1])
except ValueError:
    print("Invalid input. Please provide a valid integer for the number of rows.")
    sys.exit(1)

# Step 2 and 3: Input validation
if num_rows < 1:
    print("Invalid input value. The number of rows cannot be less than 1.")
    sys.exit(1)
elif num_rows > 20:
    print("Invalid input value. The number of rows cannot be more than 20.")
    sys.exit(1)

# Step 4: Calculate the number of asterisk characters to be printed for each row.
total_asterisks = 0

# Step 5: Use loops to print the top half of the diamond.
for i in range(1, num_rows + 1, 2):
    spaces = (num_rows - i) // 2
    asterisks = i
    total_asterisks += asterisks
    print(" " * spaces + "* " * asterisks)

# Step 6: Use loops to print the bottom half of the diamond.
for i in range(num_rows - 2, 0, -2):
    spaces = (num_rows - i) // 2
    asterisks = i
    total_asterisks += asterisks
    print(" " * spaces + "* " * asterisks)

# Step 7: If the number of rows is even, repeat the widest row to maintain symmetry.
if num_rows % 2 == 0:
    widest_row = num_rows + 1  # Adjust for even rows
    total_asterisks += widest_row
    print(" " * ((num_rows - widest_row) // 2) + "* " * widest_row)

# Step 8: Display the total number of asterisk characters printed.
print(f"Total asterisk characters printed: {total_asterisks}")
