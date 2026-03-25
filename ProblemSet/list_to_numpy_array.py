import numpy as np

# 1. Write a Python program to convert a list of numeric value into a one-dimensional
# NumPy array.
# Expected Output:
# Original List: [12.23, 13.32, 100, 36.32]
# One-dimensional numpy array: [ 12.23 13.32 100. 36.32]

original_list = [12.23, 13.32, 100, 36.32]

numpy_array = np.array(original_list)

print(original_list)
print(numpy_array)
