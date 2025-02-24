# Task 1: Convert Fahrenheit to Celsius
fahrenheit = float(input("Please provide your Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9  # formula
print(f"The {fahrenheit}°F is {round(celsius)}°C")


# Task 2: Calculate Age from Birth Year
birth_year = int(input("Please provide your birth year: "))
current_year = 2025  # Assuming the current year is 2025
age = current_year - birth_year
print(f"Your age is {age}")

# Task 3: Calculate Area of a Circle (Assume PI = 3.14)

SPEED_OF_LIGHT = 3 * 10**8  # CONSTANT_CASE -> Indication to other developers

pi = 3.14
radius = float(input("Provide the radius of the circle: "))
area = pi * (radius**2)
print(f"Area of the circle is {area:.4f}")

# Task 4
# Task: Build a loader
# Input: 70
# Output: [======= ] 70%

# Input: 23
# Output: [==      ] 23%

# Task 4: Build a Loader


def display_loader(percentage):
    total_blocks = 10  # Total length of the loader
    filled_blocks = round((percentage / 100) * total_blocks)  # Calculate filled portion
    empty_blocks = total_blocks - filled_blocks  # Remaining empty space

    loader = "[" + "=" * filled_blocks + " " * empty_blocks + f"] {percentage}%"
    print(loader)


# Get user input
percentage = int(input("Input: "))
display_loader(percentage)


# OR

load = input("Please enter your number: ")
loader = int(load) // 10
output = loader * "="
blank = (10 - loader) * " "
print(f"[{output}{blank}] {load}%")

# 20 * "=" 20 times repeat "="

percentage = int(input("Input: "))
loader = percentage // 10
loader_symbols = loader * "="
space_symbols = (10 - loader) * " "
print(f"Output: [{loader_symbols}{space_symbols}] {percentage}%")
