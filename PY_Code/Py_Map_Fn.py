# Map Function
"""
The map() function executes a specified function each item in a iterable.
The item is sent to the function as a parameter.

Syntax:
map(function, iterables)
"""
# Example - 1 (Square root)
myList = [1, 2, 3, 4, 5]
result = map(lambda x: x * x, myList)
print(list(result))
print("------------------------------------s")
# Example - 2 (Add List with Tuple)
list_01 = [1, 3, 5, 7, 9]
tuple_01 = (2, 4, 6, 8, 10)
add = map(lambda l, t: l + t, list_01, tuple_01)
print(set(add))
