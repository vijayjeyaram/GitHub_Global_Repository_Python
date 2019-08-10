chocolateCount = int(input("How many chocolates do you want?:"))
availableChocolateCount = 100
dispenseChocolateCount = 1

if chocolateCount <= availableChocolateCount:
    while dispenseChocolateCount <= chocolateCount:
        print("Collect the Chocolate :)")
        dispenseChocolateCount = dispenseChocolateCount + 1
        availableChocolateCount = availableChocolateCount - 1
else:
    print("There is NO sufficient Chocolates :(")

print("Available Chocolate Count after Dispatch:", availableChocolateCount)




