# Exception Handling

# List Without Exception
myList = [1, 2, 3, 4, 5]
print(myList)
print(myList[2])

# List With Exception
try:
    print(myList[7])
except Exception as e:
    print("Entered Value crossed the Boundary.", e)



