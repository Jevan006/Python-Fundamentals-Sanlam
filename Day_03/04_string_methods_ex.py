secret_message = "Programming in Python is not only powerful but also fun!"

# Task 1
# Expected Output
# `PYTHON-POWERFUL`

# 1. Solve
# 2. Make it better

secret_message = "Programming in Python is not only powerful but also fun!"

# Extract "Python" using slicing
word1 = secret_message[16:22].upper()  # "PYTHON"

# Extract "powerful" using slicing
word2 = secret_message[31:39].upper()  # "POWERFUL"

# Combine with hyphen
result = word1 + "-" + word2

print(result)  # Output: PYTHON-POWERFUL


# Task 1.2
flipped_message = "!nuf sseldnE dna seitinutroppo lufrewop htiw nohtyP"

# Expected Output
# "python 🗡️ powerful 🌸"

flipped_message = "!nuf sseldnE dna seitinutroppo lufrewop htiw nohtyP"
original = flipped_message[::-1]
result_message = original[0:6] + "🗡️ " + original[12:20] + "🌸"

print(result_message.lower())

# Task 1.3

# After the 🔑
message = "    🚨🔍📱🔑secret_code✌️"

# Output
# SECRET_CODE✌️

message = "    🚨🔍📱🔑secret_code✌️"

print(message[message.find("🔑") + 1 :].upper())

# OR

key_index = message.find("🔑")
decoded_msg = message[key_index + 1 :].upper()
print(decoded_msg)


# Dot Chaining
clean_upper_msg = secret_message.strip().upper()

# x.upper()
