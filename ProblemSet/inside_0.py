import numpy as np

# 5. Write a Python program to create a 2d array with 1 on the border and 0 inside.
#

matrix = np.ones(25).reshape(5, 5)

print(matrix)

matrix[1:-1, 1:-1] = 0

print(matrix)
