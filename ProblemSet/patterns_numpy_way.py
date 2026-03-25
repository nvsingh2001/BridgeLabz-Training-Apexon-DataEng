import numpy as np

n = 4
m = 3

arr = (np.arange(m) < np.arange(n)[:, None]).astype(float)

print(arr)

arr = (np.arange(n) < np.arange(m)[:, None]).astype(float)

print(arr)
