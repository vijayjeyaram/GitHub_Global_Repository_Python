# Single Dimensional Array
"""
1.Required "numpy" Lib to work with Multi Dimensional Array.
2.Do not Specify the Data Type Code.

Syntax:
nameOfArray = array([Val_01, Val_02, Val_03 ...Val_n])
"""
from numpy import *

# Create 1D Array - Regular Way
print("##############################")
marks_Array = array([97, 95, 100, 98, 97])
print("Variable DataType:", type(marks_Array))
print("value DataType:", marks_Array.dtype)
print(marks_Array)

fruits_Array = array(["Apple", "Orange", "Grapes"])
print(fruits_Array)

# Create 1D Array - Using linspace()
print("##############################")
myArray_01 = linspace(0, 10, 11)
print(myArray_01)

# Add n to the existing array
print("##############################")
val_Array = array([35, 50, 15, 20, 25])
print("Before Add '5':", val_Array)
val_Array = val_Array + 5

print("After Add '5':", val_Array)

for v in val_Array:
    val_Array = v + 5
    print("After Add '5' Through For Loop:", val_Array)

# copy Array:
print("##############################")
# Shallow Copy
myArray_01 = array([5, 10, 15, 20, 30])
myArray_02 = myArray_01.view()
print("Address of myArray_01:", id(myArray_01))
print("Address of myArray_02:", id(myArray_02))
print("Shallow - Copy myArray_01 to myArray_02:", myArray_02)

# Deep Copy
myArray_03 = array([5.1, 10.1, 15.1, 20.1, 30.1])
myArray_05 = myArray_03.copy()
print("Address of myArray_03:", id(myArray_03))
print("Address of myArray_05:", id(myArray_05))
print("Deep - Copy myArray_03 to myArray_05:", myArray_05)
