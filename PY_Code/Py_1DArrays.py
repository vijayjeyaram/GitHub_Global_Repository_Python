# Arrays
""""
1.Python does not have built-in support for Arrays, but Python Lists can be used instead.
2.Arrays are used to store multiple values in one single variable.
3.Array can hold similar data Types
4.We can store n size of elements in the array. It does grow its size at runtime.

Syntax:
arrayName = array('DataTypeCode',[Val_01, Val_02, Val_03 ...Val_n])

from array import *
#Create an Integer Array - Method
fruits_Array = array('i', ["Apples", "Blueberries", "Dates", "Evergreen Huckleberry", "Finger Lime"])
print("Fruits Array: ", array.fruits_Array)
print(type(array.fruits_Array))
"""
from array import *

# Create an Array
marks_01_Array = array('i', [97, 90, 100, 100, 97])
print("Marks-01 Array: ", marks_01_Array)

marks_02_Array = array('i', [85, 80, 81, 82, 87])
print("Marks-02 Array: ", marks_02_Array)

# concat array
marks_03_Array = marks_01_Array + marks_02_Array
print(marks_03_Array)

# Iterate Array
print("##############################")
for val in marks_03_Array:
    print(val)
# copy array
print("##############################")
# Syntax:
# NameOfNewArray = array(GetDatTypeOf_FROM_Array,(var for var NameOfArray)
# NameOfNewArray = array(GetDatTypeOf_FROM_Array.typecode,(var for var NameOf_FROM_Array)
duplicateMarkArray = array(marks_03_Array.typecode, (x for x in marks_03_Array))
print(duplicateMarkArray)
for values in duplicateMarkArray:
    print(values)
