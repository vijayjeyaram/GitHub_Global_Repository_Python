
myColor = ["Blue", "Green", "Violet", "Purple", "White", "Yellow"]
print(myColor)
# Iterate List Though Values
for c in myColor:
    print(c)
print("----------")
# Iterate List Though Index
for c in range(len(myColor)):
    print(c, myColor[c])
print("----------")
# Iterate List Though Enumerate Function
for index, color in enumerate(myColor):
    print(index, color)
print("----------")
# Iterate List Though Enumerate Function and mention the index
for index, color in enumerate(myColor, 3):
    print(index, color)
print("----------")