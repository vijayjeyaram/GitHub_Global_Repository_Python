# Lambda Functions
"""
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
"""


# Regular Function
def add(a, b):
    c = a + b
    return c


print(add(5, 5))
print("----------------------------------")
# Lambda Function
result = (lambda x, y: x * y)(5, 6)

print(result)
# print(result(5, 5))
print("----------------------------------")
