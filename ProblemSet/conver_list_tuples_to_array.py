import numpy as np

# Write a Python program to convert a list and tuple into arrays.
# List to array:
# [1 2 3 4 5 6 7 8]
# Tuple to array:
# [[8 4 6]
# [1 2 3]]

l1 = [1, 2, 3, 4, 5, 6, 7, 8]

print(f"List = {l1}")

tup = ((8, 4, 6), (1, 2, 3))

print(f"Tuple = {l1}")

array_from_list = np.array(l1)

array_from_tup = np.array(tup)

print(f"Array from list = {array_from_list}")
print(f"Array from tuple = {array_from_tup}")
