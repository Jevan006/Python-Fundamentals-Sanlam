# In python
# Function treated as first class (if value)

# x = 1

# Rules
# 1. Function: Assign to variable
# 2. Function: Pass as an argument
# 3. Function: Return

# 1. Assign to variable
# x = 1


# def greet(name):
#     return f"Hi, {name}"


# print(type(greet))  # <class 'function'>

# y = greet  # function

# print(y("Jamie"))

# 2. Function: pass as argument - say_hello (function) is passsed as argument

# def say_hello():
#     return "Hello, "

# def greeting(hello_msg, name):
#     print(hello_msg() + name)

# greeting(say_hello, "Python!")

# Functional languages -F#, Haskell, Scala

# 3. Function: Returned


def f1():
    def f2():
        print("Hi 👋")

    return f2


f1()()
# Make it print Hi
