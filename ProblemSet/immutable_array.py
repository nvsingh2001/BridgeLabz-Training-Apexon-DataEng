import numpy as np


arr = np.arange(0, 11)

arr.flags.writeable = False

arr[2] = 45
