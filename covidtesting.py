# covid testing
# CSMC 254
# Amra Ibrahim

# Related problem:
# Let's say you want to find the projected 

#Write out the known values for tests, death rate, and positive tests
total_tests_us = 60000000           

# Step 1: Take input from the user (number of tests)
total_tests = int(input("Enter the number of people tested for Covid: "))

# Step 2: Define the positivity rate and death rate
positivity_rate = 0.12  # 12%
death_rate = 0.034     # 3.4%

# Step 3: Calculate the expected number of positive cases and projected deaths
positive_cases = total_tests * positivity_rate
projected_deaths = int(positive_cases * death_rate)  # Round down to an integer

# Step 4: Display the projected number of Covid deaths
print(f"Projected number of Covid deaths based on {total_tests} tests: {projected_deaths}")
