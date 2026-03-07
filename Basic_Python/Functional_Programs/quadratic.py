import math

a, b, c = map(int, input().split())

delta = b * b - 4 * a * c

if delta < 0:
    print("Imaginary Roots")
else:
    root1 = (-b + math.sqrt(delta)) / (2 * a)
    root2 = (-b - math.sqrt(delta)) / (2 * a)

    print(f"Root1 = {root1}, Root2 = {root2}")
