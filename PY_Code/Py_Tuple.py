# Tuple
""""
1.Tuple can hold any kind of Data Type.
2.A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round () brackets.
3.List can allows to hold duplicate values.
4.Access Tuple Items: You can access tuple items by referring to the index number, inside square [] brackets.
5.Change Tuple Values: Once a tuple is created, you cannot change its values. Tuples are unchangeable.
6.Add Items: Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
7.Remove Items: You cannot remove items in a tuple.
8.Check if Item Exists: To determine if a specified item is present in a tuple use the in keyword:

Syntax:
    varName = ()
    varName = (val_01,val_02,val_03...val_n)
"""
# Create Tuple with different kind of DataType
allValueTuple = (10, -5, "Test", 'V', 3.14, 3.14)
print(allValueTuple)

allValueTuple
# Update Tuple Value (It wont allow to update)
# allValueTuple[2] = "Software"

# Tuple Functions

#count(): Returns the number of times a specified value occurs in a tuple
print("##############################")
#Syntax:
#nameOfTuple.count(value)
print("count():", allValueTuple.count(3))

#index(): Searches the tuple for a specified value and returns the position of where it was found
print("##############################")
#Syntax:
#nameOfTuple.index(value)
print(allValueTuple.index(3.14))
print("##############################")

#Check if Item Exist
print("##############################")
#Syntax:
# if "ItemValue" in NameofTuple:
if 3.14 in allValueTuple:
    print("Item Exist in Tuple")
else:
    print("Item NOT Exist in Tuple")

