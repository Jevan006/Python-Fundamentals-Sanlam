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
