# String Functions:

# capitalize():	Converts the first character of a sentence  to upper case
proverb_01 = "a bad workman always blames his tools"
print("Converted to Upper Case:", proverb_01.capitalize())

# casefold(): Converts string into lower case
proverb_02 = "PRACTICE MAKES PERFECT"
print("Converted from Upper Case to lower case:", proverb_02.casefold())

# count(): Returns the number of times a specified value occurs in a string
myString_01 = "I love apples, apple are my favorite fruit"
print("Returns the number of times a specified value occurs in a string:", myString_01.count("apple"))

# encode(): Returns an encoded version of the string
proverb_02 = "PRACTICE MAKES PERFECT"
print("Encoded string:", proverb_02.encode())

# Splits(): The string at the specified separator, and returns a list
proverb_02 = "PRACTICE MAKES PERFECT"
print("split string:", proverb_02.split(" "))

