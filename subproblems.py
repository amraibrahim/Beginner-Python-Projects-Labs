# Function to greet a person by name
def greetings(name):
    # Check if the name is "Alice" or "Bob"
    if name == "Alice" or name == "Bob":
        # Return a personalized greeting
        return f"Hello, {name}!"
    else:
        # Return a generic greeting for strangers
        return "Hello, Stranger!"

# Testing the greetings function
print(greetings("Alice"))  # Output: "Hello, Alice!"
print(greetings("Bob"))    # Output: "Hello, Bob!"
print(greetings("Charlie"))# Output: "Hello, Stranger!"
