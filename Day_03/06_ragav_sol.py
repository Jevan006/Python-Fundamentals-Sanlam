# Ragav Solution

# Conditionals (Control flow)
# Take a decision -> Choice


# if...else
# if  no_of_person <=2 -> bike  else   car

no_of_person = 4

# Condition return boolean | if expects a boolean
if no_of_person <= 2:
    print("We will take the bike for the party")
else:
    print("We will take the car for the party")

# Lexical order -> Dictionary way of looking at it

# Task 1.1
# Get two person name and height
# Case 1:
# Ethan, Luvuyo
# 185cm, 175cm
# Ethan is taller than Luvuyo by 10cm


# person1 = input("Please tell me person1 name: ")
# person2 = input("Please tell me person2 name: ")
# height1 = float(input(f"Please tell me the height of {person1}: "))
# height2 = float(input(f"Please tell me the height of {person2}: "))


# if height1 > height2:
#     print(f"{person1} is taller than {person2} by {height1 - height2}cm")
# else:
#     print(f"{person2} is taller than {person1} by {height2 - height1}cm")


# Case 2:
# Ethan, Luvuyo
# 185cm, 194cm
# Luvuyo is taller than Ethan by 9cm


# Task 1.2
# Case 3:
# Ethan, Luvuyo
# 185cm, 185cm
# Ethan and Luvuyo are of the same height
# Clue: elif


# person1 = input("Please tell me person1 name: ")
# person2 = input("Please tell me person2 name: ")
# height1 = float(input(f"Please tell me the height of {person1}: "))
# height2 = float(input(f"Please tell me the height of {person2}: "))


# if height1 > height2:
#     print(f"{person1} is taller than {person2} by {height1 - height2}cm")
# elif height2 > height1:
#     print(f"{person2} is taller than {person1} by {height2 - height1}cm")
# else:
#     print(f"{person1} and {person2} are of the same height")

# only one if & else, multiple elif


# Task 1.3
# Improve code quality
# Clue: abs() -> Always +ve -> |x|


person1 = input("Please tell me person1 name: ")
person2 = input("Please tell me person2 name: ")
height1 = float(input(f"Please tell me the height of {person1}: "))
height2 = float(input(f"Please tell me the height of {person2}: "))
height_difference = abs(height1 - height2)

if height1 > height2:
    print(f"{person1} is taller than {person2} by {height_difference}cm")
elif height2 > height1:
    print(f"{person2} is taller than {person1} by {height_difference}cm")
else:
    print(f"{person1} and {person2} are of the same height")
