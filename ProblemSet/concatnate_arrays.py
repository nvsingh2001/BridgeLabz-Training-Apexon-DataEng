import numpy as np


arr1 = [[0, 1, 3], [5, 7, 9]]
arr2 = [[0, 2, 4], [6, 8, 10]]


arr1 = np.array(arr1)
arr2 = np.array(arr2)

print(arr1)
print(arr2)

conatenated_array = np.concatenate((arr1, arr2), axis=1)


print(conatenated_array)
