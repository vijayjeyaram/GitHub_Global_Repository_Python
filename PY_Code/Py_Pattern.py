# Print Square Pattern
patternCount = int(input("Enter the Pattern Count:"))

# Square Pattern
for i in range(patternCount):
    for j in range(patternCount):
        print("#", end="")
    print()

print("------------------------------------")

# Right Angle Triangle
for k in range(patternCount):
    for l in range(k + 1):
        print("#", end="")
    print()

print("------------------------------------")

# Right Angle Triangle - Inverse
for k in range(patternCount):
    for l in range(patternCount - k):
        print("#", end="")
    print()
print("------------------------------------")
for u in range(patternCount):
    for v in range(u):
        if patternCount > v:
            print(end="")
        else:
            print("#")
print()
