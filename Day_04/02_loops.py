print("Vote for Jevan 🎊")
print("Vote for Jevan 🎊")
print("Vote for Jevan 🎊")

# Refactor while loop

i = 1

while i <= 3:
    print("Vote for Jevan 🎊")
    i = i + 1

    print("Voting Ended🎊")

# Refactor in 'for' loop
# for and range (pair)
# always start from 0 when counting

for i in range(3):
    print(i)

# range(start, end) -> range(start, end)
for i in range(1, 11):
    print(i)

# print odd numbers from 1 -> 50
# Easy way
for i in range(1, 51, 2):
    print(i)

# Hard way
# Hard
for i in range(1, 51):
    if i % 2 != 0:
        print(i)

# Easy
for i in range(1, 51, 2):
    print(i)

# Refactor in 'for' loop
# for and range (pair)
# print 3 times
for i in range(3):  # Loop runs 3 times (0, 1, 2)
    print("Vote for Jevan 🎊")
