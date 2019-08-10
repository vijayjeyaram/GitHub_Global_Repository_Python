# List
""""
1.List can hold any kind of Data Type.
2.List is a collection which is ordered and changeable.In Python tuples are written with square [] brackets.
3.Access Items: You access the list items by referring to the index number:
3.List can allows to hold duplicate values.
4.Change Item Value: To change the value of a specific item, refer to the index number:

Syntax:
    varName = []
    varName = [val_01,val_02,val_03...val_n]
"""
# Create Integer Values (Unsigned)
print("##############################")
signedValueList = [-10, -5, -10, -55, -25]
print("Signed List Values are:", signedValueList)

# Create Integer Values (Signed)
print("##############################")
unSignedValueList = [10, 5, 10, 55, 25]
print("UnSigned List Values are:", unSignedValueList)

# Create Various kinds of Data Types List
print("##############################")
allValueList = [10, -5, "Python", 3.14, 'V']
print("All Kind of List Values are:", allValueList)

# Retrieve all the values from the List using FOR Loop
print("##############################")
print("Retrieve List Values using FOR Loop:")
for l in allValueList:
    print(l)

# Retrieve Particular value from the List using Index Id (Left to Right -> 0,1,2....n-1)
print("##############################")
print("Retrieve Particular value from the List using Index Id (Left to Right -> 0,1,2....n-1)", allValueList[3])

# Retrieve Particular value from the List using Index Id (Right to Left -> -1,-2,-3....-n)
print("##############################")
print("Retrieve Particular value from the List using Index Id (Right to Left -> -1,-2,-3....-n)", allValueList[-3])

# Update List Value
print("##############################")
print("List Values Before Update:", allValueList)
allValueList[-3] = "Python Language"
print("List Values After Update:", allValueList)

# List Functions
""""
1.append(): Used for adding an elements to List.It is used to add elements to the last position of List.
Syntax:
    NameOfList.append (value)
    
2.insert(): Inserts an elements at specified position.
Syntax:
     NameOfList.insert(position(Index Id), value)
     
3.extend(): Add contents to List2 values List 1 at the end.
Syntax:
    List1.extend(List2)
    
4.sum() : Returns sum of all the elements of List.
Syntax:
     sum(NameOfList)
     
5.count():Returns total occurrence of given element of List.
Syntax:
    NameOfList.count(element)

6.length:Returns total length of List.
Syntax:
    len(NameOfList)

7.min() : Returns minimum Value of all the elements of List.    
Syntax:
    min(NameOfList)
    
8.max(): Returns maximum Value of all the elements of List.
Syntax:
    max(NameOfList)
    
9.reverse:Returns values from Right to Left
Syntax:
    NameOfList.reverse() 
10.Sort: This function can be used to sort list of integers, floating point number, string and others
###Ascending:
Syntax:
    NameOfList.sort()
###Descending:
Syntax:
    NameOfList.sort(reverse=True)
11.pop(): Index is not a necessary parameter, if not mentioned takes the last index.
Syntax:
     NameOfList.pop([index])
12.del() By Index: Element to be deleted is mentioned using list name and index.
Syntax:
    del NameOfList[index]

13.remove() By Index: Element to be deleted is mentioned using list name and element.
Syntax:
    NameOfList.remove(element)
    
14.Return the values using index range
Syntax:
    NameOfList[startIndex:EndIndex])
"""
# Create 2 Lists
print("##############################")
subject = ["Tamil", "English", "Maths", "Science", "Social Science"]
marks = [90, 73, 100, 100, 97]
print("Subject List Values - Before Appending New Subject:", subject)
print("Marks List Values - Before Appending New Subject Mark:", marks)

# append(): Add element to the last position
print("##############################")
subject.append("Computer Science")
marks.append(100)
print("Subject List Values - After Appending New Subject field:", subject)
print("Marks List Values - After Appending New Subject Mark value:", marks)

# insert(): Inserts an elements at specified position
print("##############################")
subject.insert(-7, "Id")
marks.insert(-7, 1)
print("Subject List Values - After Inserting New Id field:", subject)
print("Marks List Values - After Inserting New Id value:", marks)

# extend(): Add contents to List2 values List 1 at the end
print("##############################")
subject.extend(marks)
print("Merge 2 List:", subject)

# sum(): Returns sum of all the elements of List.
print("##############################")
print("sum():", sum(marks))

# count(): Returns total occurrence of given element of List.
print("##############################")
print("count():", subject.count(100))

# length(): Returns total length of List.
print("##############################")
print("lenght():", len(subject))

# min(): Returns minimum Value of all the elements of List.
print("##############################")
print("min():", min(marks))

# max(): Returns maximum Value of all the elements of List.
print("##############################")
print("max()", max(marks))

# reverse(): Returns values from Right to Left
print("##############################")
marks.reverse()
print("reverse()", marks)

# Sort(): This function can be used to sort list of integers, floating point number, string and others
print("##############################")
###Ascending:
marks.sort()
print("[Ascending]sort():", marks)

# Sort(): This function can be used to sort list of integers, floating point number, string and others
print("##############################")
###Descending:
marks.sort(reverse=True)
print("[Descending]sort():", marks)

#pop() By Index: Index is not a necessary parameter, if not mentioned takes the last index.
print("##############################")
marks.pop()
print("pop():", marks)

#del() By Index : Element to be deleted is mentioned using list name and index.
print("##############################")
del marks[2]
print("del():", marks)

#remove() By Value: Element to be deleted is mentioned using list name and element.
print("##############################")
marks.remove(100)
print("del():", marks)

#Retun the values using index range
print("##############################")
print("Return the value using Index Range:", subject[2:7])
print("##############################")