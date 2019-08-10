from numpy import *

# Create an 2D Array
row = int(input("Enter the Rows Count of an Array:"))
col = int(input("Enter the Cols Count of an Array:"))
print("Enter Values into an Array:")
matrix_01 = zeros([row, col], int)
# print("Initial Matrix Values:", matrix_01)

for i in range(0, row):
    for j in range(0, col):
        matrix_01[i][j] = int(input())

print(matrix_01)
