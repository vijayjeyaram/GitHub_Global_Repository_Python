# Filter Function
"""
The filter() function returns an iterator were the items are filtered
through a function to test if the item is accepted or not.

Syntax:
filter(function, iterable)
"""
mySet = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
odd = filter(lambda n: n % 2 != 0, mySet)
print(tuple(odd))
