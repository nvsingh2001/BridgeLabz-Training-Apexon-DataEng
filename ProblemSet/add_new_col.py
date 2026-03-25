import numpy as np

arr = np.array([[10, 20, 30], [40, 50, 60]])

print(arr)

arr = np.column_stack((arr, [100, 200]))

print(arr)
