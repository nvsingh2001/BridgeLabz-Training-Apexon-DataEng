import sys
import math

x, y = int(sys.argv[1]), int(sys.argv[2])

distance = math.sqrt(x * x + y * y)

print(f"{distance:.2f}")
