fav_movie = "John Wick"

# Only `J`

# Index
print(fav_movie[0])  # J
print(fav_movie[5])  # W


# Negative Index
print(fav_movie[-1])  # k
print(fav_movie[-2])  # c


# How to get only `Wick`
print(fav_movie[-4:])
# OR
print(fav_movie[-4] + fav_movie[-3] + fav_movie[-2] + fav_movie[-1])
# OR
print(fav_movie[5] + fav_movie[6] + fav_movie[7] + fav_movie[8])


# Slice operator `:`
# fav_movie[start:end] - end index not included (`2:6` so 6 wont show)
print(fav_movie[2:6])  # hn W
print(fav_movie[2:8])  # hn Wic
print(fav_movie[2:9])  # hn Wick

print(fav_movie[2:])  # hn Wick
print(fav_movie[:])  # John Wick

# Step +1
print(fav_movie[5:9:1])  # the 1 basically means take 1 step or jump from 5 to 9
print(fav_movie[2:9:2])  # h ik

# Reverse string
print(fav_movie[::-1])  # kciW nhoJ
print(fav_movie[-4::-1])  # W nhoJ
print(
    fav_movie[-4:-2:-1]
)  # blank (there is no possible way to go to -2 by going backwards with -1)


# Immutable - cannot modify
fav_hero = "The Hulk"

# fav_hero[0] = 't' ❌
# Output
# The hulk

print(fav_hero[0:4] + "h" + fav_hero[5:9])  # The hulk
print(fav_hero[:4] + "h" + fav_hero[5:])  # The hulk
print(fav_hero[:4] + "h" + fav_hero[-3:])  # The hulk

# Repeat operator (*)
print("💓" * 20)

# Case modifying methods
catchphrase = "i am Groot"


print(catchphrase.upper())  # I AM GROOT
print(catchphrase.lower())  # i am groot
print(catchphrase.capitalize())  # I am groot
print(catchphrase.title())  # I Am Groot
print(catchphrase.swapcase())  # I AM gROOT

print(catchphrase)  # String methods does not modify original value (Immutable)

# Strip - remove only leading & trailing characters
message = "   With great power comes great responsibility   "
clean_message = message.strip()
print(message)
print(clean_message)

# message.lstrip()
# message.rstrip()


coded_message = "********SO*S******"
decoded = coded_message.strip("*")
print(decoded)  # SO*S

# How many times Dream is repeated?
quote = "Dream is not something that you see in sleep, Dream is something that does not let you sleep"
print(quote.count("Dream"))

# Dream -> 🛌💭
print(quote.replace("Dream", "🛌💭"))
print(quote.replace("Dream", "🛌💭", 1))

# Find -> helps find index
print(quote.find("something"))  # 13 (always first occurence)
print(quote.find("**"))
