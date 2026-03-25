import numpy as np


# 6. Write a Python program to add a border (filled with 0's) around an existing array.

matrix = np.ones(9).reshape(3, 3)

print(matrix)

matrix = np.pad(matrix, pad_width=1, mode="constant", constant_values=0)

print(matrix)
