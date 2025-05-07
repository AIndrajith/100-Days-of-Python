# Matrix Operations with NumPy

import numpy as np

# create a 2 x 2 matrix

matrix = np.array([[1, 2],[3, 4]])
print(matrix)

A = np.array([[1, 2],[3, 4]])
B = np.array([[5, 6],[7, 8]])

# Addition
print("Addition:\n", A + B)

# Subtraction
print("Subtraction:\n", A - B)

# Multiplication
print("Element-wise Multiplication: \n", A * B)

# Dot Product
print("Dot Product:\n", np.dot(A,B))

# Transpose
print("Transpose of A: \n", A.T)

# Determinant
det = np.linalg.det(A)
print("Determinant: \n", det)

# Inverse
if det != 0:
    inverse = np.linalg.inv(A)
    print("Inverse:\n", inverse)
else:
    print("Matrix is not invertible")    