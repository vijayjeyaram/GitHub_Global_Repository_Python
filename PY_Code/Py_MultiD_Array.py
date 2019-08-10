# Multi Dimensional Array
"""
1.Required "numpy" Lib to work with Multi Dimensional Array.
2.Do not Specify the Data Type Code.

Syntax:
1DArray = array([Val_01, Val_02, Val_03 ...Val_n])
2DArray = array([[Val_01, Val_02, Val_03 ...Val_n], [Val_01, Val_02, Val_03 ...Val_n]])
3DArray = ([[[Val_01, Val_02, Val_03 ...Val_n]], [Val_01, Val_02, Val_03 ...Val_n], [Val_01, Val_02, Val_03 ...Val_n]]])
anyDArray = zeros(NoOfRows,NoOfCols) -- Default values will be zero
anyDArray = ones(NoOfRows,NoOfCols) -- Default values will be one
"""

from numpy import *

# Create 2D Array
myArray_01 = array([[10, 15, 20, 25, 30], [35, 40, 45, 50, 55]])
print("Display Array:", myArray_01)
print("Data Type of Array Variable:", type(myArray_01))
print("Data Type of Array Value:", myArray_01.dtype)
print("Display Rank of an Array:", myArray_01.ndim)
print("(Row,Col) of an Array:", myArray_01.shape)
print("Count Elements:", myArray_01.size)

# Array Conversion:
# Convert MultiD to 1D:
my2DArray = array([[10, 15, 20, 25, 30, 60], [35, 40, 45, 50, 55, 65]])
my1DArray = my2DArray.flatten()
print("Converted from MultiD array to 1D Array:", my1DArray)
print("Display Rank of an Array:", my1DArray.ndim)
# print("Converted from MultiD array to 1D Array:", myArray_01.flatten())

# Create a 1D Array using zeros() function
zeros1DArray = zeros([5], int)
print(zeros1DArray)

zeros2DArray = zeros([3, 3], int)
print(zeros2DArray)
