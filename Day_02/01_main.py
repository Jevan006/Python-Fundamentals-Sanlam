# variable_name =value
import py_compile

name = "Jevan, says 👋🌍!!!!"
age = 23
balance = 1000000.50
is_rich = True

print(name)
print(age)
print(balance)

# Dynamically typed -> Python smart

print(type(name))  # <class 'str'>
print(type(age))  # <class 'int'>
print(type(balance))  # <class 'float'>
print(type(is_rich))  # <class 'bool'>

# My name is Jevan


print("My name is " + name)


# My age is 23

print("My age is " + str(age))

# fstring
# {} -> interpolation (substitution)
# {} -> expressions are allowed
# Auto converts
# Readable


print(f"My age is {age}")
print(f"He has {2 * 1000} followers 👌")
