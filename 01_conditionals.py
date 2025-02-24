from inspect import stack

stock1 = "vanilla"
stock2 = "chocolate"
stock3 = "tin roof"
stock4 = "cookie dough"

# Output
# Please tell me your fav 🍦?: Vanilla
# Yes, we have vanilla in stock

# Case 2
# Please tell me your fav 🍦?: Salted caramel
# Yes, we have vanilla in stock

# Case 3
# Clue: in (Refactoring)
# Code Quality improves, functionality remains the same

# Task 1.1
stock1 = "vanilla"
stock2 = "chocolate"
stock3 = "tin roof"
stock4 = "cookie dough"

# Get user input
favorite = input("Please tell me your fav 🍦?: ").lower().strip()

# Check availability
if favorite == stock1.lower():
    print(f"Yes, we have {stock1} in stock")
elif favorite == stock2.lower():
    print(f"Yes, we have {stock2} in stock")
elif favorite == stock3.lower():
    print(f"Yes, we have {stock3} in stock")
elif favorite == stock4.lower():
    print(f"Yes, we have {stock4} in stock")
else:
    print("Sorry, we don't have that flavor 😢")


# Task 1.2

stock1 = "vanilla"
stock2 = "chocolate"
stock3 = "tin roof"
stock4 = "cookie dough"

if favorite == stock1 or favorite == stock2 or favorite == stock3 or favorite == stock4:
    print("We have the flavour in stock")
else:
    print("We don't have the flavour in stock")


# Case 3

# List of available flavors
stock = ["vanilla", "chocolate", "tin roof", "cookie dough"]


def check_stock(favorite):  # Convert input to lowercase for case-insensitive comparison
    favorite = favorite.lower().strip()

    if favorite in (stock1, stock2, stock3, stock4):
        print(f"Yes, we have {favorite} in stock 🍦")
    else:
        print("Sorry, we don't have that flavor 😢")
        print(f"But we do have {stock[1]} in stock 🍦")  # Suggest default flavor


# Get user input
favorite = input("Please tell me your fav 🍦?: ")
check_stock(favorite)


# Control Flow
#
