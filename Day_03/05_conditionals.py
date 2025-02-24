# Conditionals (Control flow)
# Take a decision -> Choice

# if ... else
# if no_of_person <= 2 -> bike else car

no_of_person = 1

if no_of_person <= 2:
    print("We will take the bike for the party")
else:
    print("We will take the car for the party")


# Task 2
# Get two person name and height
# Case 1
# Ethan, Luvuyo
# 185cm, 175cm
# Ethan is taller than Luvuyo by 10cm

# Case 2
# Ethan, Luvuyo
# 185cm, 195cm
# Luvuyo is taller than Ethan by 10cm

# Get two person names and their heights
name1 = input("Insert name1")
height1 = float(input(f"Enter {name1}'s height in cm: "))

name2 = input("Insert name2")
height2 = float(input(f"Enter {name2}'s height in cm: "))

# Compare heights
if height1 > height2:
    print(f"{name1} is taller than {name2} by {height1 - height2}cm.")
elif height2 > height1:
    print(f"{name2} is taller than {name1} by {height2 - height1}cm.")


# Task 1.2
# Case 3:
# Ethan, Luvuyo
# 185cm, 185cm
# Ethan and Luvuyo are of the same height
# Clue: elif

# Get two person names and their heights
name1 = input("Enter the first person's name: ")
height1 = float(input(f"Enter {name1}'s height in cm: "))

name2 = input("Enter the second person's name: ")
height2 = float(input(f"Enter {name2}'s height in cm: "))

# Compare heights
if height1 > height2:
    print(f"{name1} is taller than {name2} by {height1 - height2:.2f}cm.")
elif height2 > height1:
    print(f"{name2} is taller than {name1} by {height2 - height1:.2f}cm.")
else:
    print(f"{name1} and {name2} are of the same height.")


# Lexical order -> Dictionary way of looking at it

# only one if & else, but multiple elif
