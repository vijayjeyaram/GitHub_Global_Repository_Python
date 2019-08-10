# Break Statement:

chocolateCount = int(input("How many chocolates do you want?:"))
availableChocolateCount = 5
dispenseChocolateCount = 1

while dispenseChocolateCount <= chocolateCount:
    if dispenseChocolateCount > availableChocolateCount:
        print("There is NO sufficient Chocolates :(")
        break

    print("Collect the Chocolate :)")
    dispenseChocolateCount = dispenseChocolateCount + 1

print("################################")

# Continue Statement:
# It will Skip the further stmt.

# Don't print the value which are divisible by 5
for i in range(1, 101):
    if i % 5 == 0:
        continue
    print(i)

print("################################")

# Pass Statement:
# Instead of empty block we can use Pass.

# Print only ODD numbers
for i in range(1, 101):
    if i % 2 == 0:
        pass
    else:
        print(i)


