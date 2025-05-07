# Handling User Input for Matrices

import numpy as np 

# Function to Create Matrix from user Input
def get_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    print("Enter the matrix elements row by row: ")
    elements = []
    for _ in range(rows):
        row = list(map(float, input().split()))
        elements.append(row)
    return np.array(elements)

# Example Usage
matrix = get_matrix()
print("Matrix: \n", matrix)