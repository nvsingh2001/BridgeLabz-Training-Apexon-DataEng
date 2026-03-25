import numpy as np

# 9. Write a Python program to append values to the end of an array.
# Expected Output:
# Original array:
# [10, 20, 30]
#
# After append values to the end of the array:
# [10 20 30 40 50 60 70 80 90]


arr = np.arange(10, 40, 10)

print(arr)

for num in range(50, 110, 10):
    arr = np.append(arr, num)

print(arr)
