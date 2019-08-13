# Dictionary
""""
1.A dictionary is a collection which is unordered, changeable and indexed.
2.In Python dictionaries are written with curly {} brackets, and they have keys and values.
3.Accessing Items: You can access the items of a dictionary by referring to its key name, inside square [] brackets.
4.Accessing Items:There is also a method called get() that will give you the same result
5.Change Values: You can change the value of a specific item by referring to its key name
6.Duplicate keys were NOT allowed.

Syntax:
    varName = {"key_01":value_01, "key_02":value_02, "key_03":value_03, ... "key_n":value_n}
"""

# Create a Dictionary
print("##############################")
studentMarkInfo = \
    {
        "Id": 1,
        "Name": "Vijay",
        "Tamil": 97,
        "English": 91,
        "Maths": 100,
        "Science": 98,
        "Social": 99
    }
print(studentMarkInfo)

#Accessing Items: You can access the items of a dictionary by referring to its key name, inside square brackets.
#Regular Way:
#Syntax:
#nameOfDictionary["Key"]
print("##############################")
print(studentMarkInfo["Name"])

#Using Method
#Syntax:
#nameOfDictionary.get("Key")
print(studentMarkInfo.get("Science"))

#Change Values: You can change the value of a specific item by referring to its key name:
print("##############################")
#Syntax:
#nameOfDictionary["Key"] = "Value"
studentMarkInfo["Science"] = 100
print(studentMarkInfo)

#Loop Through a Dictionary - Values
print("##############################")
for data in studentMarkInfo:
    print(data)

#You can also use the values() function to return values of a dictionary:
print("++++++++++++++++++++++++++++++")
for value in studentMarkInfo.values():
    print(value)

#Loop Through a Dictionary - Keys,Values
print("++++++++++++++++++++++++++++++")
for key_Values in studentMarkInfo:
    print(studentMarkInfo[key_Values])

#Loop through both keys and values, by using the items() function:
print("++++++++++++++++++++++++++++++")
for key, val in studentMarkInfo.items():
    print(key, val)

#Adding Items: Adding an item to the dictionary is done by using a new index key and assigning a value to it.
print("##############################")
#Syntax:
#nameOfDictionary["Key"] = "Value"
studentMarkInfo["Computer"] = 100
print(studentMarkInfo)
print("##############################")
#Removing Items: There are several methods to remove items from a dictionary:
#Syntax:
#nameOfDictionary("Key")
studentMarkInfo.pop("Computer")
print(studentMarkInfo)
print("##############################")
#Dynamic Dictionary
#Syntax:
#dict.fromkeys(keys, value)
#From List
myList = ["Key_01", "Key_02", "Key_03", "Key_04", "Key_05"]
myDictionary_01 = dict.fromkeys(myList, "Value")
print(myDictionary_01)

myDict = dict.fromkeys(range(1, 6), "Test")
print(myDict)

# Definition and Usage
# The setdefault() method returns the value of the item with the specified key.
# If the key does not exist, insert the key, with the specified value, see example below

#Syntax:
#dictionary.setdefault(key_name, value)

studentMarkInfo = \
    {
        "Id": 1,
        "Name": "Vijay",
        "Tamil": 97,
        "English": 91,
        "Maths": 100,
        "Science": 98,
        "Social": 99
    }
print(studentMarkInfo)
# Here Science Mark has been existing so its return the value.
scienceMark = studentMarkInfo.setdefault("Science")
print(scienceMark)

# Here ComputerScience Mark has NOT existing so its insert the key.
computerMark = studentMarkInfo.setdefault("Computer")
print(computerMark)
print(studentMarkInfo)