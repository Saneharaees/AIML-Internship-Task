# This script demonstrates how to create and call user defined functions
# Exercise on User defined functions in Python

# Function to greet a user
def greet_user(name):
    return "Hello, " + name + "!"

# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Calling the functions
message = greet_user("Student")
result = add_numbers(10, 20)

print(message)
print("The addition result is:", result)
