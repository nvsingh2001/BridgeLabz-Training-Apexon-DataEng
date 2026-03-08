import random

n = int(input())

distinct_num = set([])

num_iteration = 0

while len(distinct_num) < n:
    distinct_num.add(random.randint(1, n))
    num_iteration += 1

print(num_iteration)
