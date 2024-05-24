import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: python right_triangle.py <positive_integer>")
    sys.exit(1)

try:
    numRows = int(sys.argv[1])

    if numRows < 0:
        print("Invalid input value. The number of rows cannot be negative.")
    else:
        total_asterisks = 0

        for i in range(1, numRows + 1):
            row = "*" * i
            total_asterisks += i
            print(row)

        print()  # Blank line
        print(total_asterisks)

except ValueError:
    print("Invalid input. Please provide a positive integer.")
