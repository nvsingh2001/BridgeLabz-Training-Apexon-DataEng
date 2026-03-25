import numpy as np

arr = np.zeros(9).reshape(3, 3)

print(arr)

np.fill_diagonal(arr, 1)

print(arr)
