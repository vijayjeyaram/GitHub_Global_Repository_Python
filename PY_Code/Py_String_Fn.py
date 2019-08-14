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

# Replace():
test_01 = "Hello World"
print("Replace string:", test_01.replace("World", "Universe"))

#IsDigit():
test_02 = "12345.x"
print("IsDigit string:", test_02.isdigit())

#IsAlpha():
test_03 = "x.1"
print("IsAlpha string:", test_03.isalpha())

#strip(): Using this function we can remove particular char from a string (left/right) side
test_04 = "oooTestooo"
print("remove particular char from a string:", test_04.strip("o"))

#lstrip(): Using this function we can remove particular char from a string (left side)
print("remove particular char from a string:", test_04.lstrip("o"))

#rstrip(): Using this function we can remove particular char from a string (right side)
print("remove particular char from a string:", test_04.rstrip("o"))