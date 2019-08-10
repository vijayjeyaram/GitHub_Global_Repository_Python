#Set
""""
1.List can hold any kind of Data Type.
2.A set is a collection which is unordered and unindexed. In Python sets are written with curly {} brackets.
3.List can NOT allows to hold duplicate values/It will Eliminate the Duplicate values.
4.Sets are unordered, so you cannot be sure in which order the items will appear.
5.Set using concept of hash.
6.Once a set is created, you cannot change its items, but you can add new items.
7.Access Items: You cannot access items in a set by referring to an index, since sets are unordered the items has no index.

Syntax:
    varName = {}
    varName = {val_01,val_02,val_03...val_n}
"""

#Create Set
print("##############################")
allDataSets = {5, -10, "Test", 3.14, 'V'}
print(allDataSets)

#Create Set with DuplicateValue (It will Eliminate the Duplicate value
print("##############################")
duplicateSets = {5, -10, "Test", 3.14, 'V', 3.14}
print(duplicateSets)
#Remove value from Set using ValueName
print("##############################")
duplicateSets.discard(5)
print(duplicateSets)

#Add Item to Sets
print("##############################")
#Syntax:
#NameOfSet.add([val_01, val_02, val_03 ...val_n])
#NameOfSet.add("value")
print("Add Single Item:", allDataSets)

#Add Multiple Item to Sets
print("##############################")
#Syntax:
#NameOfSet.update([val_01, val_02, val_03 ...val_n])
allDataSets.update([100, 1.73, "Engineer", 'e'])
print("Add Multiple Items:", allDataSets)
print("##############################")