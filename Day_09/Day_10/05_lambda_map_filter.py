def greet(name):
    return f"Hi, {name}"


# Lambda expression/ Lambda function:function one liner

greet1 = lambda name: f"Hi, {name}"

print(greet("Jevan"))
print(greet1("Jevan"))


# 1. Anonymous - nameless fuctions
# 2. One liner
# 3. Implicitly return (automatically)


def add(n1, n2):
    return n1 + n2


add1 = lambda n1, n2: n1 + n2
print(add(9, 8))


# map & filter

player_stats = [10, 30, 60]

boosted_stats = map(lambda x: x * 2, player_stats)

print(boosted_stats, list(boosted_stats))

# map -> fn -> Takes another fn as arg
# map -> Higher order functions

boosted_stats = map(lambda x: x * 2, [10, 30, 60])

# When to go for map
# 1. len(Input_list) == len(Output_list)
# 2. Transform data type
# 3. Doesn't affect the Input list

# When to go for filter
# 1. len(Input_list) >= len(Output_list)
# 2. Input data_type == Output data_type
# 3. Doesn't affect the Input list
