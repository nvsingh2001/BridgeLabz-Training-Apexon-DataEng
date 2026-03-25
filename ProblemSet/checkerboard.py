import numpy as np

# 7. Write a Python program to create a 8x8 matrix and fill it with a checkerboard pattern.

matrix = np.zeros((8, 8))

matrix[0::2, 1::2] = 1
matrix[1::2, 0::2] = 1

print(matrix)
