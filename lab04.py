# Prompt the user for scoring inputs for the Apples
apples_three_pointers = int(input("Enter the number of successful three-point shots for the Apples: "))
apples_two_pointers = int(input("Enter the number of successful two-point shots for the Apples: "))
apples_free_throws = int(input("Enter the number of successful one-point free throws for the Apples: "))

# Prompt the user for scoring inputs for the Bananas
bananas_three_pointers = int(input("Enter the number of successful three-point shots for the Bananas: "))
bananas_two_pointers = int(input("Enter the number of successful two-point shots for the Bananas: "))
bananas_free_throws = int(input("Enter the number of successful one-point free throws for the Bananas: "))

# Calculate the total scores for Apples and Bananas
apples_score = (apples_three_pointers * 3) + (apples_two_pointers * 2) + apples_free_throws
bananas_score = (bananas_three_pointers * 3) + (bananas_two_pointers * 2) + bananas_free_throws

# Determine the winning team or if it's a tie
if apples_score > bananas_score:
    print("Apples")
elif bananas_score > apples_score:
    print("Bananas")
else:
    print("Tie")
