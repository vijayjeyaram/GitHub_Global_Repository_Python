from numpy import *

#Create Two 2D Array

#Array-1
row_matrix_01 = int(input("Enter the Row Count of an Array-01:"))
col_matrix_01 = int(input("Enter the Col Count of an Array-01:"))

print("Enter the Matrix-1 elements:")

#Create zero Array
matrix_01 = zeros([row_matrix_01, col_matrix_01], int)

#Update zero with other Number
for m1 in range(0, row_matrix_01):
    for m2 in range(0, col_matrix_01):
        matrix_01[m1][m2] = int(input())
print("Entered Elements in Matrix-1:\n", matrix_01)

#Array-2
row_matrix_02 = int(input("Enter the Row Count of an Array-02:"))
col_matrix_02 = int(input("Enter the Col Count of an Array-02:"))

print("Enter the Matrix-2 elements:")
#Create zero Array
matrix_02 = zeros([row_matrix_02, col_matrix_02], int)

for m3 in range(0, row_matrix_02):
    for m4 in range(0, col_matrix_02):
        matrix_02[m3][m4] = int(input())
print("Entered Elements in Matrix-2:\n", matrix_02)

#Mutiplication
matrix_03 = matrix_01 * matrix_02
print("Multiplication of Two Matrix:\n", matrix_03)

