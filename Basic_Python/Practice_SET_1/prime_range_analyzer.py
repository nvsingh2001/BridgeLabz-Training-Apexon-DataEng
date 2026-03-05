import math


def isprime(num: int) -> bool:
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True


a = int(input())
b = int(input())
count = 0

for num in range(a, b + 1):
    if isprime(num):
        count += 1

print(count)
